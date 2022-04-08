'''
단어변환 - dfs
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
answer = 0
def check(now,next):
    for i in range(len(now)):
        if now[i] == next[i]:
                continue
        elif now[i] != next[i]:
                new = now.replace(now[i], next[i], 1)
                return new
    return now

def match(n):
    if n != target:
        return False
    else:
        return True

def bfs(start,cnt):
    visited = []
    q = []
    q.append((start, cnt))
    visited.append(start)
    while q:
        first, count = q.pop(0)
        if count > len(words) and not match(first):
            return 0
        for wrd in words:
            n_wrd = check(first, wrd)
            if not match(n_wrd) and n_wrd not in visited:
                q.append((n_wrd, count+1))
                visited.append(n_wrd)
            if match(n_wrd) and n_wrd not in visited:
                return count+1
    return 0

print(bfs(begin, 0))

            

