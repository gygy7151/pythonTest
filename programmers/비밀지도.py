'''
비밀지도
'''
'''
두번째풀이 - 훨씬 간략해지고 새로운 메서드들을 사용했음
zfill(width): 스트링앞에 0을 채워줌. 따로 리턴하는 객체는 없음
rjust(width,[fillchar]): '2'.rjust(3, '0')
 // '002'처럼 됨. 문자열 앞에 채워주고 싶은 문자 지정가능하며 길이도 지정가능함
'''
def solution(n, arr1, arr2):
    answer = []
    
    for x, y in zip(arr1, arr2):
        S = bin(x|y)[2:].rjust(n, '0')
        S = S.replace('0', ' ')
        S = S.replace('1', '#')
        answer.append(S)
 
    return answer

'''
첫번째풀이 - 한땀한땀 접근했음
이진법 변환 방법을 몰라 인터넷 검색했음

우선 이진법(binary), 팔진법(octal decimal), 십육진법(hexadecimal)
사실 이진법이나 십육진법이 젤 많이 쓰임
십지수를 바로 해당 진법수로 리턴하는 방법 
2진법: bin()
8진법: oct()
16진법: hex()
참고로 str(0b101010) // '42'가됨

다른진수의 문자열을 십진수로 변환하기 -> 숫자를 리턴함
int('0b101010, 2) // 42
int('0o52, 8)  // 42
int('0x2a', 16) // 42
사실 int()함수의 2번째 인자는 디폴트값이 10이기 때문에 생략했을경우 10진수의 문자열이 숫자로 변환되는것

추가로 format() 내장함수를 이용하면 십진수를 다른 진수의 문자열로 바꿀때 접두어를 제외할 수 있음
2진법 : format(42, 'b') // '101010'
8진법 : format(42, 'o') // '52'
16진법 : format(42, 'x') // '2a'
#대문자변환도 가능함
16진법 : format(42, 'X') // '2A'

접두어를 포함시키고 싶으면? #b, #o, #x, #X 해주면됨

#십진수를 한꺼번에 여러 진법의 문자열로 변환하고 싶으면?
"int: {0:d}, bin: {0:b}, hex: {0:x}".format(42)


'''
def solution(n, arr1, arr2):
    answer = []
    MAPA, MAPB = [], []

    for a, b in zip(arr1, arr2):
        A = format(a, 'b')
        B = format(b, 'b')
        MA, MB = [], []
        # 상당히 비효율적임.  rjust(n, '0') 또는 zfill(n)해주면 쉬움 코드가 5배가량 차이남
        if len(A) != n:
            TA = ''.join(map(str, [0]*(len(A) - n)))
            A = TA + A

        if len(B) != n:
            TB = ''.join(map(str, [0]*(len(B) - n)))
            B = TA + B
        
        for a in A:
            if a == '0':
                MA.append(' ')

            else:
                MA.append('#')

        for b in B:
            if b == '0':
                MB.append(' ')
            else:
                MB.append('#')

        MAPA.append(MA)
        MAPB.append(MB)
    
    MC = []
    #귀찮아서 그냥 zip사용함. 이전에 더 길었음
    for a, b in zip(MAPA, MAPB):
        if a == ' ' and b == ' ':
            MC.append(' ')
        else:
            MC.append('#')
        
        #이때도 처음엔 리스트를 담았는데 출력조건은 리스트가 아닌 스트링 문자열이었음
        # answer.append(MC)
        answer.append(''.join(MC))
        
    return answer