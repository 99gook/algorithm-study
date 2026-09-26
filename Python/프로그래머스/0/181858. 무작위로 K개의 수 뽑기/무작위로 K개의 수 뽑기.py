def solution(arr, k):
    answer = []
    for num in arr:
        if num not in answer:
            answer.append(num)
        if len(answer) == k:
            break
    answer += [-1] * (k - len(answer))        
    return answer