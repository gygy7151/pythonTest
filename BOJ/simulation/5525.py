'''
IOIOI
'''
'''
세번째풀이 - KMP
'''
def makeTable(pattern):
    patternSize = len(pattern)
    table = [0] * patternSize
    j = 0

    for i in range(1, patternSize):
        
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table

def KMP(parent, pattern):
    table = makeTable(pattern)
    parentSize = len(parent)
    patternSize = len(pattern)
    j = 0
    ANS = 0
    for i in range(parentSize):
        
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]
        
        if parent[i] == pattern[j]:
            #모든 문자열이 매칭이 된경우
            if j == patternSize -1:
                ANS += 1
                j = table[j]
                #만약 몇번째에서 매칭이 되는지 알고싶다면?
                #print(i-patterSize+2)
            else:
                #단순히 매칭만 이루어진 경우이기때무에 j를 1씩 증가시켜주면됨
                j += 1
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