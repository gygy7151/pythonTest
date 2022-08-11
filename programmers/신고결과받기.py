
'''
신고결과받기
'''
'''
첫번째풀이
'''
def solution(id_list, report, k):
    answer = []
    ban_user = set()

   
    # 1 set은 그냥 비어있어두 상관없음
    D = { id: [0, set()] for id in id_list}
    id_list = { id: 0 for id in id_list}


    # 2 context 입력값이 처음엔 2개인줄 알고 잘못 입력함
    for context in report:
        user, badUser = context.split()

        if badUser in D[user][1]:
            continue
        D[user][1].add(badUser)
        D[badUser][0] += 1


    # 3
    for userId, report in D.items():
        if report[0] >= k:
            ban_user.add(userId) 
    
    #4 그냥 단순히 userId가 ban_user 포함되면 해당 유저 id에 +1 카운트하는 실수를 저지름..
    for userId, report in D.items():
        for badUser in report[1]:
            if badUser in ban_user:
                # 리스트명을 잘못선언했음 user_id(x), id_list(o)
                id_list[userId] += 1

    #print(id_list)


    # 5
    for resultMailCount in id_list.values():
        answer.append(resultMailCount)

    return answer