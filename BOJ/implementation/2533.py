'''
사회망 서비스(SNS)
'''
'''
두번째풀이
트리 구조와 DP를 합친 Tree DP 문제다.
DP의 경우 부문제의 최적해가 모여 전체 문제의 최적해가 찾을 수 있는 경우에 사용할 수 있다.
트리 구조의 경우 서브 트리들이 모여 전체 트리를 이루기 때문에 서브 트리의 최적해들을 통해 전체 트리의 최적해를 찾을 수 있다면 트리 구조에도 DP를 사용할 수 있다.
서브 트리들의 경우 구분할 수 있는 가장 좋은 포인트는 해당 서브트리의 ROOT 노드다.
따라서 구분되는 서브트리들의 ROOT 노드를 통해 DP 배열을 구성할 수 있다.
예를 들어 DP[ROOT노드 번호][A][B] ... 이런 식으로 문제 타입에 맞게 A,B... 를 세팅할 수 있다.
대부분의 Tree DP는 DFS를 통해 리프 노드까지 나아가고 리프 노드 부터 부문제를 해결하면서 위쪽으로 차근차근 올라온다.
즉 리프 노드쪽 부터 부문제를 해결해보면 마지막에는 최종 본 트리의 ROOT 노드의 본 문제를 해결할 것이고 앞에서 구한 것들을 통해 최적해를 구할 수 있을 것이다.
'''
import sys

sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
lines = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    lines[a].append(b)
    lines[b].append(a)
dp = [[0, 0] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]


def dfs(r):
    visited[r] = 1
    dp[r][0] = 1
    for i in lines[r]:
        if not visited[i]:
            dfs(i)
            dp[r][0] += min(dp[i][0], dp[i][1])
            dp[r][1] += dp[i][0]


dfs(1)
print(min(dp[1][0], dp[1][1]))

'''
첫번째풀이 - 4% 시간초과
'''
'''
얼리 어답터가 아닌 사람들은 자신의 모든 친구들이 얼리어답터일때만 아이디어를 받아들인다고함
친구 관계 그래프가 트리인 경우.
모든 두정점 사이엔 경로가 존재하면서, 사이클이 존재하지 않는 경우만 고려한다고 함
최소 얼리어답터의 수를 구하라..?
긍까 1번은 부모노드고
그다음 뎁스인 노드를 구하라는 거네.
어떻게 구할까?
1번노드랑 맨처음 연결한 애들만 구하면 되는거 아님?
근데 정점노드가 누구인지 알아야됨.. 진입차수가 필요하겠군
진입차수가 0인 애가 바로 부모 정점 노드임
'''

# 진입차수 담긴 1차원 배열 inDegree
# 진입차수가 1이고.. 
# 걍 연결된 link를 각 노드 별로 담은개 필요하겠군.. 상당히 무겁겠는데?
# 와..근데 N이 백만개래.. ㅋㅋㅋ

# 연결된 노드 정보에 접근해서 길이를 구하고 그 길이가 ans길이보다 크면 갱신해준다.
from collections import defaultdict
def solution():
    N = int(input())
    DP = defaultdict(int)

    for _ in range(N-1):
        i, j = map(int, input().split())
        DP[i] += 1

    print(max(DP.values()))
solution()




