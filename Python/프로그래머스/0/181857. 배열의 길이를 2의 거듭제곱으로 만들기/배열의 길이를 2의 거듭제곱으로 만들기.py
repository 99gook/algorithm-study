def solution(arr):
    for i in range(11):          
        if 2**i >= len(arr):
            diff = 2**i - len(arr)
            break

    for k in range(diff):
        arr.append(0)

    return arr