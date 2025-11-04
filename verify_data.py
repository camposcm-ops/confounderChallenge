"""Quick verification script for the data files."""
import pandas as pd

# Check observational data
df_obs = pd.read_csv('patients_data.csv')
print("Observational Data:")
print(f"  Total patients: {len(df_obs)}")
print(f"  Doc Dreamy mean: {df_obs[df_obs['doctor_name'] == 'Doc Dreamy']['post_surgical_score'].mean():.2f}")
print(f"  Doc Duck mean: {df_obs[df_obs['doctor_name'] == 'Doc Duck']['post_surgical_score'].mean():.2f}")
print(f"  Doc Dreamy severity mean: {df_obs[df_obs['doctor_name'] == 'Doc Dreamy']['severity'].mean():.2f}")
print(f"  Doc Duck severity mean: {df_obs[df_obs['doctor_name'] == 'Doc Duck']['severity'].mean():.2f}")

# Check randomized data
df_rand = pd.read_csv('patients_data_randomized.csv')
print("\nRandomized Data:")
print(f"  Total patients: {len(df_rand)}")
print(f"  Doc Dreamy mean: {df_rand[df_rand['doctor_name'] == 'Doc Dreamy']['post_surgical_score'].mean():.2f}")
print(f"  Doc Duck mean: {df_rand[df_rand['doctor_name'] == 'Doc Duck']['post_surgical_score'].mean():.2f}")
print(f"  Doc Dreamy severity mean: {df_rand[df_rand['doctor_name'] == 'Doc Dreamy']['severity'].mean():.2f}")
print(f"  Doc Duck severity mean: {df_rand[df_rand['doctor_name'] == 'Doc Duck']['severity'].mean():.2f}")

print("\n✓ Data verification complete!")

