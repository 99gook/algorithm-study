def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs :
        str = str[s : s+l]
        if int(str) > k :
            answer.append(int(str))
    return answer