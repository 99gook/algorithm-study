def solution(myString):
    answer = myString.split("x")
    answer.sort()
    count = 0
    for a in answer:
        if a == "":
            count += 1
    return answer[count:]