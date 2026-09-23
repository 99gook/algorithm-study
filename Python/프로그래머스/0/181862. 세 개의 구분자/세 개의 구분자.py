def solution(myStr):
    answer = []
    replaced = myStr.replace("b","a").replace("c","a")
    pieces = replaced.split("a")
    for i in pieces:
        if i != "":
            answer.append(i)
    if len(answer) == 0:
        answer = ["EMPTY"]
    return answer