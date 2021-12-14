'''
'큰수의 법칙'
숫자가 더해지는 횟수 M이 7이고, K번을 초과하여
더해질 수 없는 법칙, 배열의크기 N
반복되는 수열의 길이는? M/(K+1)
첫번째로 큰수의 개수는 M-(M/(K+1))
두번째로 큰수의 개수는 M/(K+1)
'''

n, m ,k = map(int, input().split())

'''
'''

def solution(n, m, k):
    
    #제일 큰수와 제일 작은수를 구해야지
    arr = input().split()
    arr.sort()
    first = int(arr[n-1])
    second = int(arr[n-2])
    
    #그리고? 제일큰수는  (M/(K+1)) + M % (K+1)번만큼 곱해주어 큰수가 더해진 전체 개수를 result에 담는다
    #제일 작은수의 개수는 전체 M번더한개수에서 result개수를 감해주면 구해진다.
    result = first * ( (n/(k+1)) + m % (k+1))
    result  += second * (m - result)

    print(result)


solution(n, m, k)
