'''
괄호변환
'''
def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        
        elif p[i] == ')':
            right += 1
            
        if left == right:
            return p[:i+1], p[i+1:]
            
def check_right(u):
    new = []
    for wrd in u:
        if wrd == '(':
            new.append(wrd)
        else:
            if not new:
                return False
            new.pop()
    return True

# def change(__u):
#     for idx, i in __u:
#         if i == '(':
#             __u[idx] = ')'
        
#         else:
#             __u[idx] = '('
#     return __u
    

def solution(p):
    if not p:
        return ""
    
    u, v = divide(p)
    
    if check_right(u):
        return u + solution(v)
    
    else :
        answer = '('
        answer += solution(v)
        answer += ')'

        for p in u[1: len(u)-1]:
            if p == '(':
                answer += ')'

            else:
                answer += '('
        
        return answer


#또다른 풀이
# def solution(p):
#     if p=='': return p
#     r=True; c=0
#     for i in range(len(p)):
#         if p[i]=='(': c-=1
#         else: c+=1
#         if c>0: r=False
#         if c==0:
#             if r:
#                 return p[:i+1]+solution(p[i+1:])
#             else:
#                 return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

# .join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) )) 대신 ''.join(['(' if x==')' else ')' for x in p[1:i]]) 도 가능