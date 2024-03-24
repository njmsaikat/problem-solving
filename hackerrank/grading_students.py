#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grade_list=[]
    for grade in grades:
        if grade<=35:
            final_grade_list.append(grade)
        else:
            next_multiple_of_five = (grade//5 +1)*5
            if next_multiple_of_five-grade<3:
                final_grade_list.append(next_multiple_of_five)
            else:
                final_grade_list.append(grade)
    return final_grade_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
