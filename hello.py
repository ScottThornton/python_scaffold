import math

def add(x, y):
    return x+y

def hypotenuse(x, y):
    return math.sqrt(pow(x,2) + pow(y,2)) 

a = 3
b = 6
result = hypotenuse(a, b)
print(f"This is the hypotenuse: {a}, {b}, {result}")
