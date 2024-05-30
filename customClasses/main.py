class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username


user_1 = User("001", "Aman")
print(user_1.user_id)
print(user_1.username)

user_2 = User("002","Khan")
print(user_2.user_id)
print(user_2.username)

# When we add parameters to the constructor which is the init function
# Means whenever a new object is being constructed from this class, it must provide these
# two pieces of data. - user_id and username
