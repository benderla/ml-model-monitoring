## Why ML Monitoring Matters

Machine learning models often degrade in production due to:

• changes in incoming data distributions  
• evolving user behavior  
• upstream pipeline changes  
• model concept drift

Without monitoring, models can silently fail while still producing predictions.

This project demonstrates how production ML systems detect and respond to these issues.

## Monitoring Signals

The system tracks three categories of signals:

### Data Quality
• missing values
• feature distribution changes

### Data Drift
• statistical divergence between training and production data

### Model Performance
• anomaly rate trends
• prediction confidence

## Sample Code
from scipy.stats import ks_2samp

def detect_feature_drift(train_feature, prod_feature):
    stat, p_value = ks_2samp(train_feature, prod_feature)
    return p_value

The Kolmogorov–Smirnov test compares two distributions and detects statistically significant drift.

## Alerting Strategy

Alerts are triggered when:

• p-value < 0.05 for any monitored feature  
• anomaly rate changes by more than 5%  
• prediction latency exceeds threshold

These alerts signal that the model may require retraining or investigation.

## Investigation Workflow

When monitoring alerts trigger:

1. Confirm the alert is not caused by upstream pipeline changes.
2. Compare feature distributions against training data.
3. Evaluate model performance on labeled validation samples.
4. Decide whether retraining is required.

## Limitations

This repository demonstrates monitoring concepts using a simplified dataset.

Real systems would require:

• larger production datasets
• automated monitoring pipelines
• integrated alerting infrastructure