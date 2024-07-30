import pandas as pd
import ast

# Load data
df = pd.read_csv("cmu_ipa_cambridge.csv")

# Define the discrepant function
def discrepant(row):
    # Check if the columns are already lists
    cm = row['Cambridge IPAs']
    mp = row['Matched Pronunciations (IPA)']
    
    # Parse the string representation of lists if they are not already lists
    if isinstance(cm, str):
        cm = ast.literal_eval(cm)
    if isinstance(mp, str):
        mp = ast.literal_eval(mp)
    return len(cm) > 0 and len(mp) == 0

# Apply the function to filter the rows
discrepant_df = df[df.apply(discrepant, axis=1)]
discrepant_words = discrepant_df['CMU Word'].tolist()

print(f"Words present in both dictionaries but with no pronunciation matches (Method 1): {len(discrepant_words)}")
# Function to safely evaluate strings to lists
def parse_list(column):
    return column.apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

# Parse the list columns
df['CMU IPAs'] = parse_list(df['CMU IPAs'])
df['Cambridge IPAs'] = parse_list(df['Cambridge IPAs'])
df['Matched Pronunciations (IPA)'] = parse_list(df['Matched Pronunciations (IPA)'])

# Filter the DataFrame
filtered_df = df[(df['CMU IPAs'].apply(len) > 0) & 
                 (df['Cambridge IPAs'].apply(len) > 0) & 
                 (df['Matched Pronunciations (IPA)'].apply(len) == 0)]

print("Filtered df")
print(filtered_df.shape)

filtered_words = filtered_df['CMU Word'].tolist()

print(f"Words present in both dictionaries but with no pronunciation matches (Method 2): {len(filtered_words)}")
# Compare the two lists and output the differences
discrepant_set = set(discrepant_words)
filtered_set = set(filtered_words)

# Words in Method 1 but not in Method 2
diff_1_not_2 = discrepant_set - filtered_set
# Words in Method 2 but not in Method 1
diff_2_not_1 = filtered_set - discrepant_set

print(f"Words in Method 1 but not in Method 2: {len(diff_1_not_2)}")
print(f"Words in Method 2 but not in Method 1: {len(diff_2_not_1)}")

# Optionally, print the lists of differences
print(f"Words in Method 1 but not in Method 2: {list(diff_1_not_2)}")
print(f"Words in Method 2 but not in Method 1: {list(diff_2_not_1)}")
