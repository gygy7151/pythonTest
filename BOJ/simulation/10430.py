'''
나머지
'''
#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
A, B, C = map(int, input().split())
res1 = (A+B)%C
res2 = ((A%C) + (B%C)) % C
res3 = (A*B)%C
res4 = ((A%C) * (B%C))%C
print(res1)
print(res2)
print(res3)
print(res4)