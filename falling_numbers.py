import math

def falling_numbers(n) :
    while(True):
        fact = math.pow(n,.9)
        n = n + fact + 1
        print(n)

falling_numbers(1)
