import pandas as pd
import os
from datetime import datetime
from config.config import input_path


def get_files():
    """
    Retrieves and processes Excel files from a specified input directory, extracting
    the "SubSector Analysis" sheet from each file, and merging them into a single
    DataFrame with an additional "Date" column.

    The function assumes that the Excel files in the input directory have names ending
    with a date in the format "DD_MM_YYYY". The "Date" column is populated with this
    date extracted from the file name.

    Returns:
        pandas.DataFrame: A DataFrame containing the merged data from all processed
        Excel files, sorted by the "Date" column in ascending order.
    """
    files = os.listdir(input_path)
    files_db = []

    for file in files:
        full_pth = os.path.join(input_path, file)
        excel_file = pd.ExcelFile(full_pth)
        sheet_names = excel_file.sheet_names

        files_db.append({"name": file, "path": full_pth, "sheets": sheet_names})

    price_filter_dfs = []

    for item in files_db:
        str_dt = item.get("name").split(".")[0][-10:]
        file_date = datetime.strptime(str_dt, "%d_%m_%Y").date()
        df = pd.read_excel(item.get("path"), sheet_name="SubSector Analysis")
        df.insert(0, "Date", file_date)
        price_filter_dfs.append(df)

    merged_df = pd.concat(price_filter_dfs, ignore_index=True)
    merged_df = merged_df.sort_values(by=["Date"], ascending=True)

    return merged_df
