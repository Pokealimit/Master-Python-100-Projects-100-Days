import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(squirrel_data.columns)
fur_count = squirrel_data['Primary Fur Color'].value_counts().rename_axis('Fur Color').reset_index(name='Counts')
print(fur_count)

fur_count.to_csv("squirrel_count.csv")




