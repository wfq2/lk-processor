import os.path

import pandas as pd

data_columns = [
    "date",
    "lkid",
    "ticker",
    "name",
    "analyst",
    "sector",
    "pal",
    "exposure",
]


def root_directory():
    base_dir_name = "lk-processor"
    cwd = os.getcwd()
    return cwd.split(base_dir_name)[0] + base_dir_name


def convert_date(date_string: str):
    # Some bad Data Parsing Right Here - fixes poorly formatted dates
    if date_string[:4] != "2018":
        date_string = date_string[4:] + date_string[:4]
    return pd.to_datetime(date_string)


def get_data_input(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(
        f"{root_directory()}/input_files/{csv_path}",
        header=0,
        names=data_columns,
        converters={"date": convert_date},
    )


def write_data_output(df: pd.DataFrame, csv_path: str) -> None:
    df.to_csv(f"{root_directory()}/output_files/{csv_path}")
