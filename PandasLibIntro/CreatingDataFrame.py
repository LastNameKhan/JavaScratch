import pandas

data = pandas.read_csv("weather_data.csv.csv")
print(data)

# Creating the DataFrame from Scratch

data_dict = {
    "students": ["Amy", "James", "Aman"],
    "Scores" : [76, 56, 65]
}

created_data = pandas.DataFrame(data_dict)
created_data.to_csv("Created_data.csv")
print(created_data)