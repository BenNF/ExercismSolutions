def is_armstrong(number):
    number = str(number)
    power = len(number)
    return int(number) == sum([int(x)**power for x in number])


