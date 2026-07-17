def solution(num_list):
    num = 1
    for i in num_list:
        num *= i
    if num < sum(num_list)**2: return 1
    else: return 0