'''
양궁대회
'''
'''
참고풀이 - 그리디, 비트마스크
'''
def solution(n, info):
    answer = [0 for _ in range(11)]
    # 라이언이 쏜 과녁갯수 담는 용도
    tmp = [0 for _ in range(11)]
    maxDiff = 0

    for subset in range(1, 1 << 10):
        ryan = 0
        apeach = 0
        cnt = 0
        print(subset)
        print(type(subset))

        for i in range(10):
            if subset & (1 << i):
                ryan += 10 - i
                # info[i]어피치까 쏜 과녁갯수
                tmp[i] = info[i] + 1
                cnt += tmp[i]
            else:
                tmp[i] = 0
                if info[i]:
                    apeach += 10 - i

        if cnt > n: continue

        tmp[10] = n - cnt

        # maxDiff가 같은게 여러개 있는경우
        if ryan - apeach == maxDiff:
            for i in range(10):
                if tmp[i] > answer[i]:
                    answer = tmp[:]
                    break
                elif tmp[i] < answer[i]:
                    break

        #라이언이 이기는 경우
        if ryan - apeach > maxDiff:
            maxDiff = ryan - apeach
            answer = tmp[:] # 화살정보를 복사해주면됨 캬~~~~

    if maxDiff == 0:
        answer = [-1]

    return answer 

'''
두번째 풀이 - 시뮬레이션 - 조합활용 - 추후도전
'''


'''
첫번째 풀이  - 틀림 -> 수정완료
'''

def solution(n, apeach_score):
    answer = [0 for _ in range(11)]
    ryan_score = [0 for _ in range(11)]
    maxDiff = 0

    for brute in range(1, 1 << 10):
        ryan = 0
        apeach = 0
        cnt = 0

        for i in range(10):
            if brute & (1 << i):
                ryan += 10 - i
                ryan_score[i] = apeach_score[i] + 1
                # 아 실수.. 어피치 과녁횟수를 더해주고 있었음..
                cnt += ryan_score[i]

            else:
                ryan_score[i] = 0

                if apeach_score[i]:
                    apeach += 10 - i

        if cnt > n: continue

        ryan_score[10] = n - cnt

        if ryan - apeach == maxDiff:
            for i in range(10, -1,-1):
                if ryan_score[i] > answer[i]:
                    answer = ryan_score[:]
                    break

                elif ryan_score[i] < answer[i]:
                    break

        if ryan - apeach > maxDiff:
            maxDiff = ryan - apeach
            answer = ryan_score[:]

    if maxDiff == 0:
        answer = [-1]

    return answer

