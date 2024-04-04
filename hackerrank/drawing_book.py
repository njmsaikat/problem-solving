n=6
p=2
def pageCount(n, p):
    front_turn=p//2
    back_turn=n//2-front_turn
    min_turn=min(front_turn,back_turn)
    # return min_turn
    print(min_turn)

pageCount(n, p)