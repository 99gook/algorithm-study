def solution(n):
    answer = []
    for j in range(n):
        row = []
        for i in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        answer.append(row)        
    return answer
