N,n=input(),input().split() 
print(all(int(each_element)>=0 for each_element in n) and any(each_element==each_element[::-1] for each_element in n))