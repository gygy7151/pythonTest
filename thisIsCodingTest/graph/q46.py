'''
최종순위 - 
올해 예선에 참가한 n개의팀
놀랍게도 작년과통일한 팀임
최종순위말고 순위가 바뀐팀목록만 발표하려고함
작년에 팀 13이 6보다 순위가 높았는데
올해는 팀 6이 13보다 순위가 높으면 (6, 13)을
발표할것임
이 정보만으로 올해 최종순위를 만들어보고자함 (ㅋㅋ뭐냐결국 1등이중요허네)
작년순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을때 
올해 순위를 만드는 프로그램을 만들어라
근데, 올해순위를 만들수 없는경우도 있을 수 있고
일관성이 없는 잘못된 정보일 수 도 있다.
입력조건 첫째줄에는 테스트케이스의 케이스의 개수nums가 주어지고,nums는 100개를 넘지 않음
두번째줄에는 팀의수 n이 주어지고
세번째줄에는 n개의 정수 ti를 포함한 줄 이때 ti는 작년에 i등을한 팀의 번호임 1등이 가장 성적이높은팀
(이때 ti는 1이상 n이하임)
네번째줄에는 상대적인 등수가 바뀐 쌍의 수 m (이때 m은 0이상 25000이하임)
다섯번째줄에는 ai와 bi를 포함하고 있는 m줄
출력조건에 n개의 정수를 한줄에 출력하되
1등팀부터 순서대로출력함
만약 확실한 순위를 찾을수 없다면 ?를 출력함
데이터에 일관성이 없어서 순위를 정할수 없는경우엔
IMPOSSIBLE을 출력함
'''
import sys
import copy
input = sys.stdin.readline
nums = int(input())
grade = []
result = ''

def arrange_rank(cases):
    for i in range(cases):
        team_num = int(input())
        grade.append(list(map(int, input().split())))
        origin = copy.deepcopy(grade)
        m = int(input())
        if m == 0:
            result = grade[i]
            print(result)
            continue
        else :
            for _ in range(m):
                a, b = map(int, input().split())
                if grade[i].index(a) > grade[i].index(b):
                    grade[i].remove(b)
                    a_rank = grade[i].index(a)
                    grade[i].insert(int(a_rank)+1, b)
                    result = grade[i]
                elif grade[i].index(a) == grade[i].index(b):
                    result = '?'
            if origin[i] == grade[i]:
                result = 'IMPOSSIBLE'
    
        print(result)

arrange_rank(nums)



        





