arr=[-4, 3, -9, 0, 4, 1]
def plusMinus(arr):
    arr_length = len(arr)
    positive=0
    negative=0
    zero=0

    for element in arr:
        if element>0:
            positive+=1
        elif element<0:
            negative+=1
        else:
            zero+=1
    list_of_values=[]
    list_of_values.append(positive/arr_length)
    list_of_values.append(negative/arr_length)
    list_of_values.append(zero/arr_length)
    
    for element in list_of_values:
        print("{:.6f}".format(element))

plusMinus(arr)