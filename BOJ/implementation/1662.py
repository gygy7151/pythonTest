'''
압축
'''
'''
첫번째풀이
'''
'''
K는 한자리 정수이고
Q는 0자리 이상의 문자열
K(K(K(Q)))
Q라는 문자열이 K번 반복되는 거임
아.. 
와 이거 되게 어렵다..
'''
def solution():
    S = input()
    stack =[]
    length = 0
    K = ''

    for char in S:
        if char.isdigit():
            length += 1
            K = char # 가장 최근의 반복되는 수
        
        elif char == '(':
            # K는 곱해야 하는 수, length-1은 (를 만나기 전까지의 전체길이
            stack.append((K, length-1))

        else:
            # )일때, 곱해야하는 수 multi, '('이전부터 multi 전까지의 길이 preL
            # ( ) 사이에 있는 문자길이 length
            multi, preL = stack.pop()

            length = (int(multi) * length) + preL

    print(length)
solution()

    

