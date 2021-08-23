# find number of ways in which a number can be expressed as a sum of consecutive integers (> 0)

def consecutive(num):
    numberOfWays = 0
    upperBound = int((((2 * num) + 0.25) ** 0.5) - 0.5) + 1
    for i in range(1, upperBound):
        num -= i
        if num % i == 0:
            numberOfWays += 1
    
    return numberOfWays - 1
