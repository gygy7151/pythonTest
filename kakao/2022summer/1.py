'''
테스트케이스3개 맞음. 예외를 모르겠음
'''
survey = ["RT", "TR", "RT", "RT", "NA"]
choices = [1, 1, 7, 7, 7] 

def solution(survey, choices):
    n = len(survey)
    score = [0,3,2,1,0,1,2,3]
    category = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for id, opt in enumerate(survey):
        num = choices[id]
        if score[num] == 0:
            break
        if 0 < num < 4:
            category[opt[0]] += score[num]
        elif 4 < num < 8:
            category[opt[1]] += score[num]
    order = ['R','T','C','F','J','M','A','N']
    answer = ""
    for i in range(0, 7, 2):
        if category[order[i]] >= category[order[i+1]]:
            answer += order[i]
        elif category[order[i]] < category[order[i+1]]:
            answer += order[i+1]
    answer = list(answer)
    answer.insert(0,'\"')
    answer.append('\"')
    answer = ''.join(answer)
    return answer
res = solution(survey,choices)
print(res)
