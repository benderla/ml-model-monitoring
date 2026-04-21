# Drift Detection Example

Scenario:
- model trained on baseline data
- incoming data distribution shifts

Example:
- feature: packet_rate
- baseline mean: 50
- current mean: 80

Detection:
- statistical test shows significant shift

Action:
- trigger alert
- investigate data source
- evaluate model performance impact