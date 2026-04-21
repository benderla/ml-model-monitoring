# drift_check.py

# Simple drift detection example
# Compares baseline data vs current data using mean difference

baseline_data = [45, 50, 52, 48, 49]
current_data = [70, 75, 80, 78, 72]

def calculate_mean(data):
    return sum(data) / len(data)

baseline_mean = calculate_mean(baseline_data)
current_mean = calculate_mean(current_data)

print(f"Baseline mean: {baseline_mean}")
print(f"Current mean: {current_mean}")

# simple threshold check
threshold = 10

if abs(current_mean - baseline_mean) > threshold:
    print("ALERT: Potential data drift detected")
else:
    print("No significant drift detected")