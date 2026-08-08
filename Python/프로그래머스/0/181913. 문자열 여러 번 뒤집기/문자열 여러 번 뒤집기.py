def solution(my_string, queries):
    s = list(my_string)
    for start, end in queries:
        s[start:end+1] = s[start:end+1][::-1]
    return ''.join(s)