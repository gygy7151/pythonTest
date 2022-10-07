'''
다이어트

경계조건 설정을 위해 A^2 - B^2 = (A-B)(A+B)로 인수분해를 한다.
 이 때, 알 수 있는 경계조건은 두 가지다.
1. A > B : 몸무게는 음수가 아니기 때문에 A > B이다.
2. A + B <= G 여야한다. A - B가 가질 수 있는 최소값은 1이다.
 이 때, A+B가 G보다 커지게 되면, 문제에서 요구하는 숫자가 아니다.
  따라서 A + B <= G이하의 범위만 찾아야 한다.

(현재 몸무게)^2 - (예전 몸무게)^2 = 찐 몸무게

 

1부터 g까지의 모든 수를 배열에 담아두고 투 포인터를 실행했다. end는 현재 몸무게를 가리키는 포인터이고 start는 예전 몸무게를 가리키는 포인터로 설정했다.

 

위 식대로 찐 몸무게를 구한 후 구한 값이 g와 같다면 정답을 담아두는 배열에 삽입한다. 

g보다 작다면? 찐 몸무게를 더 늘려야 하므로 end(현재 몸무게)를 증가

g보다 크거나 같다면? 찐 몸무게를 줄여야 하므로 start(예전 몸무게) 증가
'''
'''
첫번째풀이
'''
def solution():
    G = int(input())
    start = 0
    end = 0
    arr = [ x for x in range(1, G+1)]
    ans = []

    while end < G:
        weight = arr[end] * arr[end] - arr[start] * arr[start]

        if weight == G:
            ans.append(arr[end])
        
        if weight < G:
            end += 1
        else:
            start += 1
    
    if not len(ans):
       print(-1)
    else:
        ans.sort()
        print(*ans, sep="\n")
solution()


