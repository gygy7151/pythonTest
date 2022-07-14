'''
시저암호
'''
'''
세번째풀이 - 두번째와 첫번째나의 풀이를 믹스
'''
def solution(s,n):
    answer = ''
    
    for i in s:

        if i:
            if i >= 'A' and i <= 'Z':
                answer += chr((ord(s[i]) - ord('A') + n) % 26 + ord('A') )

            elif i >= 'a' and i <= 'z':
                answer += chr((ord(s[i]) - ord('a') + n) % 26 + ord('a') )
            
            else:
                answer += ' '
    
    return answer

'''
두번째풀이 - ord() -숫자반환, chr() - 문자반환 상당히 간편하고 편함
'''
def solution(s,n):
    s = list(s)
    
    for i in range(len(s)):
        
        if s[i].isupper():
            s[i] = chr( (ord(s[i]) - ord('A') + n) % 26 + ord('A') )
        
        elif s[i].islower():
            s[i] = chr ( (ord(s[i]) - ord['a'] + n) % 26 + ord['a'] )
    
    return ''.join(s)
print(solution())

'''
첫번째풀이 - 너무고생이다..
'''
# ALPHA = {
#     1: 'A',
#     2: 'B',
#     3: 'C',
#     4: 'D',
#     5: 'E',
#     6: 'F',
#     7: 'G',
#     8: 'H',
#     9: 'I',
#     10:'J',
#     11:'K',
#     12:'L',
#     13:'M',
#     14:'N',
#     15:'O',
#     16:'P',
#     17:'Q',
#     18:'R',
#     19:'S',
#     20:'T',
#     21:'U',
#     22:'V',
#     23:'W',
#     24:'X',
#     25:'Y',
#     26:'Z' 
# }
# ALPHA_NUM = {
#     'A':1,
#     'B':2,
#     'C':3,
#     'D':4,
#     'E':5,
#     'F':6,
#     'G':7,
#     'H':8,
#     'I':9,
#     'J':10,
#     'K':11,
#     'L':12,
#     'M':13,
#     'N':14,
#     'O':15,
#     'P':16,
#     'Q':17,
#     'R':18,
#     'S':19,
#     'T':20,
#     'U':21,
#     'V':22,
#     'W':23,
#     'X':24,
#     'Y':25,
#     'Z':26
# }
# def solution(s, n):
#     answer = ''
#     TEMP = list(s)
#     for idx, char in enumerate(TEMP):
#         if char != ' ':
#             TEMP[idx] = (ALPHA_NUM[char.upper()] + n) % 26
#             if (ALPHA_NUM[char.upper()] + n) % 26 == 0:
#                 TEMP[idx] = 26

#     for idx, num in enumerate(TEMP):
#         if num != ' ':
#             # 소문자치환
#             if s[idx] != s[idx].lower():
#                 TEMP[idx] = ALPHA[num]

#             else:
#                 TEMP[idx] = ALPHA[num].lower()

#     answer = "".join(TEMP) 
#     return answer