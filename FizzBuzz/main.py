target  = int(input("Please Enter a value to get the result\n"))
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        number = "FizzBuzz"
    elif number % 3 == 0:
        number = "Fizz"
    elif number % 5 == 0:
        number = "Buzz"
    print(number)