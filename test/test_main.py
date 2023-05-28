import pytest

from src import main
from src.persistence import get_data_input
from src.transforms import group_by_ikid, update_sector_column, add_daily_return_column
import pandas as pd

"""
["date", "lkid", "ticker", "name", "analyst", "sector", "pal", "exposure"]
"""


@pytest.fixture()
def one_day_test_df():
    return get_data_input("one_day_test_input.csv")


@pytest.fixture()
def daily_return_test_df():
    return get_data_input("daily_return_test_input.csv")


def test_aggregation(one_day_test_df):
    output = group_by_ikid(one_day_test_df)
    assert output.iloc[0].analyst == "Alice"
    assert output.iloc[0].sector == "Bintech"
    assert output.iloc[0].pal == 0
    assert output.iloc[0].exposure == 0


def test_update_sector_column(one_day_test_df):
    def assert_it(x):
        if "Technology" in x:
            assert x == "Information Technology"

    with pytest.raises(AssertionError):
        one_day_test_df["sector"].apply(assert_it)
    output = update_sector_column(one_day_test_df)
    output["sector"].apply(assert_it)


def test_daily_return(daily_return_test_df):
    output = add_daily_return_column(group_by_ikid(daily_return_test_df))
    expected_returns = pd.Series([0.1, -0.09091, 0.2, -(12.0 - 10.0) / 12.0], name="daily_return")
    pd.testing.assert_series_equal(output["daily_return"].reset_index(drop=True), expected_returns)


def test_main():
    main.main("practical.csv", "blotter-new.csv")
