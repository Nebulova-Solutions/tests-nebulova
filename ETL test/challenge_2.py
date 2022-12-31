import pandas as pd
import numpy as np

data = [
    {"timestamp": 0, "variable": "var1", "value": 0},
    {"timestamp": 5, "variable": "var2", "value": 0},
    {"timestamp": 9, "variable": "var1", "value": 1},
    {"timestamp": 11, "variable": "var2", "value": 1},
    {"timestamp": 12, "variable": "var1", "value": 0},
    {"timestamp": 13, "variable": "var2", "value": 0},
    {"timestamp": 15, "variable": "var1", "value": 1},
    {"timestamp": 17, "variable": "var2", "value": 1},
    {"timestamp": 19, "variable": "var1", "value": 0},
    {"timestamp": 20, "variable": "var1", "value": 0},
]

df = pd.DataFrame(data=data)

# TODO your implementation
transformed_df = pd.DataFrame()
# end of your implementation

# Expected output
expected_df = pd.DataFrame(
    [
        {"timestamp": 0, "var1": 0.0, "var2": np.nan},
        {"timestamp": 1, "var1": 0.0, "var2": np.nan},
        {"timestamp": 2, "var1": 0.0, "var2": np.nan},
        {"timestamp": 3, "var1": 0.0, "var2": np.nan},
        {"timestamp": 4, "var1": 0.0, "var2": np.nan},
        {"timestamp": 5, "var1": 0.0, "var2": 0.0},
        {"timestamp": 6, "var1": 0.0, "var2": 0.0},
        {"timestamp": 7, "var1": 0.0, "var2": 0.0},
        {"timestamp": 8, "var1": 0.0, "var2": 0.0},
        {"timestamp": 9, "var1": 1.0, "var2": 0.0},
        {"timestamp": 10, "var1": 1.0, "var2": 0.0},
        {"timestamp": 11, "var1": 1.0, "var2": 1.0},
        {"timestamp": 12, "var1": 0.0, "var2": 1.0},
        {"timestamp": 13, "var1": 0.0, "var2": 0.0},
        {"timestamp": 14, "var1": 0.0, "var2": 0.0},
        {"timestamp": 15, "var1": 1.0, "var2": 0.0},
        {"timestamp": 16, "var1": 1.0, "var2": 0.0},
        {"timestamp": 17, "var1": 1.0, "var2": 1.0},
        {"timestamp": 18, "var1": 1.0, "var2": 1.0},
        {"timestamp": 19, "var1": 0.0, "var2": 1.0},
        {"timestamp": 20, "var1": 0.0, "var2": 1.0},
    ]
)
pd.testing.assert_frame_equal(
    transformed_df, expected_df
)  # This should not trigger any error