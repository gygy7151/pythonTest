'''
상어초등학교
'''
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n = int(input())
p = n * n
classroom = [[0]*(n) for _ in range(n)]
like_room = [[] for _ in range(p+1)]
for _ in range(p):
    data = list(map(int, input().split()))
    #data[0]은 학생번호로 추후 활용
    like = data[1:]
    like_room[data[0]] = like
    temp = []
    for i in range(n):
        for j in range(n):
            sum_like, sum_empty = 0, 0
            if classroom[i][j] != 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = i + dy[k]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if classroom[i][j] in like:
                    sum_like += 1
                if classroom[nx][ny] == 0:
                    sum_empty += 1
            temp.append((sum_like, sum_empty, (i,j)))
    temp.sort(key = lambda x : (-x[0], -x[1], x[2]))
    classroom[temp[0][2][0]][temp[0][2][1]] = data[0]

sum_answer = 0
for i in range(n):
    for j in range(n):
        answer = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or nx >= n or ny < 0  or ny >= n:
                continue
            if classroom[nx][ny] in like_room[classroom[i][j]]:
                answer += 1
                continue
        if answer != 0:
            sum_answer += (10 ** (answer-1))
print(sum_answer)


