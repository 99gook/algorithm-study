def solution(myString, pat):
    my = myString.replace("A","@").replace("B","A").replace("@","B")
    if pat in my:
        return 1
    else:
        return 0