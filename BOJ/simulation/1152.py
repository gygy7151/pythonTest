'''
단어의 개수
'''
# 단어 공백 단어 -> 공백1개당 단어2개 예상가능
# 그런데양쪽에도 공백 존재 가능하다 했으므로 아래와 같이 경우의수 4가지 존재 
# 아.. 빈 문자열도 카운팅해야 했음
test = tuple(input().split())

print(len(test))

# def result(cnt):
#     res = 0
#     res = cnt * 2
#     print(res)

# if cnt == 2:
#     if test[0] == '\'' and test[1] == '\'':
#         print(0)
# # 맨앞에만 공백이 존재하는 경우 -> 만약 공백 2  - 1
# elif test[0] == '\'' and test[-1] != '\'':
#     cnt -= 1
#     result(cnt)

# # 맨뒤에만 공백이 존재하는 경우 -> 만약 공백 2  - 1
# elif test[0] != '\'' and test[-1] == '\'':
#     cnt -= 1
#     result(cnt)

# # 양옆에 모두 공백이 존재하는 경우 -> 만약 공백 2  - 2
# elif test[0] == '\'' and test[1] == '\'':
#     cnt -= 2
#     result(cnt)

# # 양옆에 모두 공백이 존재하지 않는 경우 -> 그대로
# elif test[0] != '\'' and test[1] != '\'':
#     result(cnt)

