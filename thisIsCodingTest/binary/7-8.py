'''
떡볶이 떡 만들기

떡볶이의 총길이는 H로 지정가능
하지만 개별 떡의 길이는 일정하지 않음
절단기는 한번만 절단함
높이가 H보다 긴떡은 H의 위의 부분이 잘리고
낮은떡은 잘리지 않음

예를들어 19, 14, 10, 17 떡이 
절단기를 15로 지정하면
자른뒤 높이는 15 14 10 15가 됨 요론느낌
잘린떡의 길이는 4 0 0 2 가되므로
손님은 6센치만큼의 길이를 가져간다.
이집 장사 사기네..
손님이 왔을때 요청한 총 길이가 m일때
적어도 m만큼의 떡을 얻기 위해
절단기에서 설정할 수 있는 최댓값의 높이를 구하는
프로그램을 작성하시오
'''

n, m = map(int, input().split())
slices = list(map(int, input().split()))

max_val =  max(slices)
min_val = min(slices)

def making_dduck() :
    total = 0

    while m > total : 

        for h in range(max_val, min_val, -1) :

            res = []
            for i  in range(n) :

                if slices[i] <= h :

                    res.append(0)
                
                else :

                    res.append(abs(h - slices[i]))
        
            print(res)
            total = int(sum(res))
            print(total, '합계')
        
            if total == m :
                print('최대 높이는 {}입니다.'.format(h))
                break


making_dduck()
