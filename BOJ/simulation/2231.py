'''
분해합
'''
def solution():
    N = int(input())
    INF = int(1e9)
    ans = INF

    if N == 1:
        print(0)
        return

    for M in range(N):
        i_digits_sum = list(map(int, list(str(M))))
        i_digits_sum = sum(i_digits_sum)
        divided_sum = M + i_digits_sum

        if divided_sum == N:
            ans = min(ans, M)

    if ans == INF:
        print(0)
    else:
        print(ans)
solution()