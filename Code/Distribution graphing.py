import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# Clean numeric columns
for col in ['WS', 'VORP']:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(r'[^0-9.\-]', '', regex=True)
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')

# --- 1. Distribution of Win Shares (WS) ---
plt.figure(figsize=(10, 6))
plt.hist(df['WS'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title("Distribution of Win Shares (WS) Among NBA Players", fontsize=16, weight='bold')
plt.xlabel("Win Shares (WS)", fontsize=12)
plt.ylabel("Number of Players", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# --- 2. Distribution of VORP ---
plt.figure(figsize=(10, 6))
plt.hist(df['VORP'].dropna(), bins=30, color='lightcoral', edgecolor='black')
plt.title("Distribution of VORP Among NBA Players", fontsize=16, weight='bold')
plt.xlabel("Value Over Replacement Player (VORP)", fontsize=12)
plt.ylabel("Number of Players", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
