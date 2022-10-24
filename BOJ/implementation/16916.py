'''
부분문자열- P와 S가 주어질때 P가 S의 부분 문자열인지 판단하여 결과 반환하는 문제임
'''
'''
첫번째풀이
KMP 알고리즘을 이해하고 구현하면 쉬움
'''
def solution():
    s = input()
    p = input()
    
    def make_table():
        length = len(p)
        table = [0] * len(p)
        j = 0

        for i in range(1, length):
            while j > 0 and p[i] != p[j]:
                j = table[j-1]
            
            if p[i] == p[j]:
                j += 1
                table[i] = j

        return table
    
    def kmp():
        table = make_table()
        j = 0

        for i in range(len(s)):
            while j > 0 and s[i] != p[j]:
                j = table[j-1]
            
            if s[i] == p[j]:
                if j == len(p)-1:
                    return True
                
                else:
                    j += 1

        return False

    
    print(1 if kmp() else 0)
solution()


