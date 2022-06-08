'''
하얀칸
'''
white_pone_num = 0
cnt = 4

while cnt > 0:

    for i in [1,2]:
        board = list(map(str, input().rstrip()))
        if i == 1:
            for i in range(0,7,2):
                if board[i] == 'F':
                    white_pone_num += 1
        else:
            for i in range(1,8,2):
                if board[i] == 'F':
                    white_pone_num += 1
    cnt -= 1

print(white_pone_num)


