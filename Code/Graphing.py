import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import linregress

# Load dataset
df = pd.read_csv("Dataset_with_Expected_and_Value.csv")

# Clean and convert money values to numeric
def clean_money(x):
    if pd.isna(x):
        return None
    return float(str(x).replace('$', '').replace(',', '').strip())

df['Value (WS)'] = df['Value (WS)'].apply(clean_money)
df['Value (VORP)'] = df['Value (VORP)'].apply(clean_money)

# Drop rows missing required data
df = df.dropna(subset=['Value (WS)', 'Value (VORP)'])

# --- LINEAR REGRESSION & CORRELATION ---
slope, intercept, r_value, p_value, std_err = linregress(df['Value (WS)'], df['Value (VORP)'])
r_squared = r_value ** 2

# Create regression line values
x_vals = np.linspace(df['Value (WS)'].min(), df['Value (WS)'].max(), 100)
y_vals = intercept + slope * x_vals

# --- PLOT SETUP ---
plt.figure(figsize=(13, 9))
sns.set(style="whitegrid")

# Scatter plot of players
plt.scatter(df['Value (WS)'], df['Value (VORP)'], color='dodgerblue', alpha=0.7, s=40, edgecolor='white')

# Plot regression line
plt.plot(x_vals, y_vals, color='black', linestyle='-', linewidth=2, label=f"Regression Line (r² = {r_squared:.3f})")

# Axis limits
plt.xlim(-50_000_000, 50_000_000)
plt.ylim(-60_000_000, 120_000_000)

# Axis ticks every $10M, based on limits
x_ticks = np.arange(-50_000_000, 50_000_001, 10_000_000)
y_ticks = np.arange(-60_000_000, 120_000_001, 10_000_000)
x_tick_labels = [f"${t/1_000_000:.0f}M" for t in x_ticks]
y_tick_labels = [f"${t/1_000_000:.0f}M" for t in y_ticks]

plt.xticks(x_ticks, x_tick_labels, rotation=45, fontsize=10)
plt.yticks(y_ticks, y_tick_labels, fontsize=10)

# Add center lines
plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.axhline(0, color='black', linestyle='--', linewidth=1)

# Annotate each player
for _, row in df.iterrows():
    plt.text(row['Value (WS)'], row['Value (VORP)'], str(row['Name']), fontsize=8, alpha=0.75)

# Quadrant labels
plt.text(25_000_000, 120_000_000, "High WS / High VORP", fontsize=13, color='green', weight='bold', ha='center')
plt.text(-25_000_000, 120_000_000, "Low WS / High VORP", fontsize=13, color='orange', weight='bold', ha='center')
plt.text(25_000_000, -55_000_000, "High WS / Low VORP", fontsize=13, color='orange', weight='bold', ha='center')
plt.text(-25_000_000, -55_000_000, "Low WS / Low VORP", fontsize=13, color='red', weight='bold', ha='center')

# Titles and labels
plt.title("Expected Win Shares vs Expected VORP (Quadrant Analysis)", fontsize=18, weight='bold', pad=20)
plt.xlabel("Value (WS) — Difference Between Expected WS ($USD) and Salary", fontsize=13, labelpad=10)
plt.ylabel("Value (VORP) — Difference Between Expected VORP ($USD) and Salary", fontsize=13, labelpad=10)

# Add correlation coefficient text on the plot
plt.text(-45_000_000, 110_000_000, f"r = {r_value:.3f}\nr² = {r_squared:.3f}", fontsize=12, color='black',
         bbox=dict(facecolor='white', edgecolor='gray', alpha=0.7))

plt.legend()
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()

# Print stats to console
print("📊 Linear Regression Results:")
print(f"  Slope: {slope:.4f}")
print(f"  Intercept: {intercept:.4f}")
print(f"  r: {r_value:.4f}")
print(f"  r²: {r_squared:.4f}")
print(f"  p-value: {p_value:.6f}")
