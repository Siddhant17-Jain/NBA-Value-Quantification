import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# Columns to analyze
cols = ['WS', 'BPM', 'VORP', 'DARKO', 'CPM', 'Salary']

# Clean and safely convert to numeric
for col in cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(r'[^0-9.\-]', '', regex=True)  # keep only digits, dots, negatives
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')  # turn bad values into NaN safely

# Compute sums and averages (NaN ignored)
sums = df[cols].sum()
averages = df[cols].mean()

# Convert to DataFrames
sums_df = pd.DataFrame({'Column': sums.index, 'Sum': sums.values})
averages_df = pd.DataFrame({'Column': averages.index, 'Average': averages.values})

# Merge sums and averages for a unified CSV
summary_df = pd.merge(sums_df, averages_df, on="Column")

# Save to CSV
summary_df.to_csv("sums_and_averages.csv", index=False)

# Print confirmation and preview
print("✅ Cleaned, summed, and averaged values saved as sums_and_averages.csv\n")
print(summary_df)

# Print league-wide averages specifically for WS and VORP
print("\n🏀 League-Wide Averages:")
print(f"• Average WS: {averages['WS']:.2f}")
print(f"• Average VORP: {averages['VORP']:.2f}")
