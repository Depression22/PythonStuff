def enough(cap, on, wait): #capacity, people on bus alrd, people waiting to get in
    sum = wait + on
    if  sum <= cap:
        return 0
    if sum > cap:
        return sum - cap

print(enough(10, 5, 5))