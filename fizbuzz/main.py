def fizzbuzz(value: int):
    if value % 15 == 0:
        return "Fizz Buzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"

    return str(value)
