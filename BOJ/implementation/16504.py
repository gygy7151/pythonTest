'''
종이접기
'''
'''
첫번째풀이
'''
def solution():
    answer = 0
    for _ in range(int(input())):
        answer += sum(list(map(int, input().split())))
    
    print(answer)
solution()
