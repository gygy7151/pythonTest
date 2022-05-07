'''
테스트케이스 모두 틀림// 정답은 15인데..
'''
def solution(alp, cop, problems):
    n = len(problems)
    visited = [False] * (n)
    answer = 0
    temp_alp, temp_cop, temp_cost = 0, 0, -2
    for i, prob in enumerate(problems):
        if not visited[i]:
            if prob[0] == alp and prob[1] == cop:
                visited[i] = True
                alp += prob[0]
                cop += prob[1]
                answer += prob[4]
                temp_alp = max(temp_alp, prob[0])
                temp_cop = max(temp_cop, prob[1])
                temp_cost = min(temp_cost, prob[4])
            else:
                alp_diff = abs(prob[0]-alp)
                cop_diff = abs(prob[1]-cop)
                new_cost = (alp_diff) + (cop_diff)
                for j in range(i, n):
                    if problems[j][0] == alp and problems[j][1] == cop:
                        if problems[j][2]>= alp_diff and problems[j][3] >= cop_diff:
                            visited[j] = True
                            alp += prob[0]
                            cop += prob[1]
                            answer += prob[4]
                            temp_alp = max(temp_alp, prob[0])
                            temp_cop = max(temp_cop, prob[1])  
                            temp_cost = min(temp_cost, prob[4])
                        else:
                            visited[i] = True
                            alp += int(alp_diff)
                            cop += int(cop_diff)
                            answer += (prob[4] + int(new_cost))
    return answer

alp, cop = 10, 10
problems = [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]
res = solution(alp,cop,problems)
print(res)
