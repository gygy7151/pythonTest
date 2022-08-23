'''
친구
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    G = []
    values = [0 for _ in range(N)]

    for _ in range(N):
        temp = set()
        datas = list(input())
        M = len(datas)
        
        for i in range(M):
            if datas[i] == 'Y':
                temp.add(i)
        
        G.append(temp)
    
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if j in G[i]:
                values[i] += 1
            
            elif G[i] & G[j]:
                values[i] += 1

    print(max(values))

solution()

