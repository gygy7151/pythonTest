#딕셔너리
x =  {
   "name" : "워니",
   "age" :  20,
}
print(x)

print(x["name"]) #x딕셔너리의 "name"값을 프린트
print(x["age"]) #x딕셔너리의 "age"값을 프린트


#x딕셔너리 출력값
#name과 age는 불변하는 값들임. immutable
#list의 경우 key와 value값으로 나뉘는게 아닌점이 딕셔너리와 큰 차이점
#list의 경우 소괄호 안에 있는 값들을 바꿀 수 있음.
#단 딕셔너리에 새로운 값을 아래와 같이 추가할 수 있음

x[0]= "이고" #딕셔너리에 새로운 key값과 value값을 넣는 방법
print(x)
#{'name': '워니', 'age': 20, 0: '이고'}

print(x[0])
#워니

print("age" in x) #age라는 key가 x에 있으면 true
print("name" in x) #name이라는 key가 x에 있으면 true

#딕셔너리의 key값들만 프린트하는 방법
x =  {
   0 : "워니",
   1 :  20,
   "age ": 28, 
 }
print(x.key())
#AttributeError: 'dict' object has no attribute 'key'
#딕셔너리 오브젝트의 어트리뷰트key는 없다.

print(x.keys())
#dict_keys(0, 1, "age") (x)
#dict_keys([0, 1, "age"]) (O) 배열로 파라미터를 받는다.

#딕셔너리의 value값들만 프린트하는 방법
print(x.values())
#dict_values(["워니", 20, 28])

#만약값을 key값 또는 value값을 하나씩 차례대로 출력하고 싶을땐 for문을 이용한다
x =  {
   0 : "워니",
   1 :  20,
   "age": 28, 
 }

for key in x:
    print(key)
    print(x[key])

#차례대로 값을 리턴한다
#0
#워니
#1
#20
#age
#28

#근데 key값과 value값을 구분해서 나타내 보여주고 싶을땐?
x = {
   0 : "자아",
   1 : 20,
   "vulepe" : 1,
}

for key in x:
       print("key": str(key))
       print("value": str(x[key])) 
#invalid syntax     ^ 
#(x) ':'이 아니라 '+'가 들어가야됨

for key in x:
       print("key" + str(key))
       print("value" + str(x[key]))
# key: 0
# value: 자아
# key: 1
# value: 20
# key: vulepe
# value: 1 

#key를 새로 생성하는 방법(위에 이미 언급함)
x = {
   "age" : 12
   "wing" : 13
   1 = "Ijaa"
}

x[4] = "Hola~!"

print(x)
#{'age' : 12, 'wing' : 13, 1 : 'Ijaa', 4 : 'Hola~!'}


#countingFruit
#리스트가 100개이상 될때..다 셀 수 없으므로 아래와 같이 코딩을 짜보자

fruit = ["사과", "사과", "복숭아", "레몬", "후르츠", "레몬", "사과", "복숭아", "포도", "사과", "사과", "복숭아", "레몬", "후르츠", "레몬", "사과", "복숭아", "포도"]
    
d={}
# d = {"사과": 2, "바나나":1 ..중략}

for x in fruit:
    #x  = "딸기"

    if x in d: # "딸기"라는 key가 d라는 딕셔너리에 들어있어?
        print d[x] = d[x] + 1 #있어? 그럼 "딸기" 갯수를 하나 올려줘 (x) if문결과값엔 print 들어가면 안돼 그리고 print하려면 ()parentheses가 들어가줘야되는데 중략되었잖아 체크해:)
    else
        d[x] = 1 #없어? 그럼 딕셔너리 d에 추가해줘


#Answer
d = {}

for h in fruit:
    if h in d:
        d[h] = d[h] + 1
    else: #else뒤에 : 세미콜론 꼭 붙여줘야돼..
        d[h] = 1

print(d) #함수를 실행시키는건 이거다. 위에는 그냥 붕어빵 틀일뿐 







