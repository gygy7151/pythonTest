'''
점화식 - 13699
'''
n = int(input())
t = [0] * (n+1)
t[0] = 1
for i in range(1, n+1):
    temp = 0
    for j in range(i):
        temp += (t[j]*t[i-1-j])
    t[i] = temp
print(t[n])

    