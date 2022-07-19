
'''
완주하지못한선수
'''
'''
두번째풀이
'''
from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    #애초에 완주하지 못한 사람이 한명뿐이라..
    return list(answer.keys())[0]

'''
첫번째풀이 - 정확성,효율성 모두 성공
'''
from collections import Counter
def solution(participant, completion):
    P = Counter(participant)
    P = { name:cnt for name, cnt in P.items()}

    for runner in completion:
        if P[runner]:
            P[runner] -= 1
    
    for name, cnt in P.items():
        if cnt != 0:
            return name