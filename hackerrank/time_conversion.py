#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time=s[:-2]
    indicator=s[-2:]

    time_hour = time[:2]
    time_min_sec = time[3:]

    if indicator=="PM" and time_hour!="12":
        time_hour = str(int(time_hour)+12)
    elif indicator=="AM" and time_hour=="12":
        time_hour = "00"
    else:
        time_hour = time_hour
    return str(time_hour+":"+time_min_sec)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
