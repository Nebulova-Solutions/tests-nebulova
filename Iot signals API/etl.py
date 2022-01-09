import pandas as pd
from datetime import datetime


def etl_proccess(start: datetime, end: datetime) -> dict:
    data = pd.read_csv("./data.csv")
    # TODO: your implementation


def test_etl() -> None:
    test_case = {
        2: {
            "RD_VAR0": {"dates": ["2021-11"], "data": [1339]},
            "RD_VAR1": {"dates": ["2021-11"], "data": [0]},
            "RD_VAR2": {"dates": ["2021-11"], "data": [0]},
            "RD_VAR3": {"dates": ["2021-11"], "data": [2751]},
        }
    }
    assert etl_proccess(datetime(2021, 10, 1), datetime(2021, 11, 30)) == test_case


if __name__ == "__main__":
    # Run test_etl
    test_etl()
