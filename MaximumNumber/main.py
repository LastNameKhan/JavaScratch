student_score = [78, 65, 89, 86, 55, 91, 64, 89]

max_number = 0
track_score = 0
for score in student_score:
    if max_number <= score:
        max_number = score

print(max_number)

#Second Logic

heighest_score = 0
for score in student_score:
    if score > heighest_score:
        heighest_score = score

print(heighest_score)

