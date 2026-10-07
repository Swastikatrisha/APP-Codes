import numpy as np
import pandas as pd

# 1. Create a NumPy array of course fees (in ₹)
fees = np.array([18000, 32000, 25000, 45000, 12000, 28000, 50000, 22000])

# 2. Calculate average, maximum, and minimum course fee
avg_fee = np.mean(fees)
max_fee = np.max(fees)
min_fee = np.min(fees)

print("--- Course Fee Statistics ---")
print(f"Average Fee: ₹{avg_fee:,.2f}")
print(f"Maximum Fee: ₹{max_fee:,.2f}")
print(f"Minimum Fee: ₹{min_fee:,.2f}\n")

# 3. Create a Pandas DataFrame
course_data = {
    "Course_ID": ["C101", "C102", "C103", "C104", "C105", "C106", "C107", "C108"],
    "Course_Name": [
        "Web Development",
        "Data Science",
        "Graphic Design",
        "Cloud Computing",
        "Cybersecurity",
        "AI & Machine Learning",
        "Full Stack Java",
        "Digital Marketing"
    ],
    "Duration_Months": [3, 6, 2, 6, 2, 8, 6, 3],
    "Course_Fee": fees
}

df = pd.DataFrame(course_data)

print("--- Complete Course DataFrame ---")
print(df)
print("\n")

# 4. Display courses whose fee is greater than ₹25,000
high_fee_courses = df[df["Course_Fee"] > 25000]

print("--- Courses with Fee > ₹25,000 ---")
print(high_fee_courses.to_string(index=False))
