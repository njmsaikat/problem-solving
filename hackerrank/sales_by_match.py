n=9
ar=[10,20,20,10,10,30,50,10,20]
def sockMerchant(n, ar):
    pair_dict={}
    for i in ar:
        if i not in pair_dict:
            pair_dict[i] =1
        else:
            pair_dict[i] +=1
    pair_count=0
    for i in pair_dict:
        pair = pair_dict[i]/2
        pair_count+=int(pair)
    # print(pair_count)
    return pair_count
sockMerchant(n, ar)