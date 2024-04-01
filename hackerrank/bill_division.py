bill=[3,10,2,9]
k=1
b=12

def bonAppetit(bill, k, b):
    shared_bill=0
    for i in range(len(bill)):
        if i!=k:
            shared_bill+=bill[i]
    bill_charged=shared_bill/2
    if bill_charged!=b:
        print(int(b-bill_charged))
    else:
        print("Bon Appetit")
bonAppetit(bill, k, b)