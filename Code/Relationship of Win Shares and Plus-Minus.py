import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset.csv")

# Metrics to compare with WS
metrics = ['BPM', 'VORP', 'DARKO', 'CPM']

results = []
for metric in metrics:
    if metric in df.columns and 'WS' in df.columns:
        r = df['WS'].corr(df[metric])
        r_squared = r ** 2
        results.append({'Metric': metric, 'r': r, 'r²': r_squared})
    else:
        results.append({'Metric': metric, 'r': None, 'r²': None})

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Save results
results_df.to_csv("Correlation_Results.csv", index=False)

# Print confirmation and preview
print("✅ Correlation results saved as Correlation_Results.csv\n")
print(results_df)
