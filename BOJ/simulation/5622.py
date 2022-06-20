'''
다이얼
'''
'''
두번째풀이
'''
time = {3:["A","B","C"], 4:["D","E","F"], 5:["G","H","I"],6:["J","K","L"],
        7:["M","N","O"], 8:["P","Q","R","S"],9:["T","U","V"], 10:["W","X","Y","Z"]}
word = input()
ans = 0
for i in word:
    for k, v in time.items():
        if i in v :
            ans += k
print(ans)


'''
첫번째풀이 - 통과 but 자료구조 비효율적 확장성이 낮음. 굳이 데이터수가 작으면 효율성 안고려해도 괜찮음.
'''
# dial_num = {
#     'A':2, 'B':2, 'C':2,
#     'D':3, 'E':3, 'F':3,
#     'G':4, 'H':4, 'I':4,
#     'J':5, 'K':5, 'L':5,
#     'M':6, 'N':6, 'O':6,
#     'P':7, 'Q':7, 'R':7, 'S':7,
#     'T':8, 'U':8, 'V':8,
#     'W':9, 'X':9, 'Y':9, 'Z':9
#     }

# str = list(input())
# time = [11] + [ x for x in range(2,11)]
# ans = 0

# for char in str:
#     ans += time[dial_num[char]]

# print(ans)

