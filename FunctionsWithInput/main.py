def greet():
    print("Hello")
    print("How do you do?")
    print("Hi")

greet()

#Function that allows the input
# Here the name is the parameter and the value inside it is called as an
# argument Aman is an argument passed by paramter name
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Hi {name}")

greet_with_name("Aman")

# Functions with more than 1 input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like to live in {location}")

greet_with("Aman","Nagda")

# Functiona with keyword
def greet_with_keyword(name, location):
    print(f"Hello {name}")
    print(f"How does it feel like living in {location}")

greet_with_keyword(name="Aman", location="Indore")