def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left * mpg  >=  distance_to_pump: 
        return True
    else : 
        return False
    #Happy Coding! ;)
    
print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))
print(zero_fuel(150, 25, 3))