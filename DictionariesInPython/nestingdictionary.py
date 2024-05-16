# Nesting
capitals = {
    "France":"Paris",
    "Germany":"Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"],
}

# Nesting List in List
["A","B",["C","D"]]

# Nesting Dictionary in a Dictionary
travel_data = {
    "France": {"cities_visited":["Paris","Lille","Dijon"],"total_vsists":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visits":5}
}

# Nesting a Dictionary in a List
travel_data = [
    {
        "Country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_vsists":12
    },
    {
        "Country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    },
]