import pandas as pd

# Load sums.csv
sums_df = pd.read_csv("sums.csv")

# Function to clean numeric strings
def clean_numeric(s):
    return float(str(s).replace('$', '').replace(',', '').strip())

# Extract Salary/Stat for WS and VORP, clean and convert to float
salary_per_ws = clean_numeric(sums_df.loc[sums_df['Column'] == 'WS', 'Salary/Stat'].values[0])
salary_per_vorp = clean_numeric(sums_df.loc[sums_df['Column'] == 'VORP', 'Salary/Stat'].values[0])

# Load dataset
df = pd.read_csv("Dataset.csv")

# Clean numeric columns in case there are non-numeric characters
for col in ['WS', 'VORP', 'Salary']:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(r'[^0-9.\-]', '', regex=True)
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Compute expected values (numeric)
df['Expected WS (Salary)'] = df['WS'] * salary_per_ws
df['Expected VORP (Salary)'] = df['VORP'] * salary_per_vorp

# Compute Value columns: Salary - Expected
df['Value (WS)'] = df['Expected WS (Salary)'] - df['Salary']
df['Value (VORP)'] = df['Expected VORP (Salary)'] - df['Salary']

# Format Expected and Value columns as dollar strings, rounded to 0 decimals
for col in ['Expected WS (Salary)', 'Expected VORP (Salary)', 'Value (WS)', 'Value (VORP)']:
    df[col] = df[col].round(0).apply(lambda x: f"${int(x):,}" if pd.notna(x) else "")

# Rename formatted Expected columns
df.rename(columns={'Expected WS (Salary)': 'Expected WS', 'Expected VORP (Salary)': 'Expected VORP'}, inplace=True)

# Save updated dataset
df.to_csv("Dataset_with_Expected_and_Value.csv", index=False)

print("✅ Dataset updated with Expected and Value columns saved as Dataset_with_Expected_and_Value.csv")
print(df[['WS', 'Expected WS', 'Value (WS)', 'VORP', 'Expected VORP', 'Value (VORP)']].head(10))
