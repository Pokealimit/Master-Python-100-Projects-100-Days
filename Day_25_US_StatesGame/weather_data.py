import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)

#     # Storing of temperature from weather_data
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# Finding Average Temperature
temperatures = data['temp'].to_list()

avg_temp = sum(temperatures) / len(temperatures)
print(avg_temp)

print(f"Average temperature: {data['temp'].mean()}")
print(f"Max tempature: {data['temp'].max()}")

# Get Conditions
print(data['condition'])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
# Get Row with max temperature
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 1.8 + 32
print(monday_temp_F)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")