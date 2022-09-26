'''
ACM Craft
'''
'''
두번째풀이 - 진입차수 순서대로 dp를 돌려줘야해서 위상정렬 알고리즘을 활용했다.
'''
from collections import deque

def solution():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        time = [0] + list(map(int, input().split()))
        seq = [[ ] for _ in range(N+1)] # 건설순서규칙
        inDegree = [0 for _ in range(N+1)] # 진입차수
        DP = [ 0 for _ in range(N+1)] # 해당 건물까지 걸리는 최소 시간

        for _ in range(K):
            a, b = map(int, input().split())
            seq[a].append(b)
            inDegree[b] += 1
        
        q = deque()
        for i in range(1, N+1): # 진입차수 0인거 찾아서 q에 넣기 (이때 1개이상일 수 있음 주의)
            if inDegree[i] == 0:
                q.append(i)
                # 시작값 초기화
                DP[i] = time[i]
        
        while q:
            a = q.popleft()
            for i in seq[a]:
                inDegree[i] -= 1 # 진입차수 줄이고
                DP[i] = max(DP[a] + time[i], DP[i])
                if inDegree[i] == 0:
                    q.append(i)
        
        ans = int(input())
        print(DP[ans])
solution()
            
        


'''
첫번째풀이
'''
# 첫번째 게임과 두번째 게임이 건물 짓는 순서가 다를 수 있다.
# 각 줄의 입력데이터는 건설순서 규칙이 주어진다
# 특정 건물을 짓기 위한 순서가 달라지므로 특정 건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내자
# 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미.
# 테스트 케이스 갯수 T
# 규칙의 총갯수 K
# 건물의 갯수 N - 1-indexed
# 건설해야할 건물번호 W
# 건물 X를 지은다음 건물 Y를 짓는것이 가능하다는 규칙 X Y

# from collections import defaultdict
# def solution():
#     # i번째 건물 건설에 걸리는 시간 Di
#     # i번째 건물을 건축하기 위한 전제조건 건물번호를 담은 배열 K(2번 인덱스부터시작/1번건물은 해당없음)
#     # i번 건물이 가장 빨리 완성되기 까지 걸리는 최소시간을 담은 배열 DP(1번째 요소는 D[1]로 초기화)
#     # 건물건설에 걸리는 시간을 D에 담는다.
#     # 규칙 a, b가 k개가 주어지면 defaultdict[b].append(a)를 한다 단 값이 0이면 defaultdict[b] = [a]를 대입한다.
#     # 2번째건물부터 i번째(i는 최대N) 건물까지 K[i] 요소 building 값을 for문으로 돈다.
#     # 만약 DP[building] + D[i]가 DP[i]값보다 크다면 DP[i]값을 갱신한다.
#     # - 최소시간인데 왜냐? i번째건물은 K[i]에 있는 모든건물이 건설 완료 되어야만 짓기가 가능하기 때문에 가장 오래걸리는 건물시간을 최종 소요시간을 결정한다.
#     # 최종 건물번호 DP[W]를 출력하면 다음 테스트 케이스로 넘어간다.
#     # 위과정을 총 T번 돌린다.
#     T = int(input())
    
#     for _ in range(T):
#         n, k = map(int, input().split())
#         # i번째 건물 건설에 걸리는 시간 Di
#         # i번째 건물을 건축하기 위한 전제조건 건물번호를 담은 배열 K(2번 인덱스부터접근필요/1번건물은 해당없음)
#         D, K = list(map(int, input().split())), defaultdict(int)  # D,K는 0인덱스로 시작
#         # i번 건물이 가장 빨리 완성되기 까지 걸리는 최소시간을 담은 배열 DP
#         DP = [ 0 for _ in range(n)]

#         # i번째 건물짓기위해 먼저 건축완료되어야할 건물번호를 K에 채운다.
#         for _ in range(k):
#             a, b = map(int, input().split())
            
#             if K[b-1] != 0 and b :
#                 K[b-1].append(a-1)
#             else:
#                 K[b-1] = [a-1]
        
#         # 백준이가 건설해야할 건물 번호 W
#         W = int(input())

#         print(K)
#         # 2번째건물부터 i번째(i는 최대N) 건물까지 K[i] 요소 building 값을 for문으로 돈다.
#         for i in range(n):
#             if K[i] != 0:
#                 for j in K[i]: #j 는 빌딩넘버
#                     # 만약 DP[j] + D[i]가 DP[i]값보다 크다면 DP[i]값을 갱신한다.
#                     if i == 0 and j > i:
#                         if D[j] + D[i] > DP[i]:
#                             DP[i] = D[j] + D[i]
#                     else:
#                         if DP[j] + D[i] > DP[i]:
#                             DP[i] = DP[j] + D[i]
#             else:
#                 DP[i] =max(D[i], DP[i])
        
#         # 최종 건물번호 DP[W]를 출력한다.
#         print(DP[W-1])
# solution()

        
            
            


        



    





