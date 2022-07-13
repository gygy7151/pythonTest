'''
문자열내마음대로정렬하기
'''
'''
두번째풀이
'''
def solution(strings,n):
    return sorted(sorted(strings), key=lambda x: x[n])


'''
첫번째/두번째풀이 - 인덱스는 n으로 바뀌는걸 놓침. 해당부분 수정반영함
'''
def solution(strings, n):
    answer = []
    TEMP = []
    for s in strings:
        # s[1] -> s[n]으로 코드수정
        TEMP.append((s[n], s))

    TEMP.sort(key=lambda x : (x[0], x[1]))
    # print(TEMP)
    for index_1, word in TEMP:
        answer.append(word) 
    return answer