def solution(my_string):
    result = [0] * 52
    for ch in my_string:
        if ch.isupper():
            idx = ord(ch) - ord('A')
        else:
            idx = ord(ch) - ord('a') + 26
        result[idx] += 1
    return result