import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240702.csv")

grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

grey_count = len(grey_squirrels)
red_count = len(red_squirrels)
black_count = len(black_squirrels)

create_csv = {
    "Fur Color": ["Gray", "Cinnamon","Black"],
    "Count": [grey_count, red_count, black_count]
}

created_data = pandas.DataFrame(create_csv)
created_data.to_csv("Squirrel_Count.csv")
print(created_data)


