
'''
k번째수
'''
'''
두번째풀이
'''

2
3
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

'''
첫번째풀이
'''
def solution(array, commands):
    answer = []
    #와 이걸 map으로 구현하면 i는 x[0], j는 x[1], k는 x[2]가 되는구나 히야..
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer