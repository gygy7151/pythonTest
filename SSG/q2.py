'''
log의 원소구성순서 : 수험번호 / 문제번호 / 점수
'''
logs = ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]

'''
두번째풀이
'''
def solution(logs):
    answer = []
    # 응시자 점수비교 함수
    def compare(index, a_nums):
        A = appliers_score[a_nums]
        a_solved_probs = [x for x in A if x != -1]
        for b_nums in appliers[index+1:]:
            B = appliers_score[b_nums]
            b_solved_probs = [x for x in B if x != -1]
            if len(a_solved_probs) >= 5 and len(b_solved_probs) >= 5 and len(a_solved_probs) == len(b_solved_probs):
                for i in range(len(A)):
                    if A[i] != B[i]:
                        continue
                if a_nums not in answer:
                    answer.append(a_nums)
                if b_nums not in answer:
                    answer.append(b_nums)
                    
    appliers_score = {}
    # 응시자 점수 저장
    for log in logs:
        applied_nums, prob_num, score = map(str, log.split())
        if applied_nums not in appliers_score:
            appliers_score[applied_nums] = [0] * 101
            appliers_score[applied_nums][int(prob_num)] = int(score)
        else:
            appliers_score[applied_nums][int(prob_num)] = int(score)
    # 응시자 명단 뽑기
    appliers = list(appliers_score.keys())
    # 비교대조군 문항 및 점수 일치 확인
    n = len(appliers)
    for i in range(n):
        compare(i, appliers[i])
    # 사전순 정렬
    if len(answer) == 0:
        answer.append("None")
    else:
        answer = sorted(answer)
    return answer
res = solution(logs)
print(res)
'''
첫번째풀이
'''
# answer = []
# def compare(index, a_nums):
#     # print('비교시작')
#     global answer
#     A = appliers_score[a_nums]
#     a_solved_probs = [x for x in A if x != 0]
#     print(a_solved_probs)
#     for b_nums in appliers[index+1:]:
#         # print(b_nums)
#         B = appliers_score[b_nums]
#         b_solved_probs = [x for x in B if x != 0]
#         # print(b_solved_probs)
#         if len(a_solved_probs) >= 5 and len(b_solved_probs) >= 5 and len(a_solved_probs) == len(b_solved_probs):
#             # print('안커?')
#             for idx, a_score in enumerate(A):
#                 if B[idx] != a_score:
#                     continue
#             if a_nums not in answer:
#                 # print('a_nums 들어갔당')
#                 answer.append(a_nums)
#             if b_nums not in answer:
#                 # print('b_nums 들어갔당')
#                 answer.append(b_nums)
#     print('비교끝')
# #1 dict을 선언
# appliers_score = {}
# #2 응시자 점수 저장
# for log in logs:
#     applied_nums, prob_num, score = map(str, log.split())
#     if applied_nums not in appliers_score:
#         appliers_score[applied_nums] = [0] * 101
#         appliers_score[applied_nums][int(prob_num)] = score
#     else:
#         appliers_score[applied_nums][int(prob_num)] = score
# print(appliers_score)
# #3 응시자 명단 뽑기
# appliers = list(appliers_score.keys())
# #4 비교대조군 문항일치 확인 및 점수 비교
# n = len(appliers)
# for i in range(n):
#     compare(i, appliers[i])
# print(answer)
# print(type(answer))
# # 사전순 정렬
# answer = sorted(answer)
# print(answer)


