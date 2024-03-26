#nums = [2,7,11,15], target = 9, Output: [0,1]
nums = [3,2,4]
target = 6

number_set ={}
for number in range(len(nums)):
    number_set[nums[number]] = number


for number in range(len(nums)):
    index_to_find = target-nums[number]
    # print(index_to_find)
    # print(number_set)
    if index_to_find in number_set and number_set[index_to_find] != number:
        print (number, number_set[index_to_find])
        break
