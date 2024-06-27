# To read into a file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)


# To write into a file
# use mode="w" - which delets the content present and add new content to the file
# use mode="a" if you don't want to delete the content and only add new content to the file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# To create a new File is the file does not exists it is going to create a new file for us
# The new file creation only works when we are in the mode="w" write mode only
with open("new_file.txt", mode = "w") as file:
    file.write("This is a new File created")


