import pandas as pd
import neurokit2 as nk
import matplotlib.pyplot as plt
from neurokit2 import eda_sympathetic


file_path = "segmented_data/EDA/cVemp/P2.csv"
df = pd.read_csv(file_path)

eda_signal = df["EDA"]  
sampling_rate = 1000

Cleaned_eda = nk.eda_clean(eda_signal, sampling_rate=sampling_rate)

signals, info = nk.eda_process(eda_signal, sampling_rate=sampling_rate)

eda_analysis = nk.eda_intervalrelated(signals, sampling_rate=sampling_rate)
print(eda_analysis)

symp_AUC = nk.eda_sympathetic(eda_signal, sampling_rate=sampling_rate, method='posada', show=True)
#print(symp_AUC)



# fig_data = nk.eda_plot(signals, info, static=True)
fig = plt.gcf() 
fig.set_size_inches(10, 12, forward=True) 
plt.show()  

