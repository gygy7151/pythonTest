'''
평균은 넘겠지
'''
for _ in range(int(input())):
    data = list(map(int, input().split()))
    average = sum(data[1:]) // data[0]
    
    cnt = 0
    for score in data[1:]:
        if score > average:
            cnt += 1
    over_average_ratio = (cnt / data[0]) * 100
    print(f"{over_average_ratio:.3f}%")

    