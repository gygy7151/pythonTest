'''
찾기
'''
'''
두번째풀이
'''
'''
pattern 길이가 1일때 예외처리 추가
pattern이 text보다 더 길면 이때는 0을 리턴하는 예외처리 추가
아..text받을때 굳이 빈문자열을 .으로 바꿀필요없었다.
패턴에서도 빈문자열이 존재하기 때문..
'''
def makeTable(p):
    patternSize = len(p)
    table = [0] * patternSize

    if patternSize == 1:
        return table
    j = 0
    # 1부터 시작해야됨
    for i in range(1, patternSize):

        while j > 0 and p[i] != p[j]:
            j = table[j-1]

        if p[i] == p[j]:
            j += 1
            table[i] = j

    return table

def solution():
    T = input()
    P = input()
    textSize = len(T)
    patternSize = len(P)
    table = makeTable(P)
    ANS = 0
    pos = []
    j = 0

    if textSize < patternSize:
        print(0)
        print(*pos)
        return 

    for i in range(textSize):

        while j > 0 and T[i] != P[j]:
            j = table[j-1]

        if T[i] == P[j]:
            if j == patternSize -1:
                ANS += 1
                j = table[j]
                pos.append(i-patternSize+2) # 1번째부터 시작하므로 +1 더해서 +2로해주어야됨

            else:
                j += 1


    print(ANS)
    print(*pos)

solution()

'''
첫번째풀이 - 틀림. 띄어쓰기도 문자로 받도록 input()그대로 받았어야 했음
'''
def makeTable(p):
    patternSize = len(p)
    table = [0] * patternSize

    if patternSize == 1:
        return table
    j = 0
    # 1부터 시작해야됨
    for i in range(1, patternSize):

        while j > 0 and p[i] != p[j]:
            j = table[j-1]

        if p[i] == p[j]:
            j += 1
            table[i] = j

    return table

def solution():
    T = input()
    P = input()
    print(T)
    textSize = len(T)
    patternSize = len(P)
    table = makeTable(P)
    
    ANS = 0
    pos = []
    
    j = 0

    for i in range(textSize):

        while j > 0 and T[i] != P[j]:
            j = table[j-1]

        if T[i] == P[j]:
            if j == patternSize -1:
                ANS += 1
                j = table[j]
                pos.append(i-patternSize+2) # 1번째부터 시작하므로 +1 더해서 +2로해주어야됨

            else:
                j += 1


    print(ANS)
    print(*pos)

solution()