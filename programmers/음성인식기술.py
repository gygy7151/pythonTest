# import re
call = "ababdefdedeabc"
# pattern = [[] for _ in range(len(call))]
# long = len(pattern)
    
# p1 = re.findall('\D', call)
# p2 = re.findall('[a-zA-Z]{2}', call)

# print(p1)
# print(p2)

# if 'hello' in call:
#     print(True)

from itertools import combinations
import re
def solution(call):
    lis = re.findall('\D', call)
    p = []
    org = 0
    max_ptrn = []
    for i in range(len(call), 1, -1):
        pattern = list(combinations(lis, i))
        p.append(pattern)

    for i in range(len(p)):
        case = p[i]
        for j in range(len(case)):
            ptrn = "".join(case[j])
            if ptrn in call:
                # print(ptrn)
                new = call.count(ptrn)
                if new == org and ptrn not in max_ptrn:
                    max_ptrn.append(ptrn)
                # print(new)
                # print(org)
                # print('----')
                if org < new and ptrn not in max_ptrn:
                    org = new
                    max_ptrn.clear()
                    max_ptrn.append(ptrn)
    # print(max_ptrn)
    answer = lis
    def delete(gap, word):
        for i in range(len(answer) - gap):
            test = "".join(answer[i:i+gap])
            if test == word:
                for _ in range(gap):
                    # print(i)
                    # print(i+gap)
                    del answer[i]
                    # print(answer)
                return True
        return False
    tag = False
    for _ in range(org*len(answer)):
        for wrd in max_ptrn:
            diff = len(wrd)
            tag = delete(diff, wrd)
    answer = "".join(answer)
    return answer

print(solution(call))

# import itertools
# import re
# def solution(call):
#     p = []
#     org = 0
#     max_ptrn = ''
#     for i in range(len(call), 2):
#         pattern = list(combinations(lis, i))
#         p.append(pattern)

#     for i in range(len(p)):
#         case = p[i]
#         for j in range(len(case)):
#             ptrn = "".join(case[j])
#             if ptrn in call:
#                 new = call.count(ptrn)
#                 ans_num = max(org, new)
#                 if ans_num > org:
#                     org = ans_num
#                     max_ptrn = ptrn
#     answer = call.strip(max_ptrn)
#     return answer

