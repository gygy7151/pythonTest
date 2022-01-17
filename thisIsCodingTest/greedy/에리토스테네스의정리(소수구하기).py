'''
에리토스테네스의 정리 없이 구현한 코드

'''
'''
n=1000
for i in range(n+1):
  result=True
  if(i<2):
    result = False
  for j in range(2,i):
    if(i%j==0):
      result = False
  if result:
      print(result)
      print(i, end=" ")
'''

'''
에리토스테네스의 체로 구현한 코드
'''

n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)