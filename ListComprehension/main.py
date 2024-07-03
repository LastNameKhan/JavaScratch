# Comprehension is the used to create a list from the existing list without using the for loop

numbers = [1, 2, 3]
# new_list = [new_item for item in list]
# Below is the syntax for the list Comprehension
new_list = [item+1 for item in numbers]
print(new_list)


# To do operation in string using List Compreshension

name = "AmanKhan"
new_string = [n for n in name]
# The above code will return us the Each alphabet in the list
print(new_string)

# Working with the range in List Comprehension
new_range_data = [n for n in range(1, 5)]
print(new_range_data)

name_list = ["Aman", "khan", "Rahul", "Harshit", "Choke", "Sabudana"]
shot_name_list = [n for n in name_list if len(n) <= 5]
long_name_list = [n.upper() for n in name_list if len(n) > 5]
print(long_name_list)
