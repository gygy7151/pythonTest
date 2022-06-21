'''
오븐 시계
'''
# 주어진 시각
now_h, now_m= map(int, input().split())

# 조리 시간
m_for_cooking = int(input())

# 더해주어야 할 시각
add_h = m_for_cooking // 60
add_m = m_for_cooking % 60
# print(add_h, add_m)

# 종료시각 초기화
new_h, new_m = 0, 0
# 종료시
if now_h + add_h >= 24:
    new_h = (now_h + add_h) % 24
else:
    new_h = now_h + add_h

# 종료분
if now_m + add_m >= 60:
    new_m = (now_m + add_m) % 60
    new_h += 1

else:
    new_m = now_m + add_m

if new_h == 24:
    new_h = 0

if new_m == 60:
    new_m = 0

print(new_h, new_m, sep=" ")

