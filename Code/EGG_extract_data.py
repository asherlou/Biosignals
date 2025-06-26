
import os
import pandas as pd
import neurokit2 as nk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

base_path = "segmented_data/EGG"
states = ["cVemp", "Resting_1", "Resting_2"]
sampling_rate = 1000

for state in states:

    results = []
    state_path = os.path.join(base_path, state)
    files = [f for f in os.listdir(state_path) if f.endswith('.csv')]

    for file in files:
        file_path = os.path.join(state_path, file)
        
        df = pd.read_csv(file_path)
        
        if "EGG" not in df.columns:
            print(f"Skipping {file} as it does not contain 'EGG' column.")
            continue

        egg_signal = df["EGG"]
        n = len(egg_signal)  
        frequencies = np.fft.rfftfreq(n, d=1/sampling_rate)  
        fft_values = np.fft.rfft(egg_signal)  
        fft_magnitude = np.abs(fft_values)  

        dominant_peak_idx, _ = find_peaks(fft_magnitude)
        dominant_frequency = frequencies[dominant_peak_idx[np.argmax(fft_magnitude[dominant_peak_idx])]]  
        results.append({
            "State": state,
            "Participant": file.split(".")[0],
            "EGG_Dominant_Freq": dominant_frequency
        })

    results_df = pd.DataFrame(results)
    output_path = os.path.join(state_path, "egg_analysis_results.csv")
    results_df.to_csv(output_path, index=False)

    print(f"Results saved to {output_path}")


