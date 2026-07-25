def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        sliced_arr = arr[s:e+1]
        
        valid_nums = []
        for num in sliced_arr:
            if num > k:
                valid_nums.append(num)
        if valid_nums:
            answer.append(min(valid_nums))
        else:
            answer.append(-1)
    return answer