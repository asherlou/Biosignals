import pandas as pd
import neurokit2 as nk
import matplotlib.pyplot as plt

file_path = "segmented_data/EDA/cVemp/P2.csv"
df = pd.read_csv(file_path)

eda_signal = df["EDA"]  
sampling_rate = 1000

cleaned_eda = nk.eda_clean(eda_signal, sampling_rate=sampling_rate)

signals, info = nk.eda_process(eda_signal, sampling_rate=sampling_rate)


import os
import pandas as pd
import neurokit2 as nk
import numpy as np

base_path = "segmented_data/EDA"
states = ["cVemp", "Resting_1", "Resting_2"]
sampling_rate = 1000

for state in states:

    results = []
    state_path = os.path.join(base_path, state)
    files = [f for f in os.listdir(state_path) if f.endswith('.csv')]

    for file in files:
        file_path = os.path.join(state_path, file)
        
        df = pd.read_csv(file_path)
        
        if "EDA" not in df.columns:
            print(f"Skipping {file} as it does not contain 'EDA' column.")
            continue

        eda_signal = df["EDA"]

        try:
            cleaned_ecg = nk.eda_clean(eda_signal, sampling_rate=sampling_rate)
            signals, info = nk.eda_process(cleaned_ecg, sampling_rate=sampling_rate)
            analyzed_signal = nk.eda_intervalrelated(signals, sampling_rate=sampling_rate)

            scr_peaks_n = analyzed_signal["SCR_Peaks_N"][0]
            scr_peaks_amplitude_mean = analyzed_signal["SCR_Peaks_Amplitude_Mean"][0]
            eda_tonic_sd = analyzed_signal["EDA_Tonic_SD"][0]
            eda_tonic_mean = np.mean(signals["EDA_Tonic"])
            eda_sympathetic = analyzed_signal["EDA_Sympathetic"][0]
            eda_sympatheticn = analyzed_signal["EDA_SympatheticN"][0]
            eda_autocorrelation = analyzed_signal["EDA_Autocorrelation"][0]
            

        except Exception as e:
            print(f"Error processing {file}: {e}")

        results.append({
            "State": state,
            "Participant": file.split(".")[0],
            "SCR_Peaks_N": scr_peaks_n,
            "SCR_Peaks_Amplitude_Mean": scr_peaks_amplitude_mean,
            "EDA_Tonic_SD": eda_tonic_sd,
            "EDA_Tonic": eda_tonic_mean,
            "EDA_Sympathetic": eda_sympathetic,
            "EDA_SympatheticN": eda_sympatheticn,
            "EDA_Autocorrelation": eda_autocorrelation
        })

    results_df = pd.DataFrame(results)
    output_path = os.path.join(state_path, "eda_analysis_results.csv")
    results_df.to_csv(output_path, index=False)

    print(f"Results saved to {output_path}")


