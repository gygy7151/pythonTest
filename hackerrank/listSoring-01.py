'''
simple customer support ticketing
'''

open = ['{', '[', '(']
set = { '}' : '{', ']' : '[', ')' : '(' }

# Complete the braces function below.
def braces(values):
    
    strs = values
    
    for i in range(len(values)):
      
        strs[i] = list(map(str, values[i]))

    for i in range(len(strs)) :
      
        for j in range(len(strs[i])) :
            

            if strs[i][j] == '{' or strs[i][j] == '[' or values[i][j] == '(':
                print('지나간다')
                pass
            
            else :
                if strs[i][j-1] == set[strs[i][j]] :
                    print('같다')
                    pass

                    if j == len(strs[i]) - 1 :
                        print('YES')

                elif strs[i][j-1] != set[strs[i][j]] :
                    
                    print('NO')
                    
                    break
                
                
                    

    
                    
            
    

if __name__ == '__main__':

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)
        
    braces(values)



    

