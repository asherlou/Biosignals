import os
import pandas as pd
import neurokit2 as nk

base_path = "segmented_data/RESPIRATION"
states = ["cVemp", "Resting_1", "Resting_2"]
sampling_rate = 1000

for state in states:

    results = []
    state_path = os.path.join(base_path, state)
    files = [f for f in os.listdir(state_path) if f.endswith('.csv')]

    for file in files:
        file_path = os.path.join(state_path, file)
        
        df = pd.read_csv(file_path)
        
        if "RESPIRATION" not in df.columns:
            print(f"Skipping {file} as it does not contain 'RESPIRATION' column.")
            continue

        rsp_signal = df["RESPIRATION"]

        try:
            cleaned_rsp = nk.rsp_clean(rsp_signal, sampling_rate=sampling_rate)
            signals, info = nk.rsp_process(cleaned_rsp, sampling_rate=sampling_rate)
            analyzed_signal = nk.rsp_analyze(signals, sampling_rate=sampling_rate)

            rsp_rate_mean = analyzed_signal["RSP_Rate_Mean"][0]  # Mean respiration rate
            rsp_rvt = analyzed_signal["RSP_RVT"][0]  # Respiration volume per time
            rrv_meanbb = analyzed_signal['RRV_MeanBB'][0]  # Mean breath-to-breath interval
            rrv_sd = analyzed_signal['RRV_SD1'][0]  # Respiratory variability

        except Exception as e:
            print(f"Error processing {file}: {e}")

        results.append({
            "State": state,
            "Participant": file.split(".")[0],
            "BreathRate_Mean": rsp_rate_mean,
            "RVT": rsp_rvt,
            "RRV_MeanBB": rrv_meanbb,
            "RRV_SD": rrv_sd
        })

    results_df = pd.DataFrame(results)
    output_path = os.path.join(state_path, "rsp_analysis_results.csv")
    results_df.to_csv(output_path, index=False)

    print(f"Results saved to {output_path}")


