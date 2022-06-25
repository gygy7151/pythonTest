'''
나이순 정렬
''' 
'''
첫번째 풀이 - 맞긴했으나 시간이 너무 오래걸림. 병합정렬을 이용해 두번째풀이 추후 시도 필요
'''
def solution():
    members = []

    for i in range(int(input())):
        age, name = map(str, input().split())
        members.append((int(age), i, name))

    members.sort(key= lambda x: (x[0], x[1]))

    #members 0번째: age, 2번째: name
    for info in members:
        print(info[0], info[2], sep = " ")

solution()




