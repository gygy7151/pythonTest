'''
문자열집합
'''
n, m = map(int, input().split())
S = {}
for _ in range(n):
    str = input()
    if str in S:
        continue
    S[str] = 0
for _ in range(m):
    str = input()
    if str not in S:
        continue
    S[str] += 1
str_counts = list(S.values())
answer = sum(str_counts)
print(answer)