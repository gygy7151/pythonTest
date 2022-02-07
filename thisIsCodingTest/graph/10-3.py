'''
팀결성
0번부터 N번까지의 번호를 부여했다.
모든학생이 서로다른팀이되어
총 N+1팀이 존재한다.
이때 '팀합치기'연산과 '같은팀여부확인'연산을 사용할수있다.
m개의 연산을 수행할 수 있을때,
같은 팀 여부확인 연산에 대한 연산결과를 출력하는 프로그램을 출력하시오
입력조건 0번부터 n번까지의 번호
m은 입력으로 주어지는 연산의 개수 = 통로의개수
팀합치기 연산은 0 a b 형태로 a번학생이 속한팀과 b번학생이 속한팀을 합친다는의미
같은팀여부확인연산은 1 a b 형태로 주어지며 a번학생과 b번학생이 같은팀에 속해있는지를 확인하는 연산
a와 b는 n이하의 양의정수이다.
같은팀여부확인연산에만대하여 yes 혹은 no로 결과를 출력한다.
'''

def find_team(teams, a):
    if teams[a] != a:
        teams[a] = find_team(teams, teams[a])
    return teams[a]

def union_team(teams, a, b):
    a = find_team(teams, a)
    b = find_team(teams, b)

    if a < b:
        teams[b] = a
    else:
        teams[a] = b

n, m = map(int, input().split())
teams = [0] * (n+1)

for i in range(0, n+1):
    teams[i] = i

for _ in range(m):
    check, a, b = map(int, input().split())

    if check == 0:
        union_team(teams, a, b)
    
    elif check == 1:
        if find_team(teams, a) == find_team(teams, b):
            print('YES')
        else:
            print('NO')
