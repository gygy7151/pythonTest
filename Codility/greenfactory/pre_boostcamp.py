'''
함수구현
'''
def solution(arr):
    memo = [0] * 101
    TN = arr[0]
    cnt = 1
    
    for i in range(1,len(arr)):
        if arr[i] >= 0:
            if TN == arr[i]:
                cnt +=1
            else:
                memo[TN] += cnt
                TN = arr[i]
                cnt = 1
    if arr[i] >= 0:
        if arr[-2] == arr[-1]:
            memo[arr[-2]] += cnt
        else:
            memo[arr[-1]] += 1
    
    ans = []
    
    for i in range(1,101):
        if memo[i] >= 2:
            ans.append(memo[i])
    
    if not ans:
        ans.append(-1)
    return ans

A = [0,0,1,1,1,2,1,3,2,2,2,0]
print(solution(A))