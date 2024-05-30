class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
#To start with something that is going to have a default value at initial and later going to change
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Aman")
print(user_1.user_id)
print(user_1.username)
# We can directly fetch the user_count as we don't have to pass any value in the class attributes
# because default value is already given to it.
print(user_1.followers)

user_2 = User("002","Khan")
print(user_2.user_id)
print(user_2.username)

# When we add parameters to the constructor which is the init function
# Means whenever a new object is being constructed from this class, it must provide these
# two pieces of data. - user_id and username

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
