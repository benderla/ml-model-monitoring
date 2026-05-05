import pandas as pd
import argparse

def check_drift(baseline_path, new_path):
    base = pd.read_csv(baseline_path)['prediction']
    new = pd.read_csv(new_path)['prediction']

    base_mean = base.mean()
    new_mean = new.mean()

    base_std = base.std()
    new_std = new.std()

    mean_shift = new_mean - base_mean
    std_shift = new_std - base_std

    print("Drift Check Results:")
    print(f"- Baseline Mean: {base_mean:.2f}")
    print(f"- New Mean: {new_mean:.2f}")
    print(f"- Mean Shift: {mean_shift:.2f}")
    print(f"- Std Shift: {std_shift:.2f}")

    if abs(mean_shift) > 0.05:
        print("- Drift Detected: YES")
    else:
        print("- Drift Detected: NO")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    check_drift(args.baseline, args.input)