first = input()
second = input()
third = input()


def find_number():
    if first.isdigit():
        return get_answer(int(first) + 3)
    elif second.isdigit():
        return get_answer(int(second) + 2)
    else:
        return get_answer(int(third) + 1)


def get_answer(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


print(find_number())
