'''
IOIOI
'''
'''
세번째풀이 - KMP....드뎌정복
'''
def makeTable(pattern):
    patternSize = len(pattern)
    table = [0] * patternSize
    j = 0

    for i in range(1, patternSize):
        
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        
        if pattern[i] == pattern[j]:
            #어차피 i는 자연스럽게 +1이되고 j에만 +1해주면됨
            #그리고 i는 +1되기전에 일치하는 인덱스위치에세 j를 대입해주면됨(반드시 1이더해지고 대입해줘야됨)
            j += 1
            table[i] = j

    return table

def KMP(parent, pattern):
    table = makeTable(pattern)
    parentSize = len(parent)
    patternSize = len(pattern)
    j = 0
    ANS = 0
    # O(N)
    for i in range(parentSize):
        
        #parent하고 pattern을 각각 비교해주는 거임
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]
        
        if parent[i] == pattern[j]:
            #모든 문자열이 매칭이 된경우
            #비교패턴사이즈만큼 모두 매칭이 된 경우
            if j == patternSize -1:
                ANS += 1
                #아..table값은 j부터 해당패턴과 다른 값 시작인덱스를 의미함
                j = table[j]
                #만약 몇번째에서 매칭이 되는지 알고싶다면?
                #print(i-patterSize+2)
            else:
                #단순히 매칭만 이루어진 경우이기때무에 j를 1씩 증가시켜주면됨
                j += 1
    
    #만약 ANS가 0이면 return -1해서 실패를 알려줄 수도 있겠지?
    return ANS

def solution():
    N = int(input())
    M = int(input())
    A = 'I' + 'OI'* N
    S = input()
    print(KMP(S, A))

solution()



'''
두번째풀이 - 아..이것도 50점임..엄청 큰숫자는 안됨..
'''
# def hashing(s):
#     r = 31
#     m = 1234567891
#     return sum((ord(c)-96)*r**i%m for i, c in enumerate(s)) % m

# def solution():
#     N = int(input())
#     M = int(input())
    
#     A = 'I' + ('OI'* N)
#     B = input()
    
#     #비교용도
#     hashA = hashing(A)
    
#     ANS = 0
#     for i in range(M):
#         hashB = hashing(B[i:i+(2*N+1)])
#         if hashA == hashB:
#             ANS += 1

#     return ANS

# print(solution())

'''
첫번째풀이
'''
# def solution():
#     N = int(input())
#     IO = 'I' + ('OI'*N)
    
#     M = int(input())
#     S = input()

#     answer = 0
#     for i in range(M-(2*N)):
#         if IO == S[i:i+(2*N+1)]:
#             answer += 1

#     return answer
# print(solution())