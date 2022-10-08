
'''
코딩친구 - 15분만에 풀이완료
'''
'''
첫번째풀이
'''
'''

kelly는 뒤처짐
sam보다 더 많은문제를 푸는데 필요한 최소일수를 구해라.
만약 능가할수 없다면 -1을 리턴함

differenc는 5문제 sam이 앞서 있다는 말임
그리고 각각 데일리로 푸는 문제갯수가 주어짐
kelly는 0부터 시작하고
sam은 differenc를 초깃값으로 갖고 있으면 됨
kelly가 맨처음 sam보다 앞설때를 구하면 됨

불가능한건 언제지 도대체? 
samDaily가 kelly가 매일 푸는 문제보다 많은경우
절대 앞설 수 없음
데일리 문제푸는 수가 똑같다? 이것도 절대 이길 수 없음 
비길 순 있어도..
ㅇ
예외처리를 앞서해줘야 겟군
결국 kelly가 samDaily보다 매일 좀 더 많이 풀면
결국 앞선다는 거구나..
희야 이거 진짜 중요하다.

'''

'''
문자열탐색
'''
'''
제거 할 수 있는 최대 문자수를 검색하라..음
예를들면 abbabaa가 있는데
bb를 제거할꺼면 제거 순서를
7,1,2,5,4,3,6

# 인덱스를 차례로 돌면서 -로 해당 값처리한다
# 처리하면서 target subsequenc가 존재하는지 안하는지 체크한다.
# 정규표현식을 활용해 target문자열 여부를 검사한다.
# 리턴값이 None이 아니면 maxRemoval += 1한다.
# 만약 리턴값이 None이면 maxRemoval을 반화하고 함수종료한다.
# 아...target값 요소 하나씩 여부 체크해줘야 되서 
# for문으로 돌면서 각각 p값 체크해줘야 되겠구만 
# 만약 하나라도 None이 발생하면? maxRemoval += 1 break로 나옴
# 아니면 maxRemoval을 반화하고 함수종료한다.
# 순서는 -1씩 주의..
'''
from collections import Counter

def solution(origin, target):
    dic = Counter(origin)
    
    # origin 요소를 target과 각각 비교해서 모두 일치하는지 확인
    # 각 횟수별로 origin 돌면서 카운트 맞는지 비교
    for char in dic.keys():
        target_count = Counter[char]
        now_char_cnt = 0
        
        for t_char in target:
            if t_char == char:
                now_char_cnt += 1


        if now_char_cnt == target_count:
            continue
        else:
            # 만약 하나라도 안맞으면 removalCnt 리턴
            return False
    
    return True
        
        # 그게 아니라면 removalCnt 추가

remove = [3,1,2,7,4,5]
origin = list('aabbabbab')
target = 'bb'
removalCnt = 0
for idx in remove:
    origin[idx] = '-'
    res = solution("".join(origin),target)
    # removalCnt 리턴
    if not res:
        print(removalCnt)
        break
    
    else:
        removalCnt += 1


