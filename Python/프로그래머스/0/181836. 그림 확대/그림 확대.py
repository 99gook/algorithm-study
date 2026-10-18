def solution(picture, k):
    answer = []
    for row in picture:              
        wide = ''
        for ch in row:               
            wide += ch * k           
        for _ in range(k):           
            answer.append(wide)
    return answer