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
# There are two types of datasets that pandas identify first one is
# DataFrame(2 dimensional), Handle majority of tyupical ise cases in finanace, statistics
# , social science and many areas of engineering
# Second one is Series(1-dimensinal)
print(type(file_data))
# The above code is going to return as the DataFrame Object
print(type(file_data["temp"]))
# The above code is going to return as the Series Object because we are capturing only a single row
# Series is equivalent to list

# Below code example of converting the data into a dictionary
dictionary_data = file_data.to_dict()
print(dictionary_data)

# To convert a Series into a list
temp_row = file_data["temp"]
list_converted_temp = temp_row.tolist()
print(list_converted_temp)

# Calculate the average of the list_converted_temp
print(temp_row.mean())

# To find out the maximum
print(temp_row.max())

# Another method of getting the data from the column
print(file_data.condition)

# Get the data in the Row
print(file_data["day"] == "Monday")
print(file_data[file_data["temp"] == file_data["temp"].max()])

# To get the specific row values
monday = file_data[file_data["day"] == "Monday"]
print(monday["condition"])

# TO CONVET MONDAY temperature into fahremheit
monday_value = file_data[file_data["day"] == "Monday"]
monday_temp = monday_value["temp"][0]
monday_f = monday_temp * 9/5 + 32
print(monday_f)
