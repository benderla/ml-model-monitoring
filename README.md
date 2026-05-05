# ML Model Monitoring — Drift Detection System

This project implements a lightweight monitoring system for machine learning models to detect data drift, prediction shifts, and performance degradation over time.

It demonstrates how to compare baseline and new model predictions using both heuristic thresholds and statistical tests.

---

## Why This Matters

* ML models degrade over time as data distributions shift
* Performance metrics alone are not enough — underlying data can drift silently
* Without monitoring, models can fail without obvious signals

This project shows how to detect those failures using simple, practical techniques.

---

## What This System Does

* Compares baseline vs new prediction distributions
* Detects shifts in model output behavior
* Calculates statistical differences (mean, standard deviation)
* Applies the Kolmogorov-Smirnov (KS) test for distribution comparison
* Flags drift conditions based on both threshold and statistical signals

---

## System Overview

Baseline Predictions
→ New Predictions
→ Distribution Comparison
→ Drift Detection
→ Alert Signal

---

## Example Workflow

### Run monitoring check

```bash
python monitor.py \
  --baseline examples/predictions_v1.csv \
  --input examples/predictions_v2.csv
```

---

## Drift Detection Example

Example run comparing baseline vs new predictions:

```bash
python monitor.py \
  --baseline examples/predictions_v1.csv \
  --input examples/predictions_v2.csv
```

Output:

```text
Drift Check Results:
- Baseline Mean: 0.29
- New Mean: 0.71
- Mean Shift: 0.43
- Std Shift: -0.00
- KS Statistic: 0.7970
- KS p-value: 0.000000
- Mean Drift Detected: YES
- KS Drift Detected: YES
- Drift Detected: YES
```

---

## Interpretation

* Large mean shift (0.43) indicates a major change in prediction behavior
* KS test confirms distributions are statistically different (p < 0.05)
* Combined signals reduce false positives and improve confidence in drift detection

This approach reflects real-world monitoring systems that use both heuristic thresholds and statistical validation.

---

## How It Works

* Establishes a baseline distribution from historical predictions
* Compares new prediction data against baseline
* Measures statistical differences (mean and variance)
* Applies KS test to detect distribution-level changes
* Flags drift when either threshold or statistical conditions are met

---

## What This Project Demonstrates

* Practical ML monitoring without heavy infrastructure
* Detection of model behavior changes after deployment
* Use of statistical methods (KS test) for validation
* Foundation for alerting and retraining workflows

---

## Limitations

* Uses simple statistical checks (not full monitoring pipeline)
* No real-time or streaming integration
* No automated alerting or retraining loop

---

## Next Steps

* Add time-based monitoring (batch or streaming data)
* Integrate alerting (logs, notifications)
* Store historical metrics for trend analysis
* Trigger automated retraining based on drift signals

---

## Repository Structure

* `monitor.py` → core drift detection logic
* `examples/` → sample prediction datasets
* `notebooks/` → analysis and experimentation
* `metrics/` → evaluation outputs (if applicable)

---

## Tech Stack

* Python (pandas, numpy)
* SciPy (KS statistical test)

---

## Requirements

```bash
pip install -r requirements.txt
```

---

## Key Takeaway

This project demonstrates how to move beyond model deployment and implement monitoring that detects when models begin to fail in production environments.

---

## Monitoring Workflow

Baseline → New Data → Drift Detection → Alert → Investigation → Retraining

---

## What Happens After Drift Detection

* Drift event is logged
* System triggers alert for investigation
* Root cause analysis performed (data vs model issue)
* Model retrained or threshold adjusted
* Updated model redeployed

---

## Example Monitoring Lifecycle

1. Model deployed
2. Predictions collected daily
3. Drift check runs automatically
4. Drift detected via KS test
5. Alert generated
6. Model reviewed and updated

This mirrors real-world ML operations where monitoring feeds directly into model lifecycle management.
