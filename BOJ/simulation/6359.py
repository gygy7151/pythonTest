'''
만취한 상범
'''
def solution():
    K = int(input())
    M = int(input())
    friend = [1 for _ in range(K+1)]
    
    cal = [ int(input()) for _ in range(M)]
    for i in range(M):
        num = cal[i]
        j = 1
        while num*j <= K:
            friend[num*j] = 0
            j += 1

    print(friend)
    for i in range(1, K+1):
        if friend[i]:
            print(i)

solution()
