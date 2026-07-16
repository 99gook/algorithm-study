def solution(a, b, c):
    total1 = a+b+c
    total2 = a**2 + b**2 + c**2
    total3 = a**3 + b**3 + c**3
    
    if a == b == c:
        return total1 * total2 * total3
    elif a == b or b == c or a == c:
        return total1 * total2
    else:
        return total1