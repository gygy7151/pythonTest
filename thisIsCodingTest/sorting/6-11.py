'''
성적이 낮은 순으로 학생 출력하기
학생 정보는 학생의 성적과 이름으로 구분
'''
import random

n = int(input())
array = []

for i in range(n) :
    
    input_data = input().split()

    array.append((input_data[0], int(input_data[1])))


for student in array :

    print(student[0], end = ' ')





