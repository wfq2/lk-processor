import pytest

from src import main
from src.persistence import get_data_input
from src.transforms import group_by_ikid, update_sector_column, add_daily_return_column

"""
["date", "lkid", "ticker", "name", "analyst", "sector", "pal", "exposure"]
"""


@pytest.fixture()
def one_day_test_df():
    return get_data_input("one_day_test_input.csv")


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


def test_add_pal_column(one_day_test_df):
    input_df = get_data_input("practical.csv")
    output = group_by_ikid(input_df)
    add_daily_return_column(output)


def test_main():
    main.main("practical.csv")
