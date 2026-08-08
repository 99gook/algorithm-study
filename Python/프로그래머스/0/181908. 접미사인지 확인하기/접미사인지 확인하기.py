def solution(my_string, is_suffix):
    n = len(is_suffix)
    if is_suffix == my_string[ -n: ]:
        return 1
    else:
        return 0