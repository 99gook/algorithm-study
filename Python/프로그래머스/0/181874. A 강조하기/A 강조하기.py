def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i] == 'a':
            answer += myString[i].upper()
        elif myString[i] == 'A':
            answer += myString[i]
        else:
            answer += myString[i].lower()
        
    return answer