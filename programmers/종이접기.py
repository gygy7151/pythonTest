'''
종이접기
'''
# def solution():
#     grid = [[1, 4, 16, 1], [20, 5, 15, 8], [6, 13, 36, 14], [20, 7, 19, 15]]
#     answer = 0

#     for i in range(4):
#         for j in range(4):
#             for k in range(j+1, 4, 2):
#                 answer = max(answer, max(grid[i][j] + grid[i][k], grid[j][i] + grid[k][i]))
            
#     print(answer)

# solution()

'''
NC소프트 종이접기 문제 - 드뎌 맞췄다..가 아님..
니가 예전에 접근했던 것처럼 왼쪽 오른쪽 모두다 for문 돌려줘야됨
1차원배열 입력값으로 주어지는 종이를
k번 이하로 접고
그 배열의 최댓값을 구하는게 목적임
단 1 <= k <= 4
배열안의 숫자 값은 100이하의 정수임
종이의 길이는 50이하였음
'''
def solution():
    N, K = map(int, input().split())
    paper = list(map(int, input().split()))
    ans = -1

    # dfs를 활용할거임
    def dfs(paper, depth):
        nonlocal ans
        # 만약 depth가 k이면 
        ## paper중 최댓값이 ans보다 크면 ans를 갱신한다
        ## 안크면 그냥 종료한다.
        if depth == K:
            MAX = max(paper)
            if ans < MAX:
                ans = MAX
            return

        # 종이를 왼쪽부터 0번째부터 종이 길이 절반까지 차례대로 먼저 접는다
        for i in range(len(paper)//2):
            right = paper[0:i+1] #0인덱스부터 접근하는거 주의!
            left = paper[i+1:]
            # print('*'*50)
            # print(right, left)
            
            right_temp = []
            right_end = len(right)
            right_tail = -int(1e9)
            
            if right_end % 2 != 0:
                right_tail = right.pop()

            while right:
                right_temp.append(right.pop(0) + right.pop())

            if right_tail > 0:
                right_temp.append(right_tail)

            # print(right_temp+left)
            # print('*'*50)
            dfs(right_temp+left, depth+1)
        
        # 종이를 오른쪽부터 len(paper)-1번째부터 종이 길이 절반까지 차례대로 먼저 접는다
        for i in range(len(paper)-1, (len(paper)//2)-1,-1): #세로선은 모든 세로선 다 체크해줘야됨
            left = paper[0:i]
            right = paper[i:] #0인덱스부터 접근하는거 주의!
            # print('*'*50)
            # print(left, right)
            
            right_temp = []
            right_end = len(right)
            right_tail = -int(1e9)
            
            if right_end % 2 != 0:
                right_tail = right.pop()

            while right:
                right_temp.append(right.pop(0) + right.pop())

            if right_tail > 0:
                right_temp.append(right_tail)

            # print(left + right_temp)    
            # print('*'*50)
            dfs(left+right_temp, depth+1)
    
    dfs(paper, 0) # 시작은 한번도 안접었으므로 0
    print(ans)

solution()




