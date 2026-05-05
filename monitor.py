import argparse
import pandas as pd
from scipy.stats import ks_2samp


def check_drift(baseline_path, new_path, mean_threshold=0.05, p_value_threshold=0.05):
    baseline = pd.read_csv(baseline_path)["prediction"]
    new = pd.read_csv(new_path)["prediction"]

    baseline_mean = baseline.mean()
    new_mean = new.mean()

    baseline_std = baseline.std()
    new_std = new.std()

    mean_shift = new_mean - baseline_mean
    std_shift = new_std - baseline_std

    ks_statistic, p_value = ks_2samp(baseline, new)

    mean_drift = abs(mean_shift) > mean_threshold
    ks_drift = p_value < p_value_threshold
    drift_detected = mean_drift or ks_drift

    print("Drift Check Results:")
    print(f"- Baseline Mean: {baseline_mean:.2f}")
    print(f"- New Mean: {new_mean:.2f}")
    print(f"- Mean Shift: {mean_shift:.2f}")
    print(f"- Std Shift: {std_shift:.2f}")
    print(f"- KS Statistic: {ks_statistic:.4f}")
    print(f"- KS p-value: {p_value:.6f}")
    print(f"- Mean Drift Detected: {'YES' if mean_drift else 'NO'}")
    print(f"- KS Drift Detected: {'YES' if ks_drift else 'NO'}")
    print(f"- Drift Detected: {'YES' if drift_detected else 'NO'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    check_drift(args.baseline, args.input)