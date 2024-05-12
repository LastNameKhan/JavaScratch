states_of_India = ["Madhya Pradesh","Rajasthan","Gujrat","Uttrakhand"]

# To get any value from the list
print(states_of_India[1])

# To get the items from the end of the list
print(states_of_India[-1])

# To Change the data at an specific index in the List
states_of_India[1] = "Delhi"
print(states_of_India)

# To add an Item at the end of the list
states_of_India.append("UP")
print(states_of_India)

# To add two list
states_of_India.extend(["State1","State2","State3"])
print(states_of_India)