def solution(strArr):
    x = [0] * 31
    for i in strArr:
        x[len(i)] += 1
    return max(x)            