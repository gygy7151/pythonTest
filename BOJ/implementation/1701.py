'''
Cubeditor 부분문자열이 두번이상 중복되는것 중 젤 긴거 찾는 문제
'''
'''
첫번째풀이
기존 기능은 찾는 문자열이 단한번만 나오면 okay였다.
근데 신규 기능은 어떤 문자열내에서 부분 문자열이 두번 이상 나오는 문자열을 찾는 기능이다.
이때 두 부분 문자열은 겹쳐도 된다.
이런 문자열 중 가장 길이가 긴 것을 구하는 프로그램을 작성하시오
부분 문자열은 한개에서부터 절반까지길이임
'''
def solution():
    s = input()

    def check(pattern):
        length = len(pattern)
        table = [0] * len(pattern)
        j = 0
        for i in range(1, length):
            while j > 0 and pattern[i] != pattern[j]:
                j = table[j - 1]
            
            if pattern[i] == pattern[j]:
                j += 1
                table[i] = j
        
        return max(table)

    result = 0

    for idx in range(len(s)):
        sub_str = s[idx:len(s)]
        result = max(result, check(sub_str))
    
    print(result)
solution()


