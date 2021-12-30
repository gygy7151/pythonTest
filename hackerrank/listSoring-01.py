'''
simple custommer support ticketing
'''

open = ['{', '[', '(']
set = { '}' : '{', ']' : ']', ')' : '(' }

# Complete the braces function below.
def braces(values):
    
    strs = values
    print(strs)
    
    for i in range(len(values)):
        strs[i] = list(map(str, values[i]))
    
    
    for i in range(len(strs)) :
        for j in range(len(strs[i])) :
            print(strs[i][j])
            if strs[i][j] == '{' or strs[i][j] == '[' or strs[i][j] == '(':
                pass
            
            else :
                try :
                    print(set[strs[i][j]])
                    print(strs[i][j-1])
                    if set[strs[i][j]] == strs[i][j-1] :
                        print('YES')
                        strs[i][j] = strs[i][j-2]
                    
                except ValueError:
                    print('NO')
                    strs[i][j] = strs[i][j-2]

    
                    
            
    

if __name__ == '__main__':

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)
        
    braces(values)

    

