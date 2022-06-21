'''
소수구하기 - 소수하나씩
'''
# start, end = map(int, input().split())
# memo = [0,0] + [1] * (end-1)
# primes = []

# for i in range(2, end+1):
#     if memo[i]:
#         primes.append(i)
#         for j in range(2*i, end+1, i):
#             memo[j] = 0

# for k in range(start, end+1):
#     if memo[k]:
#         print(k)

'''
두번째풀이 - 에라토스테네스의 체를 잘못이해하고 활용했다.. -> 역시나 시간초과
'''
'''
합성수로 접근하되 체크하는 배수 범위를 max로 제한했다.
'''
# 소수인 num의 배수를 자기자신을 제외하고 모두 지운다.
def delete(num):
    global memo
    for i in range(num*2,end+1,num):
        memo[i] = 0

    
start, end = map(int, input().split())
# 소수 배수 구할때 맥시멈으로 활용
max_num = 0
while True:
    max_num += 1
    multiple = max_num**2
    if multiple > end:
        break

# 모든 수는 소수가 될 가능성을 디폴트로 깔고감
## 단 범위는 end값 범위까지
memo = [0,0]+ [1] * (end+1)
N = len(memo)

for i in range(2, max_num+1):
    # 소수만 추가
    delete(i)

for i in range(start,end+1):
    if memo[i] == 1:
        print(i)




'''
첫번째풀이 - 시간초과
'''
# start, end = map(int, input().split())
# sn_memo = [1] * (end+2)

# for i in range(2,end+1):
#     for j in range(2, i):
#         if sn_memo[i] != 0:
#             if i % 1 == 0 and i % i == 0:
#                 if i % j != 0:
#                     continue
#                 if i % j == 0:
#                     sn_memo[i] = 0
#                     break
#     # i는 소수이므로 i배수들은 모두 비소수로 처리
#     for k in range(i, end+1, i):
#         if k % i == 0:
#             sn_memo[k] = 0
# # print(sn_memo)

# for i in range(start, end+1):
#     if i == 1:
#         continue
#     if sn_memo[i] == 1:
#         print(i)
