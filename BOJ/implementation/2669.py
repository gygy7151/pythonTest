'''
직사각형
'''
'''
첫번째풀이
'''
import sys
def solution():
    graph = [[0 for _ in range(101)] for _ in range(101)]
    
    #네개만 받는다는걸 놓쳤다..
    for _ in range(4):
        x1, y1, x2, y2 = map(int, input().split())

        for dx in range(x1, x2):
            for dy in range(y1, y2):
                graph[dx][dy] = 1
    
    answer = 0
    for row in graph:
        answer += sum(row)
    print(answer)
solution()
        

