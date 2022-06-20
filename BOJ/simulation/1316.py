'''
그룹단어체크
'''
def check(word):
    if len(word) == 1:
        return True
    words = list(word)
    group = [words[0]]
    target = words[0]
    for i in range(1,len(words)):
        if words[i] == target:
            continue
        if words[i] in group:
            return False
        else:
            target = words[i]
            group.append(words[i])
    return True

ans = 0
for _ in range(int(input())):
    if check(input()):
        ans += 1
print(ans)




    
