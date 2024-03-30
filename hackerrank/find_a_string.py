def count_substring(string, sub_string):
    s_len=len(string)
    ss_len=len(sub_string)
    counter=0
    for i in range(s_len-ss_len+1):
        # print(string[i:i+ss_len])
        if string[i:i+ss_len]==sub_string:
            counter+=1

    # print(counter)
    return counter


count_substring("ABCDCDC", "CDC")