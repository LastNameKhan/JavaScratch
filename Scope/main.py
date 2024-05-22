# NameSpace

enemies = 1

# Local Scope exists whithin a function
def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_portion():
    potion_strength = 2
    print(potion_strength)

drink_portion()
# Below Line will give an error that name potion_strength
# id not defined although we have defined it but if we define a variable inside
# a function we can only access that inside a function because it has local scope
# print(potion_strength)

# Global Scope
# Global Variables if defined within functions and no matter where we declare them.
player_health = 10
def drink_health():
    player_health = 2
    print(player_health)
    
drink_health()

# Modifying Global Scope

friends = 1
def increase_friends():
    # using global keyword to modify the global varibale
    # Without using global keyword we cannot do it
    global friends
    friends = 2
    print(f"Friends inside function: {friends}")

increase_friends()
print(f"Friends outside function: {friends}")

