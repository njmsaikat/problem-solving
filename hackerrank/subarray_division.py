s=[1, 2, 1, 3, 2]
d=3
m=2
def birthday(s, d, m):
    numbers=len(s)
    divide_chocolate = 0
    for piece in range(numbers+1):
        sum = 0
        for index in range(piece, m+piece):
            if (m+piece < numbers+1):
                sum += s[index]
        if (sum == d):
            divide_chocolate += 1
    
    return divide_chocolate

print(birthday(s, d, m))