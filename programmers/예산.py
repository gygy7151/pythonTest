'''
예산
'''
'''
두번째 풀이 - 시간복잡도 O(N) or 오메가(K)
'''
def solution(d, budget):
    d.sort()
    cnt = 0
    while d:
        if budget - d[0] >= 0:
            budget -= d[0]
            cnt += 1
            d.pop(0)
        else:
            break
    return cnt 

'''
첫번째 풀이 - 시간복잡도 세타(N)
'''
# def solution(d, budget):
#     answer = 0
#     d.sort()
#     res = 0
#     for i_d in d:
#         compare = res + i_d
#         if compare > budget:
#              break
#         res += i_d
#         answer += 1
#     return answer