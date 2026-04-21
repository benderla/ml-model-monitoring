# ML Model Monitoring

This project defines how machine learning models are monitored after deployment, including drift detection, performance degradation, and operational response.

This project focuses on operational ownership of ML systems after deployment, not just model performance.

---

## What This Covers

- data drift detection
- model performance monitoring
- alerting thresholds
- incident response workflow

---

## Monitoring Framework

### 1. Data Monitoring

Track:
- feature distributions
- missing values
- input ranges

Goal:
- detect shifts in incoming data vs training data

---

## How Monitoring Decisions Are Made

Monitoring thresholds are not fixed and depend on system tolerance.

Examples:
- high-risk systems → prioritize recall (detect more issues)
- cost-sensitive systems → prioritize precision (reduce false alerts)

Tradeoffs:
- lower thresholds → more alerts, higher detection
- higher thresholds → fewer alerts, higher risk of missed issues

Final thresholds should be set based on:
- business impact
- acceptable false positive rate
- response capability of the team

---

### 2. Model Performance Monitoring

Track:
- precision / recall (if labels available)
- proxy metrics (if labels delayed)
- prediction distributions

Goal:
- detect degradation in model behavior

---

### 3. Drift Detection

Types:
- data drift
- concept drift

Approach:
- statistical comparison of distributions
- threshold-based alerts

---

### 4. Alerting

Trigger alerts when:
- feature distributions shift beyond threshold
- prediction distribution changes significantly
- performance drops below acceptable range

---

## Incident Response

When an alert is triggered:

1. Validate the signal
   - confirm data issue vs noise
2. Identify scope
   - which features or predictions are affected
3. Assess impact
   - user-facing impact vs internal issue
4. Take action
   - retrain model
   - adjust thresholds
   - rollback to previous model
5. Monitor recovery
   - ensure metrics return to baseline

Goal:
- reduce time from detection to resolution

---

## Handling Delayed Labels

In many systems, ground truth labels are not immediately available.

Approach:
- monitor proxy metrics (prediction distributions, input drift)
- use delayed evaluation once labels arrive
- compare short-term vs long-term performance

Impact:
- monitoring must rely on indirect signals initially
- full performance validation happens later

---

## Example Monitoring Pipeline

1. collect incoming prediction data  
2. log features and predictions  
3. compare against baseline distributions  
4. compute monitoring metrics  
5. trigger alerts if thresholds exceeded  
6. log incidents and initiate response  

Goal:
- continuous visibility into model behavior after deployment 

---

## What This Does NOT Include

- full production monitoring system
- real-time streaming pipeline
- automated retraining pipeline

---

## Interview Questions This Project Supports

- How do you monitor a model after deployment?
- What is data drift vs concept drift?
- What metrics would you track?
- How do you handle delayed labels?
- What happens when the model degrades?

---

## Example: Drift Detection Implementation

A simple example is included in:

- `src/drift_check.py`

This script:
- compares baseline vs current data
- calculates mean difference
- triggers an alert when threshold is exceeded

Example output:
- "ALERT: Potential data drift detected"

This demonstrates how monitoring logic can be implemented before integrating into a larger system.

---

This project demonstrates how monitoring enables reliable ML systems by connecting model behavior to operational decisions.