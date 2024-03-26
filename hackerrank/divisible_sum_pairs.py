n=6
k=3
ar=[1, 3, 2, 6, 1, 2]
def divisibleSumPairs(n, k, ar):
    ar=sorted(ar)
    count=0
    for i in range(n
    
    
    
    ):
        print(ar[i])
        if (ar[i]<ar[i+1]) and ((ar[i+1]+ar[i])%k) == 0:
            count += 1
    print(count)
divisibleSumPairs(n, k, ar)