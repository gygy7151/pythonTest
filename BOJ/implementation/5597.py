'''
과제 안 내신 분..?
'''
'''
첫번째풀이
'''
def solution():
    student = [ x for x in range(1, 31)]

    for _ in range(28):
        student.remove(int(input()))
    
    student.sort()
    print(student[0])
    print(student[1])
solution()