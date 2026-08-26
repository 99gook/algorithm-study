def solution(num_list):
    answer = 0
    case1 = 0
    case2 = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            case1 += num_list[i]
        else:
            case2 += num_list[i]
    if case1 > case2:
        answer = case1
        
    elif case1 < case2:
        answer = case2
        
    else:
        answer = case1
    return answer