import pandas as pd
import neurokit2 as nk
import matplotlib.pyplot as plt

file_path = "segmented_data/RESPIRATION/Resting_1/P2.csv"
df = pd.read_csv(file_path)

rsp_signal = df["RESPIRATION"]  
sampling_rate = 1000

cleaned_rsp = nk.rsp_clean(rsp_signal, sampling_rate=sampling_rate)

signals, info = nk.rsp_process(rsp_signal, sampling_rate=sampling_rate)

fig_data = nk.rsp_plot(signals, info, static=True)
fig = plt.gcf() 
fig.set_size_inches(10, 12, forward=True) 

rspData = nk.rsp_intervalrelated(signals, sampling_rate=sampling_rate)


#plt.show()
print(rspData)