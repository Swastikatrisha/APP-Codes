import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
np.random.seed(42)  # For reproducible results
s = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(s)

# Indexing
print("\nElement at index 3:")
print(s[3])

# Filtering: numbers greater than 50
print("\nNumbers greater than 50:")
print(s[s > 50])

# Statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())
