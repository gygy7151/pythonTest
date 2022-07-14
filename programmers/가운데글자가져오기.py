'''
가운데글자가져오기
'''
'''
두번째풀이
'''
def solution(s):
    #어차피 n-1 n 까지 포함하므로 그렇게 되는구만
    #홀수일때든 짝수일때는 -1해서 //2해주면 값이 똑같이 나오는걸 알게되었다.
    #끝부분도 마찬가지..
    return s[(len(s)-1)//2:len(s)//2+1]

'''
첫번째풀이
'''
def solution(s):
    N = len(s)//2
    return s[N] if len(s) % 2 else s[N-1:N+1]