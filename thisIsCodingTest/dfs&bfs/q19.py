'''
연산자 끼워넣기/BJ14888
'''
n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))
min_val = int(1e9)
max_val = -int(1e9)
def dfs(cnt, result, add, minus, multiple, divide):
    global min_val
    global max_val
    if cnt == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    
    if add > 0:
        dfs(cnt + 1, result + a[cnt], add - 1, minus, multiple, divide)

    if minus > 0:
        dfs(cnt + 1, result-a[cnt], add, minus - 1, multiple, divide)

    if multiple > 0:
        dfs(cnt + 1, result * a[cnt], add, minus, multiple - 1, divide)

    if divide > 0:
        dfs(cnt + 1, -((-result) // a[cnt]) if result < 0  else (result) // a[cnt], add, minus, multiple, divide-1)

dfs(1, a[0], o[0], o[1], o[2], o[3])
print(max_val)
print(min_val)