'''
소트
'''
'''
첫번째/두번째풀이  

1. i번째 인덱스에서 최댓값을 구하고 인덱스를 구한다
2. 구한 인덱스값을 범위로 -1씩 범위를 좁히며 교환한다.
3. 남은횟수 S에 idx-i를 빼주어 횟수를 갱신한다.
4. 만약 S가 0보다 작거나 같으면 nums를 출력한다.
'''
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    S = int(input())

    for i in range(N):
        # 탐색
        max_num = max(nums[i: min(N, i + S + 1)])
        idx = nums.index(max_num)

        # 교환
        for j in range(idx, i, -1):
            nums[j], nums[j-1] = nums[j-1], nums[j]
        
        # 후처리
        # idx - j아님 주의
        S -= (idx -i)
        
        if S <= 0: break

    print(*nums)
solution()
