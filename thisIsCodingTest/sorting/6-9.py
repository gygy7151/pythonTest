'''
파이썬 정렬 라이브러리
sorted()나 sort()를 이용할때 key 매개변수를
입력으로 받을 수 있다.
이때 key값으로는 하나의 함수가 들어가야 하며
정렬 기준이 된다.
만약 리스트의 데이터가 튜블로 구성되어 있을때
각 데이터의 두번째 원소를 기준으로 설정하는경우
'''

array = [('서울', '특별시'), ('수원', '특례시'), ('제주', '특별시')]

def setting(data) :
    return data[1]


result = sorted(array, key=setting)
print(result)