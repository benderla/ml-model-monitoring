import pandas as pd
import numpy as np

# set seed for reproducibility
np.random.seed(42)

# simulate 1000 prediction scores (0 to 1)
predictions = np.random.beta(a=5, b=2, size=1000)

df = pd.DataFrame({
    "prediction": predictions
})

df.to_csv("examples/predictions_v2.csv", index=False)

print("File created: examples/predictions_v2.csv")