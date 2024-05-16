country = input("Add country name") 
visits = int(input("Number of visits"))  
list_of_cities = eval(input("Create list from formatted string")) 

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

empty_dictionary = {}
def add_new_country(country,visits,list_of_cities):
  empty_dictionary["country"] = country
  empty_dictionary["visits"] = visits
  empty_dictionary["cities"] = list_of_cities
  travel_log.append(empty_dictionary)
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")