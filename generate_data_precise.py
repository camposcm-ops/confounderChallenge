"""
Generate data files for the confounder challenge with precise target means.
Target means:
- Observational: Doc Dreamy = 2.8, Doc Duck = 3.38
- Randomized: Doc Dreamy = 3.46, Doc Duck = 2.71
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

n_patients = 100

# ============================================================================
# Observational Data (with confounding)
# ============================================================================
# Target: Doc Dreamy = 2.8, Doc Duck = 3.38
# Strategy: Generate data that matches these means

# Generate patient severity (standard normal)
severity = np.random.normal(0, 1, n_patients)

# Doctor assignment based on severity (confounding)
# Low severity -> Doc Dreamy (1), High severity -> Doc Duck (0)
# Strong relationship: low severity patients prefer Dreamy
doctor_prob = 1 / (1 + np.exp(1.5 * severity))  # Adjusted for stronger confounding
doctor_id = np.random.binomial(1, doctor_prob)

# Create doctor names
doctor_name = np.where(doctor_id == 1, 'Doc Dreamy', 'Doc Duck')

# Generate post-surgical scores
# True effect: Doc Duck is actually better (lower scores by 0.75)
# But confounding makes Doc Dreamy look better because he gets easier cases

# Model: score = base + severity_coef * severity + doctor_effect + noise
# For Doc Dreamy (target mean = 2.8): 
#   - Gets lower severity patients (mean severity ≈ -0.5)
#   - No doctor effect (or small positive)
# For Doc Duck (target mean = 3.38):
#   - Gets higher severity patients (mean severity ≈ 0.5)
#   - Has doctor effect making him better (but confounding hides it)

base_score = 3.0
severity_coef = 1.0  # Higher severity -> worse outcomes
doctor_effect = np.where(doctor_id == 0, -0.75, 0)  # Doc Duck is better
noise = np.random.normal(0, 0.35, n_patients)

post_surgical_score = base_score + severity_coef * severity + doctor_effect + noise

# Adjust to match target means exactly
dreamy_mask = doctor_id == 1
duck_mask = doctor_id == 0

dreamy_current_mean = post_surgical_score[dreamy_mask].mean()
duck_current_mean = post_surgical_score[duck_mask].mean()

# Adjust Dreamy scores to target 2.8
post_surgical_score[dreamy_mask] += (2.8 - dreamy_current_mean)
# Adjust Duck scores to target 3.38
post_surgical_score[duck_mask] += (3.38 - duck_current_mean)

# Create dataframe
patients_df = pd.DataFrame({
    'patient': range(1, n_patients + 1),
    'severity': severity,
    'doctor_id': doctor_id,
    'doctor_name': doctor_name,
    'post_surgical_score': post_surgical_score
})

# Verify means
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
# Target: Doc Dreamy = 3.46, Doc Duck = 2.71
# Strategy: Random assignment, true doctor effect shows

# Generate new patient severity (standard normal)
severity_rand = np.random.normal(0, 1, n_patients)

# Random doctor assignment (no relationship with severity)
doctor_id_rand = np.random.binomial(1, 0.5, n_patients)
doctor_name_rand = np.where(doctor_id_rand == 1, 'Doc Dreamy', 'Doc Duck')

# Generate post-surgical scores
# True effect: Doc Duck is better (lower scores)
# No confounding, so true effect shows
base_score_rand = 3.0
severity_coef_rand = 0.8  # Higher severity -> worse outcomes
doctor_effect_rand = np.where(doctor_id_rand == 0, -0.75, 0)  # Doc Duck is better
noise_rand = np.random.normal(0, 0.4, n_patients)

post_surgical_score_rand = base_score_rand + severity_coef_rand * severity_rand + doctor_effect_rand + noise_rand

# Adjust to match target means exactly
dreamy_mask_rand = doctor_id_rand == 1
duck_mask_rand = doctor_id_rand == 0

dreamy_current_mean_rand = post_surgical_score_rand[dreamy_mask_rand].mean()
duck_current_mean_rand = post_surgical_score_rand[duck_mask_rand].mean()

# Adjust Dreamy scores to target 3.46
post_surgical_score_rand[dreamy_mask_rand] += (3.46 - dreamy_current_mean_rand)
# Adjust Duck scores to target 2.71
post_surgical_score_rand[duck_mask_rand] += (2.71 - duck_current_mean_rand)

# Create dataframe
patients_randomized_df = pd.DataFrame({
    'patient': range(1, n_patients + 1),
    'severity': severity_rand,
    'doctor_id': doctor_id_rand,
    'doctor_name': doctor_name_rand,
    'post_surgical_score': post_surgical_score_rand
})

# Verify means
print("\nRandomized Data:")
print(f"Doc Dreamy mean: {patients_randomized_df[patients_randomized_df['doctor_name'] == 'Doc Dreamy']['post_surgical_score'].mean():.2f}")
print(f"Doc Duck mean: {patients_randomized_df[patients_randomized_df['doctor_name'] == 'Doc Duck']['post_surgical_score'].mean():.2f}")
print(f"Doc Dreamy severity mean: {patients_randomized_df[patients_randomized_df['doctor_name'] == 'Doc Dreamy']['severity'].mean():.2f}")
print(f"Doc Duck severity mean: {patients_randomized_df[patients_randomized_df['doctor_name'] == 'Doc Duck']['severity'].mean():.2f}")

# Save to CSV
patients_randomized_df.to_csv('patients_data_randomized.csv', index=False)
print("\nSaved: patients_data_randomized.csv")

print("\nData generation complete!")

