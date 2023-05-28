import pandas as pd


def group_by_ikid(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby(["date", "lkid"]).aggregate(
        {
            "date": "first",
            "lkid": "first",
            "sector": "first",
            "analyst": "first",
            "pal": "sum",
            "exposure": "sum",
        }
    )


def update_sector_column(df: pd.DataFrame) -> pd.DataFrame:
    df["sector"] = df["sector"].apply(
        lambda x: "Information Technology" if x == "Technology" else x
    )
    return df


def add_daily_return_column(df: pd.DataFrame) -> pd.DataFrame:
    daily_return_df = df.set_index("date")
    first_day_date = df["date"].min()
    beginning_of_day_capital_df = (
        df.reset_index(drop=True)
        .groupby("date")
        .aggregate({"exposure": "sum", "pal": "sum"})
    )
    first_day_capital = (
        beginning_of_day_capital_df.at[first_day_date, "exposure"]
        - beginning_of_day_capital_df.at[first_day_date, "pal"]
    )
    beginning_of_day_capital_df = beginning_of_day_capital_df.shift(1)
    beginning_of_day_capital_df.at[first_day_date, "exposure"] = first_day_capital
    daily_return_df["daily_return"] = (
        daily_return_df["pal"] / beginning_of_day_capital_df["exposure"]
    )
    return daily_return_df
