limit = int(input("Pleaase Enter the Limit to get the list of all the even numbers\n"))+1

total = 0
for number in range(2,limit,2):
    total += number

print(total)