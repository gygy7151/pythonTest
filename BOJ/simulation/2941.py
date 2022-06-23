'''
크로아티아 알파벳
'''
def solution(S):
    ans = 0
    prototype = [
        'c=',
        'c-',
        'dz=',
        'd-',
        'lj',
        'nj',
        's=',
        'z='
        ]
    # 목록문자요소 먼저 카운팅 및 삭제
    for i in range(len(prototype)):
        if S.count(prototype[i]):
            ans += (S.count(prototype[i]))
            # S = S.replace(alpha,'*')
            S = S.replace(prototype[i],'*')
            # table = S.maketrans(prototype[i],'**')
            # S = S.translate(table)
            # print(S)
    # 목록외 문자요소 중복제거하면 안됨
    S = S.replace('*','')
    # print(S)
    ans += (len(S))
    # table = s.maketrans('i-','**')
    # s = s.translate(table)
    # res = s.count('i-')
    # for _ in range(res):
    return ans
S = input()
print(solution(S))
