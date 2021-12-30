'''
simple customer support ticketing
'''

set = {'{': '}', '[': ']', '(' : ')'}

# Complete the braces function below.
def braces(values):
    
    strs = values
    arr = []
    option = False

    
    for i in range(len(values)):
      
        strs[i] = list(map(str, values[i]))


    for i in range(len(strs)) :

        for j in range(len(strs[i])) :

            if strs[i][j] == '(' :

                arr.append(')')

            elif strs[i][j] == '[' :

                arr.append(']')

            elif strs[i][j] == '{' :

                arr.append('}')

            else:

                if arr[len(arr) - 1] != strs[i][j]:
                    option = False
                    print('NO')
                    break
                
                
                if arr[len(arr) - 1 ] == strs[i][j]:
                    option = True
                    arr.pop()
        
        if option == True :
            print('YES')


                
                    
            
    

if __name__ == '__main__':

    values_count = int(input())

    values = []

    for _ in range(values_count):
        values_item = input()
        values.append(values_item)
        
    braces(values)



    

