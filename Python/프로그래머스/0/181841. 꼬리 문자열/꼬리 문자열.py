def solution(str_list, ex):
    answer = ''
    for ch in str_list:
        if ex not in ch:
            answer += ch 
    return answer