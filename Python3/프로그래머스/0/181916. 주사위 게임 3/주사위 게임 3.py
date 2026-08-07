def solution(a, b, c, d):
    dice = [a, b, c, d]
    
    count = {}
    for x in dice:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    
    keys = list(count.keys())    
    values = list(count.values()) 
    if len(keys) == 1:
        p = keys[0]
        return 1111 * p
    
    elif len(keys) == 2:
        if 3 in values:
            p = keys[values.index(3)]
            q = keys[values.index(1)]
            return (10 * p + q) ** 2
        else:
            p = keys[0]
            q = keys[1]
            return (p + q) * abs(p - q)
    
    elif len(keys) == 3:
        singles = [k for k, v in count.items() if v == 1]
        return singles[0] * singles[1]
    
    else:
        return min(dice)