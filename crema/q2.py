'''
num = input()
val_digit = str(num)
val_standard = str(num)
min_digit = '0'
max_digit = '0'
min_val = '0'
max_val = '0'


[치환조건]
1. min_digit, max_digit를 숫자에서 찾는다. -> 여기서 
 -> for index, digit in enumerate(val) :
        # digit 타입체크 필수 -> 반드시 int형이어야됨
        # min_digit의 경우
        0아니여야되고.. 1도아니여야 되고, 2부터임 
        min_digit = min(min_digit, digit)
        max_digit = max(min_digit, digit)
        #max digit은 1이거나 min_digit보단 커야됨


        if val[0] != '1' :
            print('index가 0입니다')
            pass

        else :
            print('index가 0이 아닙니다')

            if digit == '1' and index == 0:
                max_digit = digit

            elif digit != '1' :
                if index >= 0 :
                    prev = val[index]
                    after = val[index + 1]
                    
                    if int(prev) < int(after) :
                        min_digit = 

현재값선언
다음값선언
최소자리수
최대자리수
최댓값
최솟값
차

#for index in range(len(val)) :

    인덱스가 0일때// len(val)-2 이하일때 //이건 range가 아니닌깐 -2하는게 맞음 단순한 인덱스이므로

        digit이 1이면

            최대자리수는 1
    
            만약 현재값이 다음값보다 작으면
                최소자리수는 다음값이 될 확률이 높으므로
                최소자리수 = val[다음값 인덱스]
                #limit = index 

                if val[다음값인덱스] < val[다음값 인덱스 +1]:
                    break:


            만약 현재값이 다음값보다 크거나 같으면,
                val[다음값 인덱스] = 현재값

            만약 현재값이 다음값과 같으면,
                pass

        digit이 1이 아니면
    
            만약 현재값이 다음값보다 작으면
                최소자리수는 다음값이 될 확률이 높으므로
                최소자리수 = val[다음값 인덱스]
                #limit = index 


            만약 현재값이 다음값보다 크면,
                val[다음값 인덱스] = 현재값

            만약 현재값이 다음값과 같으면,
                pass
    
    인덱스가 0보다 크거나 limit_idx 작거나
        digit이 1이면

            최대자리수는 1
    
            만약 현재값이 다음값보다 작으면
                최소자리수는 현재값이되고
                val[다음값 인덱스] = 현재값
                limit = index 


            만약 현재값이 다음값보다 크면,
                pass

        digit이 1이 아니면

            만약 현재값이 다음값보다 작으면
                최솟값은 현재값이되고
                val[다음값 인덱스] = 현재값
                limit = index 

            만약 현재값이 다음값보다 크면,
                pass
    


    인덱스가 limit_idx와 같거나 크거나 len(val)-2 이하일때


최대 자리수가 1이면
    최댓값은 val_final.replace('1','9')
    최솟값은 val_final.replace(min_digit, '0')

최대 자리수가 1이 아니면
    최솟값은 val_final.replace(min_digit, '0')
    
    limit_idx = limit +  1
    
    for i in range(limit_idx, len(val) - 1) : 

            만약 현재값이 다음값보다 작으면
                최대자리수는 다음값이되니깐 그냥
                pass

            만약 현재값이 다음값보다 크면,
                최대자리수는 현재값이 되고
                val[다음값 인덱스] = val[현재값인덱스]
    
    최댓값은 val_final.replace('max_digit','9')

difference = int(max_val) - int(min_val)
result = long(difference)

return result

'''


def findRange(num) :

    print(num)

    val = str(num)
    val_test = str(num)
    min_digit = '0'
    max_digit = '0'
    min_val = '0'
    max_val = '0'
    limit_idx = 0

    for index, digit in enumerate(val_test) :

        print(index, digit)

        if index == 0 :

            if digit == '1' :
                
                max_digit = '1'
                print(max_digit, 'max_digit 변경완료')

                if digit < val_test[index + 1] :

                    min_digit = val_test[index]
                    print(min_digit, 'min_digit 변경완료')
                    #이건 replace가 되어야됨
                    val_test.replace(val_test[index +1], digit, 1)
                    limit_idx = index + 1
                    print(limit_idx, 'limit 인덱스 변경완료')
                
                elif digit > val_test[index + 1] :
                    print('')
                    pass
            
            elif digit != '1' :
                
                if digit < val_test[index + 1] :

                    min_digit = val_test[index]
                    #애도 replace가 되어야됨
                    val_test.replace(val_test[index +1], digit, 1)
                    #val_test[index + 1] = val_test[index] 
                    limit_idx = index + 1
                
                elif digit > val_test[index + 1] :
                    pass
        

        elif index >= limit_idx and index <= (len(val_test) - 2):
            
            if digit < val_test[index + 1] :
                pass
                
            elif digit > val_test[index + 1] :
                
                max_digit = val_test[index]
                #애도 replace가 되어야됨
                val_test.replace(val_test[index +1], digit, 1)

    
    if max_digit == '1' :

        max_val = val.replace('1', '9')
        min_val = val.replace(min_digit, '0')

    elif max_digit != '1' :

        min_val = val.replace(min_digit, '0')
        max_val = val.replace(max_digit, '9')

    difference = int(max_val) - int(min_val)

    return difference




if __name__ == '__main__':

    num = int(input().strip())

    result = findRange(num)
    print(result)


