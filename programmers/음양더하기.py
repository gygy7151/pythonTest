'''
음양더하기
'''
'''
두번째 풀이
'''
def solution(absolutes, signs):
    return sum([x if y else -x for x, y in zip(absolutes,signs)])

'''
첫번째 풀이
'''
# def solution(absolutes, signs):
#     answer = 0
#     for x, y in zip(absolutes, signs):
#         if y:
#             answer += x
#         else:
#             answer -= x
        
#     return answer