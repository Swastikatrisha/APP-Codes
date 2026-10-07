import numpy as np
import pandas as pd

# 1. Create a NumPy array of treatment costs (in ₹)
costs = np.array([12500, 35000, 18000, 45000, 22000, 9500, 28000, 15000])

# 2. Calculate mean, maximum, and minimum treatment cost
mean_cost = np.mean(costs)
max_cost = np.max(costs)
min_cost = np.min(costs)

print("--- Treatment Cost Statistics ---")
print(f"Mean Cost:    ₹{mean_cost:,.2f}")
print(f"Maximum Cost: ₹{max_cost:,.2f}")
print(f"Minimum Cost: ₹{min_cost:,.2f}\n")

# 3. Create a Pandas DataFrame with sample patient records
patient_data = {
    "Patient_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Patient_Name": ["Aarav", "Ananya", "Rohan", "Priya", "Vikram", "Neha", "Sanjay", "Kavita"],
    "Treatment": ["Fever", "Surgery", "Dental", "Cardiology", "Orthopedic", "General Checkup", "Neurology", "ENT"],
    "Treatment_Cost": costs
}

df = pd.DataFrame(patient_data)

print("--- Complete Hospital DataFrame ---")
print(df)
print("\n")

# 4. Filter and display patients whose treatment cost exceeds ₹20,000
high_cost_patients = df[df["Treatment_Cost"] > 20000]

print("--- Patients with Treatment Cost Exceeding ₹20,000 ---")
print(high_cost_patients.to_string(index=False))
