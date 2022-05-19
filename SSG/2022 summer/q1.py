'''
트럭옮기기 - 정답은 3이 되어야 되는데 틀림
'''

def solution(v, a, b):
    answer = 0
    tag = 0
    def exchange_v(v, tag):
        if tag == len(v)-1:
            return False
        if v[0] - a < 0:
            for i in range(1, len(v)):
                if v[i] - b < 0:
                    tag += 1
                    v.append(v.pop(0))
                    exchange_v(v,tag)
            return True
    if exchange_v(v, tag):
        v[0] -= a
        for i in range(1, len(v)):
            v[i] -= b
        answer += 1
        v.append(v.pop(0))
    else:
        return answer
res = solution([4,5,5], 2, 1)
print(res)