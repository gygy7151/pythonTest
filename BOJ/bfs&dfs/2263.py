'''
트리의 순회
'''
'''
첫번째풀이 -  어렵다..
'''
import sys
sys.setrecursionlimit(10**6)

def solution():
    node_count = int(input())
    
    in_order = list(map(int, input().split()))
    post_order = list(map(int, input().split()))
    
    N = len(in_order)
    node_order = [0 for _ in range(N+1)]

    # 전위 순회로 사용될 리스트 초기화 - 중위순회 활용
    for i in range(N):
        node_order[in_order[i]] = i


    def pre_order(in_start, in_end, post_start, post_end):
        
        #이진탐색 기본 구조: 시작점이 끝점보다 커지면 이분탐색종료
        if in_start > in_end or post_start > post_end:
            return
        
        #재귀 이므로 단순히 -1로하면 안됨
        root = post_order[post_end]
        mid = node_order[root]

        left = mid - in_start
        right = in_end - mid

        print(root, end = " ")
        pre_order(in_start, in_start + left - 1, post_start, post_start + left - 1)
        pre_order(in_end - right + 1, in_end, post_end - right, post_end - 1)
    
    pre_order(0, N-1, 0, N-1)
    print()

solution()





        

        
