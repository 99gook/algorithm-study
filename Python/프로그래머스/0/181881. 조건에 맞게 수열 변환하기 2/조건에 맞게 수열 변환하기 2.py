def solution(arr):
    answer = 0
    while True:
        new_arr = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                new_arr.append(i // 2)
            elif i < 50 and i % 2 == 1:
                new_arr.append(i * 2 + 1)
            else:
                new_arr.append(i)

        if new_arr == arr:
            return answer

        arr = new_arr
        answer += 1