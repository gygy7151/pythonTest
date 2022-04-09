'''
단어변환 - dfs
'''
begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
answer = 0

def solution(begin, target, words):
    if target not in words:
        return 0
    q = []
    q.append((begin, 0))
    while q:
        x, count = q.pop(0)
        if x == target:
            return count
        for i in range(len(words)):
            diff = 0
            word = words[i]
            for j in range(len(x)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                q.append((word, count+1))
    return 0

print(solution(begin, target, words))


'''
두번째 풀이
'''
# def solution(begin, target, words):
#     def check(now, next):
#         for i in range(len(now)):
#             if now[i] == next[i]:
#                 continue
#             elif now[i] != next[i]:
#                 new = now.replace(now[i], next[i], 1)
#                 return new
#         return now

#     def match(n):
#         if n != target:
#             return False
#         else:
#             return True

#     def bfs(start, cnt):
#         visited = []
#         q = []
#         q.append((start, cnt))
#         visited.append(start)
#         while q:
#             first, count = q.pop(0)
#             for wrd in words:
#                 n_wrd = check(first, wrd)
#                 if not match(n_wrd) and n_wrd not in visited:
#                     q.append((n_wrd, count+1))
#                     visited.append(n_wrd)
#                 if match(n_wrd) and n_wrd not in visited:
#                     return count+2
#         return 0
#     if target not in words:
#         return 0
#     else:
#         res = bfs(begin, 0)
#         return res
# print(solution(begin, target, words))
'''
첫번째풀이
'''
# def check(now,next):
#     for i in range(len(now)):
#         if now[i] == next[i]:
#                 continue
#         elif now[i] != next[i]:
#                 new = now.replace(now[i], next[i], 1)
#                 return new
#     return now

# def match(n):
#     if n != target:
#         return False
#     else:
#         return True

# def bfs(start,cnt):
#     visited = []
#     q = []
#     q.append((start, cnt))
#     visited.append(start)
#     while q:
#         first, count = q.pop(0)
#         if count > len(words) and not match(first):
#             return 0
#         for wrd in words:
#             n_wrd = check(first, wrd)
#             if not match(n_wrd) and n_wrd not in visited:
#                 q.append((n_wrd, count+1))
#                 visited.append(n_wrd)
#             if match(n_wrd) and n_wrd not in visited:
#                 return count+2
#     return 0

# print(bfs(begin, 0))        

            

