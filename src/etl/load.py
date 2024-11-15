import pandas as pd
import os
from config.config import report_path, viz_data_path


def export_tableau_data(merged_df):
    """
    Exports the merged data DataFrame to a CSV file at the designated path,
    overwriting any existing file.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing the merged data
    """
    if os.path.exists(viz_data_path):
        os.remove(viz_data_path)
    else:
        pass
    merged_df.to_csv(
        viz_data_path, float_format="{:.6f}".format, encoding="utf-8", index=False
    )


def export_report(subsec_dfs):
    """
    Exports the list of dictionaries containing sub-sector DataFrames to a single
    Excel file at the designated path, overwriting any existing file.

    The function takes a list of dictionaries, each containing a sub-sector name and
    the corresponding DataFrame filtered by that sub-sector. It then loops through
    the list, and writes each DataFrame to a separate sheet in the Excel file.

    Args:
        subsec_dfs (list): A list of dictionaries, each containing a sub-sector name
        and the corresponding DataFrame filtered by that sub-sector
    """
    if os.path.exists(report_path):
        os.remove(report_path)
    else:
        pass

    writer = pd.ExcelWriter(report_path)

    # Loop through the data and write each DataFrame to the respective sheet
    for item in subsec_dfs:
        sheet_name = item.get("sub_sector").strip()[:31]
        df = item.get("ss_df")
        df.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.close()
