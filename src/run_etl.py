from etl import get_files, split_subsectors, export_tableau_data, export_report


def run_etl():
    """
    Executes the ETL (Extract, Transform, Load) process for processing Excel files.

    This function orchestrates the entire ETL pipeline by performing the following steps:
    1. Extracts and merges data from Excel files using the `get_files` function.
    2. Exports the merged data to a CSV file for Tableau using the `export_tableau_data` function.
    3. Splits the merged data into sub-sector specific DataFrames using the `split_subsectors` function.
    4. Exports the sub-sector DataFrames to an Excel report using the `export_report` function.
    """
    merged_df = get_files()
    subsec_dfs = split_subsectors(merged_df)
    export_tableau_data(merged_df)
    export_report(subsec_dfs)


if __name__ == "__main__":
    run_etl()
