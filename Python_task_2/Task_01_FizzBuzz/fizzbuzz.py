def fizzbuzz_checker(limit):
    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


if __name__ == "__main__":
    fizzbuzz_checker(int(input("Enter the limit: ")))
