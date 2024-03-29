arr=[1,2,3,4,5,4,3,2,1,3,4]
def migratoryBirds(arr):
    bird_type_count={}
    for each_type in arr:
        if each_type in bird_type_count:
            bird_type_count[each_type]+=1
        else:
            bird_type_count[each_type]=1
    # print(bird_type_count)
    bird_type_count = dict(sorted(bird_type_count.items()))
    
    print(max(bird_type_count, key=bird_type_count.get))
migratoryBirds(arr)