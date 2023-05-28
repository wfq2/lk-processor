import sys

from src.persistence import get_data_input, write_data_output
from src.transforms import group_by_ikid, update_sector_column, add_daily_return_column


def main(csv_input_path: str, csv_output_path: str):
    dataframe = get_data_input(csv_input_path)
    transforms = [group_by_ikid, update_sector_column, add_daily_return_column]
    for transform in transforms:
        dataframe = transform(dataframe)
    write_data_output(dataframe, csv_output_path)


if __name__ == "__main__":
    input_path, output_path = sys.argv[1], sys.argv[2]
    main(input_path, output_path)
