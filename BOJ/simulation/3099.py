'''
네번째점
'''
'''
첫번째풀이
'''
def solution():
    x1 = []
    y1 = []

    for _ in range(3):
        x, y = map(int, input().split())
        x1.append(x)
        y1.append(y)
    
    x2, y2 = 0, 0
    for i in range(3):
        if x1.count(x1[i]) == 1:
            x2 = x1[i]
        
        if y1.count(y1[i]) == 1:
            y2 = y1[i]
    
    print('{} {}'.format(x2, y2))
solution()
        

        
                        
        


