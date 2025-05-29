
from google.colab import files
uploaded = files.upload()

filename = "API_SP.POP.TOTL_DS2_en_csv_v2_375396.csv"  
df = pd.read_csv(filename, skiprows=4)

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# Upload CSV manually
uploaded = files.upload()

# Use the exact name shown after upload
filename = list(uploaded.keys())[0]

# Read the file (skip metadata)
df = pd.read_csv(filename, skiprows=4)

# Continue analysis as planned...
df_pop = df[["Country Name", "2022"]].dropna()
top_10 = df_pop.sort_values(by="2022", ascending=False).head(10)
top_10.columns = ["Country", "Population"]

# Plot
plt.figure(figsize=(12, 6))
plt.bar(top_10["Country"], top_10["Population"], color='orchid')
plt.title("Top 10 Most Populous Countries (2022)", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
