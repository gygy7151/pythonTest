def solution(answers):
    a = [1,2,3,4,5]*(10000//5)
    b = [2,1,2,3,2,4,2,5]*(10000//8)
    c = [3,3,1,1,2,2,4,4,5,5]*(10000//10)
    A = 0
    B = 0
    C = 0
    for idx, prob in enumerate(answers):
        print(idx)
        if a[idx] == prob:
            A += 1
        if b[idx] == prob:
            B += 1
        if c[idx] == prob:
            C += 1
    MAX = max(A, B, C)
    print(MAX)
    print(A, B, C)
    answer = []
    if A == MAX:
        answer.append(1)
    if B == MAX:
        answer.append(2)
    if C == MAX:
        answer.append(3)    
    return answer
answers = [1,3,2,4,2]
print(solution(answers))

# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result
