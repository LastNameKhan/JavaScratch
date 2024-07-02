# Below is one of the method to print the data in the form of a table and manipulate the data
# with open("weather_data.csv.csv") as mydata:
#     # Below readLines will give us the data in the form of a list
#     data = mydata.readlines()
#     print(data)


# Here we can use csv the python inbuilt library to print the data in the form of a table
# and manipulate accordingly
# import csv
#
# with open("weather_data.csv.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)


# The most strong and proficient form of the library to manipulate the data is Pandas and used
# widely in working with different sorts of data
# Pandas Data Analysis library called Pandas

import pandas

file_data = pandas.read_csv("weather_data.csv.csv")
# To print the data inside the the row temp which detects automatically according to the row name
print(file_data["temp"])
