import neurokit2 as nk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

eda_resting1 = pd.read_csv("segmented_data\EDA\Resting_1\eda_analysis_results.csv")
eda_cvemp = pd.read_csv("segmented_data\EDA\cVemp\eda_analysis_results.csv")
eda_resting2 = pd.read_csv("segmented_data\EDA\Resting_2\eda_analysis_results.csv")

box1 = eda_resting1["EDA_Tonic"]
box2 = eda_cvemp["EDA_Tonic"]
box3 = eda_resting2["EDA_Tonic"]

data = pd.DataFrame({
    'Baseline': box1,
    'cVemp': box2,
    'Resting': box3})


sns.boxplot(data=data)
plt.xlabel('Measurement periods')
plt.ylabel('Tonic Magnitude')
plt.title('Averaged EDA Tonic Components')
plt.show()
