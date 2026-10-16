def solution(order):
    answer = 0
    for menu in order:
        if 'latte' in menu:
            answer += 5000
        else:
            answer += 4500
    return answer