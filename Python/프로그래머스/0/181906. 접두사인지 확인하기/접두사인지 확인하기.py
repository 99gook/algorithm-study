def solution(my_string, is_prefix):
    n = len(is_prefix)
    if is_prefix == my_string[:n]:
        return 1
    else:
        return 0