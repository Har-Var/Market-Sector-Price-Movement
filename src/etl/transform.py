def split_subsectors(merged_df):
    """
    Splits the merged data DataFrame into a list of dictionaries, each
    containing a sub-sector name and the corresponding DataFrame filtered
    by that sub-sector.

    The percentages are also multiplied by 100 and rounded to 4 decimal
    places.

    Args:
        merged_df (pandas.DataFrame): DataFrame containing the merged data

    Returns:
        list: A list of dictionaries, each containing a sub-sector name and
        the corresponding DataFrame filtered by that sub-sector
    """
    column_names = merged_df.columns
    perc_cols = column_names[3:]
    for col in perc_cols:
        merged_df[col] = merged_df[col].apply(lambda x: round(x, 4))

    subsec_list = merged_df["Sub-Sector"].unique()
    subsec_dfs = []

    for subsec in subsec_list:
        subsec_dfs.append(
            {
                "sub_sector": subsec,
                "ss_df": merged_df[merged_df["Sub-Sector"] == subsec].reset_index(
                    drop=True
                ),
            }
        )
    return subsec_dfs
