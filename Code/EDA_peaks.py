import neurokit2 as nk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

eda_resting1_peaks_n = pd.read_csv("segmented_data\EDA\Resting_1\eda_analysis_results.csv")
eda_cvemp_peaks_n = pd.read_csv("segmented_data\EDA\cVemp\eda_analysis_results.csv")
eda_resting2_peaks_n = pd.read_csv("segmented_data\EDA\Resting_2\eda_analysis_results.csv")

box1 = eda_resting1_peaks_n["SCR_Peaks_N"]
box2 = eda_cvemp_peaks_n["SCR_Peaks_N"]
box3 = eda_resting2_peaks_n["SCR_Peaks_N"]

data = pd.DataFrame({
    'Baseline': box1,
    'cVemp': box2,
    'Resting': box3})


sns.boxplot(data=data)
plt.xlabel('Measurement periods')
plt.ylabel('Number of SCR ocurrences ')
plt.title('Variation of SCR ocurrences')
plt.show()



