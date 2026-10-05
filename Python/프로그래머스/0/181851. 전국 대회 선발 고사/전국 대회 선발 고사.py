def solution(rank, attendance):
    answer = 0
    amp = []
    for i in range(len(rank)):
        if attendance[i] == True:
            amp.append(rank[i])
    amp.sort()
    answer = 10000 * rank.index(amp[0]) + 100 * rank.index(amp[1]) + rank.index(amp[2])
    return answer