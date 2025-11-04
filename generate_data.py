"""
Generate data files for the confounder challenge.
This script creates two datasets:
1. patients_data.csv - Observational data with confounding
2. patients_data_randomized.csv - Randomized data without confounding
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

n_patients = 100

# ============================================================================
# Observational Data (with confounding)
# ============================================================================
# In observational data:
# - Patient severity influences doctor choice (confounding)
# - Low severity patients -> Doc Dreamy (doctor_id = 1)
# - High severity patients -> Doc Duck (doctor_id = 0)
# - Doc Dreamy gets easier cases, so his average is lower (better) = 2.8
# - Doc Duck gets harder cases, so his average is higher (worse) = 3.38

# Generate patient severity (standard normal)
severity = np.random.normal(0, 1, n_patients)

# Doctor assignment based on severity (confounding)
# Low severity -> Doc Dreamy (1), High severity -> Doc Duck (0)
# Use a sigmoid-like function to create the relationship
doctor_prob = 1 / (1 + np.exp(severity))  # Low severity = high prob of Dreamy
doctor_id = np.random.binomial(1, doctor_prob)

# Create doctor names
doctor_name = np.where(doctor_id == 1, 'Doc Dreamy', 'Doc Duck')

# Generate post-surgical scores
# True effect: Doc Duck is actually better (lower scores)
# But confounding makes Doc Dreamy look better
# Score = base + severity_effect + doctor_effect + noise

base_score = 3.0
severity_effect = 1.2 * severity  # Higher severity -> worse outcomes (stronger effect for confounding)
# True doctor effect: Doc Duck is better (lower scores by 0.75)
# But in observational data, Dreamy gets easier cases, so his average is lower
doctor_effect = np.where(doctor_id == 0, -0.75, 0)  # Doc Duck is better
noise = np.random.normal(0, 0.4, n_patients)

post_surgical_score = base_score + severity_effect + doctor_effect + noise

# Create dataframe
patients_df = pd.DataFrame({
    'patient': range(1, n_patients + 1),
    'severity': severity,
    'doctor_id': doctor_id,
    'doctor_name': doctor_name,
    'post_surgical_score': post_surgical_score
})

# Verify means are close to target
print("Observational Data:")
print(f"Doc Dreamy mean: {patients_df[patients_df['doctor_name'] == 'Doc Dreamy']['post_surgical_score'].mean():.2f}")
print(f"Doc Duck mean: {patients_df[patients_df['doctor_name'] == 'Doc Duck']['post_surgical_score'].mean():.2f}")
print(f"Doc Dreamy severity mean: {patients_df[patients_df['doctor_name'] == 'Doc Dreamy']['severity'].mean():.2f}")
print(f"Doc Duck severity mean: {patients_df[patients_df['doctor_name'] == 'Doc Duck']['severity'].mean():.2f}")

# Save to CSV
patients_df.to_csv('patients_data.csv', index=False)
print("\nSaved: patients_data.csv")

# ============================================================================
# Randomized Data (no confounding)
# ============================================================================
# In randomized data:
# - Doctor assignment is random (no relationship with severity)
# - Doc Duck's true skill shows through (mean = 2.71)
# - Doc Dreamy's true skill shows through (mean = 3.46)

# Generate new patient severity (standard normal)
severity_rand = np.random.normal(0, 1, n_patients)

# Random doctor assignment (no relationship with severity)
doctor_id_rand = np.random.binomial(1, 0.5, n_patients)
doctor_name_rand = np.where(doctor_id_rand == 1, 'Doc Dreamy', 'Doc Duck')

# Generate post-surgical scores
# True effect: Doc Duck is better (lower scores)
# No confounding, so true effect shows
base_score_rand = 3.0
severity_effect_rand = 0.8 * severity_rand  # Higher severity -> worse outcomes
# True doctor effect: Doc Duck is better (lower scores by 0.75)
doctor_effect_rand = np.where(doctor_id_rand == 0, -0.75, 0)  # Doc Duck is better
noise_rand = np.random.normal(0, 0.4, n_patients)

post_surgical_score_rand = base_score_rand + severity_effect_rand + doctor_effect_rand + noise_rand

# Create dataframe
patients_randomized_df = pd.DataFrame({
    'patient': range(1, n_patients + 1),
    'severity': severity_rand,
    'doctor_id': doctor_id_rand,
    'doctor_name': doctor_name_rand,
    'post_surgical_score': post_surgical_score_rand
})

# Verify means are close to target
print("\nRandomized Data:")
print(f"Doc Dreamy mean: {patients_randomized_df[patients_randomized_df['doctor_name'] == 'Doc Dreamy']['post_surgical_score'].mean():.2f}")
print(f"Doc Duck mean: {patients_randomized_df[patients_randomized_df['doctor_name'] == 'Doc Duck']['post_surgical_score'].mean():.2f}")
print(f"Doc Dreamy severity mean: {patients_randomized_df[patients_randomized_df['doctor_name'] == 'Doc Dreamy']['severity'].mean():.2f}")
print(f"Doc Duck severity mean: {patients_randomized_df[patients_randomized_df['doctor_name'] == 'Doc Duck']['severity'].mean():.2f}")

# Save to CSV
patients_randomized_df.to_csv('patients_data_randomized.csv', index=False)
print("\nSaved: patients_data_randomized.csv")

print("\nData generation complete!")

