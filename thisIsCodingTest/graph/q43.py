'''
탑승구 - 비행기는 탑승구 중 하나에 영구적으로 도킹
'''
g = int(input())
f = int(input())
gates = [False] * (g+1)
#f*g 행렬이 만들어질수 있음
#탑승구의수와 비행기의수는 1부터 시작임
#0,0은비워놓고시작
indegree = []

for i in range(f):
    indegree.append(input())

max_nums = 0
for gate in indegree:
        if gates[int(gate)] != True:
            gates[int(gate)] = True
            max_nums += 1 
        else:
            print(max_nums)
            break