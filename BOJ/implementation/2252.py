'''
줄세우기
'''
'''
첫번째풀이
N : 학생수, 학생번호는 1번부터 N번까지임
M : 키를 비교한 횟수
A, B가 주어지면 A가 항상 B앞에 있어야됨
학생 키 순서대로 줄 세우려고 함
답이 여러가지인 경우에는 아무거나 출력함

위상정렬을 활용
'''
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    indegree = [ 0 for _ in range(N+1)]
    G = [[] for _ in range(N+1)]
    answer = []

    for _ in range(M):
        A, B = map(int, input().split())
        indegree[B] += 1
        G[A].append(B)
    
    q = deque()
    
    for idx in range(1,N+1):
        if indegree[idx] == 0:
            q.append(idx)
    
    while q:
        vertex = q.popleft()
        answer.append(vertex)

        for nextVertex in G[vertex]:
            indegree[nextVertex] -= 1

            if indegree[nextVertex] == 0:
                q.append(nextVertex)
    
    print(*answer)

solution()









