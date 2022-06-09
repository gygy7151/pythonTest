'''
사분면고르기
'''
pos = []
for i in range(2):
    pos.append(int(input()))

# y, x가 아님. 반드시 주어진 조건대로 변수 할당
x, y = pos[0], pos[1]

if x > 0 and y > 0:
    print(1)

elif x < 0 and y > 0:
    print(2)

elif x < 0 and y < 0:
    print(3)

else:
    print(4)