def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk = stk[:-1]  
        else:
            stk.append(arr[i])
        i += 1

    if len(stk) == 0:
        return [-1]
    return stk