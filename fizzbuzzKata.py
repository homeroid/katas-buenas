def fizzbuzz(num):
    if int (num) % 15 == 0:
        return "fizzbuzz"
    elif int (num) % 3 == 0:
        return "fizz"
    elif int (num) % 5 == 0:
        return "buzz"
        return "0"


    raise NotImplementedError