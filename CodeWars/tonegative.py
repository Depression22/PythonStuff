def make_negative( number ):
    if number == 0:
        return 0
    elif number < 0:
        return number
    elif number > 0:
        return -number
        


print(make_negative(1))
print(make_negative(2))
print(make_negative(10))
print(make_negative(-1))
print(make_negative(0))