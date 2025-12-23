import pandas as pd
from pathlib import Path

root = Path(__file__).parent
file_path = root / "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

df = pd.read_csv(file_path)
fur_color_column = df["Primary Fur Color"]

unique_colors_list = fur_color_column.dropna().unique()
count_list = []
for color in unique_colors_list:
    color_count = len(fur_color_column[fur_color_column == color])
    count_list.append(color_count)

data_dict = {
    "color": unique_colors_list,
    "count": count_list
}

new_df = pd.DataFrame(data_dict)
new_df.to_csv(root/"color_count.csv")
