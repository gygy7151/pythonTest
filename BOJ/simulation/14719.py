'''
빗물
'''
'''
첫번째풀이
'''
def solution():
    H, W = map(int, input().split())
    block = list(map(int, input().split()))
    N = len(block)
    answer = 0

    if H <= 2 and W <=2:
        print(answer)
        return

    for i in range(1,N-1):
        now = block[i]
        left, right = max(block[0:i]), max(block[i:])
        
        if now < left and now < right:
            
            if left != right:
            
                if left > right:
                    answer += right - now
            
                else:
                    answer += left - now
            
            else:
                answer += right - now
    
    print(answer)
solution()