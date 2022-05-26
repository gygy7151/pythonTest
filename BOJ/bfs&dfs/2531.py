'''
회전초밥
'''
'''
두번째풀이
'''
n, d, k, c = map(int, input().split())
sushies = [int(input())for _ in range(n)]
sushies = sushies + sushies[:k]

s_table = {i+1:0 for i in range(d)}
# 쿠폰값
s_table[c] = 1
answer = -1
# 쿠폰 번호 가짓수 한개 디폴트로 추가
current_number = 1

# 초기 k개값 셋팅
for i in range(k):
    sushi = sushies[i]
    if s_table[sushi] == 0:
        current_number += 1

    s_table[sushi] += 1

for i in range(n):
    # 스시값 빼기
    sushi = sushies[i]
    if s_table[sushi] == 1:
        current_number -= 1
    s_table[sushi] -= 1
    # 스시값 더하기
    sushi = sushies[i+k]
    if s_table[sushi] == 0:
        s_table[sushi] += 1
        current_number += 1
    else:
        s_table[sushi] -= 1
    answer = max(answer, current_number)
print(answer)

'''
첫번째풀이 틀림
'''
# k_cases= []
# coupon_cases = []
# n, d, k, c = map(int, input().split())
# sushies = [int(input()) for _ in range(n)]

# for start_idx, sushi in enumerate(sushies):
#     temp = []
#     for i in range(k):
#         if sushies[(start_idx+i)%n] not in temp:
#             temp.append(sushi)
#         else:
#             break
#     k_cases.append(temp)
# for k_case in k_cases:
#     if c in k_case:
#         continue
#     coupon_cases.append(k_case)
# for i in range(len(k_cases)):
#     k_cases[i] = set(k_cases[i])
# for i in range(len(coupon_cases)):
#     coupon_cases[i] = set(coupon_cases[i])

# k_cases, coupon_cases = sorted(k_cases), sorted(coupon_cases)
# answer = max(len(k_cases[0]), len(coupon_cases[0])+1)
# print(answer)