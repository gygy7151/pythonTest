'''
전자레인지
'''
'''
첫번째풀이
'''
def solution():
    A, B, C, D, E = int(input()), int(input()), int(input()), int(input()), int(input())
    
    if A < 0:
        return (-(A)*C )+ D + (B*E)
    
    else:
        return (B-A) *E
print(solution())

