
'''
로또의 최저순위와 최소순위
'''
'''
두번째 풀이 - 로또번호와 기존 번호 일치여부를 통해 최솟값 구하고 0의갯수만큼 더해서 최댓값구해줌
단, max나 min이 2미만이면 
'''
def solution(lottos, win_nums):
    answer = []
    min = 0
    max = 0

    lucky = { x: 5 - idx for idx, x in enumerate([2,3,4,5,6])}

    win_nums = set(win_nums) 

    for digit in lottos:
        if digit == 0:
            max += 1

        if digit in win_nums:
            min += 1


    max = min + max

    answer.append(lucky[max] if max >= 2 else 6)
    answer.append(lucky[min] if min >= 2 else 6)

    return answer

'''
첫번째 풀이 - 기억은 안나지만 일일이 여러가지 조합 만들어서 비교대조하려고 했음. 너무 비효율적
'''