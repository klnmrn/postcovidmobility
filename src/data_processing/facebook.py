import os
import pandas as pd


# Read and process Facebook data
def read_facebook_data(script_dir):
    fb_data_dir = os.path.abspath(os.path.join(script_dir, "data", "processed", "Facebook"))
    fb_dataset_path = os.path.join(fb_data_dir, "Facebook_MD_Piedmont.csv")
    fb_data = pd.read_csv(fb_dataset_path)
    fb_data.drop(
        [
            "Unnamed: 0",
            "country",
            "polygon_source",
            "polygon_name",
            "polygon_id",
            "all_day_ratio_single_tile_users",
            "baseline_name",
            "baseline_type",
        ],
        axis=1,
        inplace=True,
    )
    fb_data.rename(
        columns={
            "ds": "date",
            "all_day_bing_tiles_visited_relative_change": "Facebook_movement_change",
        },
        inplace=True,
    )
    fb_data["date"] = pd.to_datetime(fb_data["date"], dayfirst=False, format="%Y-%m-%d")
    fb_data.iloc[0:, 1] = fb_data.iloc[0:, 1] * 100
    fb_data.drop(fb_data.tail(4).index, inplace=True)
    fb_data["Facebook_movement_change_rolling"] = (
        fb_data["Facebook_movement_change"].rolling(7).mean()
    )
    return fb_data
