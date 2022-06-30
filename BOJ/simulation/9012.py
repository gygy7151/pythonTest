'''
괄호
'''
def solution():
    
    # 여기선 sys.stdin.readline으로 한꺼번에 받아오면 안됨.. 중간개행문자때문에 출력에러생김
    for _ in range(int(input())):
        arr = input()
        Q = []
        pairing = True
        for pair in arr:
            
            if len(Q) < 1:
                Q.append(pair)
                continue
                
            if pair == '(':
                
                if Q[-1] == '(':
                    Q.append('(')
                
                else:
                    # ** 이걸 개별만 보고 순서를 못봤다.')(' 이건 VPS아님
                    Q.append(')')
                    pairing = False
                    break
                
            # pair == ')'
            else:
                
                if Q[-1] == '(':
                    Q.pop()
                else:
                    Q.append(')')
                    pairing = False
                    break
        
        if len(Q) == 0 and pairing == True:
            print('YES')
        else:
            print('NO')
solution()