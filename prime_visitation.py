#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lightBulbs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY states
#  2. INTEGER_ARRAY numbers
#

def lightBulbs(states, numbers):
    prime_list = []
    for number in numbers:
        for i in range(2, number+1):
            if(number % i == 0):
                p = 1
                for j in range(2, (i //2 + 1)):
                    if (i % j == 0):
                        p = 0
                        break
                
                if p == 1:
                    prime_list += [i]
    for prime in prime_list:
        for i in range(prime-1, len(states), prime):
            if (states[i]==1):
                states[i] = 0
            else:
                states[i] = 1
                
    return states
