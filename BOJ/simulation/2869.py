'''
달팽이는 올라가고 싶다.
'''
'''
네번째풀이,다섯번째풀이 - 맨마지막 케이스를 고려해 D에 +1할때랑 안할때 차이 존재 반영 - python 통과
'''
def solution():
    A,B,V = map(int, input().split())
    D = 0
    if (V-B) % (A-B):
        # 나머지있다 == A가 남아있다.(만약 V-B를 안했다면 이렇게 판단할 수 없을꺼임. 왜? A도 고려해야하기 때문) B를 더 빼줘야된다는 뜻 == +1일이된다.
        D = (V-B)//(A-B)+1
    else:
        # 딱 나누어떨어진다. = 더빼줘야할게 없다. == 몫이 총 걸리는 요일이됨
        D = (V-B)//(A-B)
    return D
print(solution())
       
'''
세번째풀이 - 시간초과뜸
'''
# def solution():
#     A,B,V = map(int, input().split())
#     for i in range(1,500000002):
        
#         if (V - A) > 0:
#             V -= A
#         else:
#             return i
#         V += B
# print(solution())

'''
두번째풀이 - 낮과밤 구분해서 계산- 시간초과뜸
'''
# def solution():
#     A,B,V = map(int, input().split())
#     D = 0
#     ANS = 0
#     while ANS < V:
#         D += 1
#         ANS += A
#         if ANS >= V :
#             break
#         ANS -= B
#         if ANS > V :
#             break
#     return D
# print(solution())
'''
첫번째 풀이 - 낮과밤을 구분안하고 무조건 낮과밤을 포함해서 계산했더니 틀림
'''
# def solution():
#     A,B,V = map(int, input().split())
#     D = 1
#     while True:
#         if D*(A-B) >= V:
#             break
#         else:
#             D += 1
#     return D
# print(solution())
    

