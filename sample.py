def FizzBuzz(num):
    div_5 = str(num%5)
    div_3 = str(num%3)
    if div_5 == "0" and div_3 == "0":
        return "FizzBuzz"
    elif div_5 == "0":
        return "Buzz"
    elif div_3 == "0":
        return "Fizz"
    else:
        return str(num)