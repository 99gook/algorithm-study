def solution(my_strings, parts):
    answer = ""
    for i in range(len(my_strings)):
        string = my_strings[i]
        s = parts[i][0]
        e = parts[i][1]
        answer += string[s:e+1]
    return answer