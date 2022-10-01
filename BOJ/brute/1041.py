'''
주사위
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    min_lists = []

    if N == 1:
        arr.sort()
        # 5개면만 보이면 됨
        for i in range(5):
            ans += arr[i]
    
    else:
        min_lists.append(min(arr[0], arr[5]))
        min_lists.append(min(arr[1], arr[4]))
        min_lists.append(min(arr[2], arr[3]))
        min_lists.sort()

        # 1, 2, 3 면의 주사위 최솟값
        min1 = min_lists[0]
        min2 = min_lists[0] + min_lists[1]
        min3 = min_lists[0] + min_lists[1] + min_lists[2]

        #걍외우셈
        # 1, 2, 3 면의 주사위 개수
        n1 = 4 * (N - 2) * (N-1) + (N-2)*(N-2)
        n2 = 4 * (N-2) + 4 * (N-1)
        n3 = 4

        ans += n1 * min1
        ans += n2 * min2
        ans += n3 * min3
    
    print(ans)
solution()


