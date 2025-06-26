import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


files = {
    "Baseline": "segmented_data/EGG/resting_1/egg_analysis_results.csv",
    "cVemp": "segmented_data/EGG/cVemp/egg_analysis_results.csv",
    "Resting": "segmented_data/EGG/resting_2/egg_analysis_results.csv"
}

data_frames = []

for state, file_path in files.items():
    df = pd.read_csv(file_path)
    df["State"] = state  
    data_frames.append(df)

data = pd.concat(data_frames, ignore_index=True)

state_order = ["Baseline", "cVemp", "Resting"]
data["State"] = pd.Categorical(data["State"], categories=state_order, ordered=True)

colors = {
    "Baseline": "#3CB371",  # Medium Sea Green
    "cVemp": "#CD5C5C",     # Indian Red
    "Resting": "#4682B4"    # Steel Blue
}
plt.figure(figsize=(10, 6))
sns.boxplot(x="State", y="EGG_Dominant_Freq", data=data, order=state_order, palette=colors, linewidth=2.5)


# plt.title("Dominant Frequency ", fontsize=20)
plt.xlabel("Measurement Stage", fontsize=20)
plt.ylabel("Dominant Frequency (Hz)", fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(axis='y', linestyle='--', alpha=1)
plt.show()

