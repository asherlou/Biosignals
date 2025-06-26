import pandas as pd
import neurokit2 as nk
import matplotlib.pyplot as plt

file_path = "segmented_data/ECG/cVemp/P2.csv"
df = pd.read_csv(file_path)

ecg_signal = df["ECG"]  
sampling_rate = 1000

cleaned_ecg = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)

signals, info = nk.ecg_process(ecg_signal, sampling_rate=sampling_rate)

fig_data = nk.ecg_plot(signals, info)

fig = plt.gcf() 
fig.set_size_inches(10, 12, forward=True) 

peaks, info = nk.ecg_peaks(cleaned_ecg, sampling_rate=1000, correct_artifacts=True)
hrv_indices = nk.hrv(peaks, sampling_rate=1000, show=True)
plt.show()
