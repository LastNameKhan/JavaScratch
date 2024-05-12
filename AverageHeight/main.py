student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total Height = {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"Total Number of Students = {number_of_students}")

average_heights = round(total_height/number_of_students)
print(f"Average Height = {average_heights}")