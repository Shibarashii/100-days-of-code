from pathlib import Path
import pandas as pd

root = Path(__file__).parent

data = pd.read_csv(root / "weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp = data["temp"]
temp_list = data["temp"].to_list()
print(temp_list)
print(f"Average Temperature: {temp.mean():.2f}")
print(f"Maximum Temperature: {temp.max()}")


# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in rows
print(data[data["day"] == "Monday"])
print(data[data.day == "Monday"])

# Get max temperature row
print(data[data["temp"] == data["temp"].max()])
print(data[data.temp == data.temp.max()])

# Get data in row
monday = data[data.day == "Monday"]
monday_temp = monday["temp"][0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday["condition"])
print(monday_temp_F)

# Create a datafram from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv(root/"new_data.csv")
