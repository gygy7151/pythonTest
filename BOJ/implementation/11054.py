'''
가장 긴 바이토닉 부분 수열
'''
'''
두번째풀이 - 세그먼트 트리활용 O(NlogN)
참고자료: https://www.crocus.co.kr/670?category=159837
'''

'''
첫번째풀이- dp활용
참고자료 : https://www.youtube.com/watch?v=sYh62pujaH8
'''
N = int(input())

List = list(map(int, input().split()))

dp1 = [1]*N
dp2 = [1]*N

sub_len=[0]*N

Max=0

for i in range(N):
    for j in range(i):
        if List[i] > List[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

List.reverse()

for i in range(N):
    for j in range(i):
        if List[i]>List[j]:
            dp2[i]=max(dp2[i],dp2[j]+1)

dp2.reverse()

for i in range(N):
    sub_len[i]=dp1[i]+dp2[i]

print(max(sub_len)-1)