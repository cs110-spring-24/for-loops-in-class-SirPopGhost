count = 0
for e in range(30):
    count = count + 1
    if count % 15 == 0:
        print("FizzBuzz")
    elif count % 5 == 0:
        print("Buzz")
    elif count % 3 == 0:
        print("Fizz")
    else:
        print(count)
