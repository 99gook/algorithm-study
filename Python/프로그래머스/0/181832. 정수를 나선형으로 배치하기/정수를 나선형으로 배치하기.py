def solution(n):
    a = [[0] * n for _ in range(n)] #n x n 크기의 빈 판을 만든다는 의미
    y, x = 0, 0  #시작 기준 좌표
    d = "right"  #배열 진행 방향 설정
    for i in range(1, n*n+1):
        a[y][x] = i #지금 서있는 칸에 i를 넣는다는 의미
        if d == "right":
            if x + 1 < n and a[y][x+1] == 0: #오른쪽으로 가면서 판이 비어있는지, 비어있으면 x 값에 계속 1을 더할꺼임
                x += 1
            else:
                d = "down"
                y += 1
        elif d == "down":
            if y + 1 < n and a[y+1][x] == 0: #아래로 가면서 판이 비어있는지, 비어있으면 y 값에 계속 1을 더할꺼임
                y += 1
            else:
                d = "left"
                x -= 1
        elif d == "left":      
            if x - 1 >= 0 and a[y][x-1] == 0: #왼쪽으로 가면서 판이 비었는지, 비어있으면 x 값에 -1을 더하며 좌측으로 이동함
                x -= 1
            else:
                d = "up"
                y -= 1
        else:
            if y - 1 >= 0 and a[y-1][x] == 0: #위로 이동하면서 판이 비었는지, 비어있으면 y 값에 계속 -1을 더하며 올라감
                y -= 1
            else:
                d = "right"
                x += 1
    return a            
                
                
        