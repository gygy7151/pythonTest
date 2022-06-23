'''
N: 주어지는 숫자
한수 : 양의 정수 X의 각 자리가 등차수열을 이루면 그 수를 한수라고 정의 (1 <= 한수 <= N)
'''
def solution():
    cnt = 0

    for n in range(1, int(input())+1):
        N = list(str(n))
        length = len(N)
        if length == 1:
            cnt+= 1
            continue
        diff = int(N[0]) - int(N[1])

        res = True
        for i in range(1,length-1):

            if diff != (int(N[i]) - int(N[i+1])):
                res = False
                break

            else:
                diff = int(N[i]) - int(N[i+1])
        if res:
            cnt += 1
         


    return cnt

print(solution())



