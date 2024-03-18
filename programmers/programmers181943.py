def solution(my_string, overwrite_string, s):
    my_string_list = list(my_string)
    overwrite_list = list(overwrite_string)
    answer = ''
    adx = 0
    for i in range(len(my_string)):
        if(i < s):
            answer += my_string[i]
        elif(adx < len(overwrite_list)):
            answer += overwrite_list[adx]
            adx += 1
        else:
            answer += my_string_list[i]
    return answer

solution('He11oWor1d', 'lloWorl', 2)