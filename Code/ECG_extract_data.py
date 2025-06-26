import os
import pandas as pd
import neurokit2 as nk

base_path = "segmented_data/ECG"
states = ["cVemp", "Resting_1", "Resting_2"]
sampling_rate = 1000

for state in states:

    results = []
    state_path = os.path.join(base_path, state)
    files = [f for f in os.listdir(state_path) if f.endswith('.csv')]

    for file in files:
        file_path = os.path.join(state_path, file)
        
        df = pd.read_csv(file_path)
        
        if "ECG" not in df.columns:
            print(f"Skipping {file} as it does not contain 'ECG' column.")
            continue

        ecg_signal = df["ECG"]

        try:
            cleaned_ecg = nk.ecg_clean(ecg_signal, sampling_rate=sampling_rate)
            signals, info = nk.ecg_process(cleaned_ecg, sampling_rate=sampling_rate)
            analyzed_signal = nk.ecg_analyze(signals, sampling_rate=sampling_rate)

            heart_rate_mean = analyzed_signal["ECG_Rate_Mean"][0]  
            hrv_sd = analyzed_signal['HRV_SDNN'][0][0][0]

        except Exception as e:
            print(f"Error processing {file}: {e}")

        results.append({
            "State": state,
            "Participant": file.split(".")[0],
            "HeartRate_Mean": heart_rate_mean,
            "HRV_Sd": hrv_sd
        })

    results_df = pd.DataFrame(results)
    output_path = os.path.join(state_path, "ecg_analysis_results.csv")
    results_df.to_csv(output_path, index=False)

    print(f"Results saved to {output_path}")


