'''
더하기사이클
'''
N = input()
if int(N) < 10:
    N = '0' + N
temp_N = N
cycle = 0
while True:
    n_sum = 0
    cycle += 1
    # str -> int
    temp = list(map(int, temp_N))
    n_sum = sum(temp)
    n_sum = str(n_sum)
    res = temp_N[-1]+ n_sum[-1]
    
    if res == N:
        break
    else:
        temp_N = res
print(cycle)
