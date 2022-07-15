'''
패션왕 신해빈
'''
'''
세번째풀이
옷을입는 조합을 구하는게 아닌, 경우의수를 구하는 것이기 때문에
(A+1)(B+1)(C+1)-1 (여기서 -1은 A,B,C중 아무것도 안입은경우를 의미)
위 공식을 대입해 풀면 쉽게 구할 수 있다.
'''
import sys
input = sys.stdin.readline

def solution():
    
    for _ in range(int(input())):
        closet = {}

        for i in range(int(input())):
            i_name, i_category = map(str, input().rsplit())
            try:
                closet[i_category] += 1
            
            except:
                closet[i_category] = 1
        
        i_counts = [ x for x in closet.values() ]
        
        if len(i_counts) == 1:
            print(i_counts[-1])
            continue
        
        ANS = 1
        for count in i_counts:
            ANS *= (count+1)
        print(ANS-1)

solution()
'''
두번째풀이 - 메모리초과
'''
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# def solution():
    
#     for _ in range(int(input())):
#         closet = {}

#         for i in range(int(input())):
#             i_name, i_category = map(str, input().rsplit())
#             try:
#                 closet[i_category] += 1
            
#             except:
#                 closet[i_category] = 1
        
#         i_counts = [ x for x in closet.values() ]
        
#         if len(i_counts) == 1:
#             print(i_counts[-1])
#             continue
        
#         # 기본 한개씩 뽑는경우는 더해주기
#         ANS = sum(i_counts)
        
#         for i in range(1,len(closet)):
#             i_set = list(combinations(i_counts, i+1))
#             i_sum = 0
            
#             for a in i_set:
#                 a_sum = 1
                
#                 for j in range(len(a)):
#                     a_sum *= a[j] 
#                 i_sum += a_sum
            
#             ANS += i_sum

#         print(ANS)            

# solution()


'''
첫번째풀이 - 틀림
'''
# import sys
# input = sys.stdin.readline

# def solution():

#     for _ in range(int(input())):
#         closet = {}

#         for _ in range(int(input())):
#             name, category = map(str, input().rsplit())
#             try:
#                 closet[category] += [name]

#             except:
#                 closet[category] = [name]

#         single, couples = 0, 1

#         if len(closet) == 1:
#             print(len(closet[''.join(list(closet))]))
#             continue

#         for items in closet.values():
#             item_cnt = len(items)
#             single += item_cnt
#             couples *= item_cnt

#         print(single + couples)

# solution()
