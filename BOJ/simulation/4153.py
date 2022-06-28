'''
직각삼각형
'''
'''
세번재풀이 - 피타고라스의 증명활용
'''
def solution():
    answer = []
    while True:
        n = list(map(int, input().split()))
        if not sum(n):
            return answer
        
        n.sort(reverse=True)
        if n[0]**2 == (n[1]**2 + n[2]**2):
            answer.append('right')
        else:
            answer.append('wrong')

res = solution()
print(*res, sep="\n")


'''
두번째 풀이 - 피라미드인들이 찾은 증명 한번더 적용해볼까? 역시나 틀림 ㅋㅋ
'''
# def solution():
#     answer = []
    
#     while True:
#         tri = list(map(int, input().split()))
#         t_sum = sum(tri)
#         if t_sum == 0:
#             return answer
        
#         prs = True
#         for i in [3,4,5]:
#             n = (t_sum * i) / 2
#             if n not in tri:
#                 answer.append('wrong')
#                 prs = False
#                 break
        
#         if prs:
#             answer.append('right')

# res = solution()
# print(*res, sep="\n")

        



'''
첫번째풀이 - 틀림
'''
# def solution():
#     answer = []
    
#     while True:
#         tri = list(map(int, input().split()))
#         t_sum = sum(tri)
#         if t_sum == 0:
#             return answer
        
#         if t_sum % 3 == 0:
#             answer.append('right')
#         else:
#             answer.append('wrong')

# res = solution()
# print(*res, sep="\n")


