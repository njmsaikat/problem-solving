if __name__ == '__main__':
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append([score, name])
        score_list.append(score)
    sorted_score = (sorted(set(score_list)))
    second_lowest_score = sorted_score[1]

    second_lowest_score_name_list = []
    for score_name in name_list:
        if score_name[0]==second_lowest_score:
            second_lowest_score_name_list.append(score_name)
    
    second_final_name_list = sorted(second_lowest_score_name_list)
    for individual_name in second_final_name_list:
        print(individual_name[1])