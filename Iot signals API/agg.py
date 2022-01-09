import pandas as pd
import numpy as np

SIZE = 100000000
data = pd.DataFrame(
    {
        "class": np.random.randint(1, 5, SIZE),
        "var1": np.random.randn(SIZE),
        "var2": np.random.randn(SIZE),
    }
)

# TODO Make the following code faster as posible
aggregated = list()
for c in data["class"].unique():
    filter_condition = data["class"] == c

    # Get maximum of var1 per class
    maximum = -float("inf")
    for i in data.loc[filter_condition, "var1"]:
        if i > maximum:
            maximum = i

    # Get average of var2 per class
    average = 0
    for i in data.loc[filter_condition, "var2"]:
        average += i
    average /= data.loc[filter_condition, "var2"].shape[0]

    aggregated.append({"class": c, "var1": maximum, "var2": average})

aggregated = pd.DataFrame(aggregated)
