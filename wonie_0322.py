//파이썬 자료구조 1(List, Tuple)
파이썬에는 여러가지 자료구조가 있는데
그중 리스트(list),튜플(tuple), 사전(dict) 형태가 가장 많이 사용된다.
자료구조란(Data Structure)?
자료를 Data이자 data의 집합이라 명할 수 있는데
data집합의 각 원소들이 논리적으로 정의된 규칙에 의해 나열되면 
자료에 대한 처리를 효율적으로 수행 할 수 있도록 자료를 구분하여 표현한것이 자료구조이다.
전산학에서 자료를 효율적으로 이용할 수 있도록 컴퓨터에 저장하는 방법.


#조건문 elif
  elif age >= 10 and age <= 20:
       print("안녕하세요, %s" % name)
  else:
   print("안녕하십니까, %s" % name)

sayHello("지영", 28)
sayHello("지호", 10)
sayHello("지정", 18)
sayHello("지아", 8)

# break, continue

for i in range(3):
   print(i) # 0
   print("철수: 안녕 영희야 뭐해?")
   print("영희: 안녕 철수야, 그냥 있어.")

   if i == 1:
    continue
   print("지니: Hey 기가지니?!")

-> 부분적으로 프린트값 끊어줌

0
철수: 안녕 영희야 뭐해?
영희: 안녕 철수야, 그냥 있어.
지니: Hey 기가지니?!
1
철수: 안녕 영희야 뭐해?
영희: 안녕 철수야, 그냥 있어.
2
철수: 안녕 영희야 뭐해?
영희: 안녕 철수야, 그냥 있어.
지니: Hey 기가지니?!
 


#break for문 while문 차이
for i in range(100):
   print(i) # 0
   print("철수: 안녕 영희야 뭐해?")
   print("영희: 안녕 철수야, 그냥 있어.")
  
   if i > 2:
     break
0부터 3까지 리턴함


i = 0
while True:
   print(i) # 0
   print("철수: 안녕 영희야 뭐해?")
   print("영희: 안녕 철수야, 그냥 있어.")
   i = i + 1
  
   if i > 2:
     break
0부터 2까지만 리턴함.


# while문 작성법
i = 0
while i < 3:
   print(i) # 0
   print("철수: 안녕 영희야 뭐해?")
   print("영희: 안녕 철수야, 그냥 있어.")
   i = i + 1 # i = 2 + 1 = 3

# for문 작성법
for i in range(3):
   print(i)
   print("철수: 안녕 영희야 뭐해?")
   print("영희: 안녕 철수야, 그냥 있어.")


List리스트
x = list()
y= []

print(x)
print(y)

x = [1, 2, 3, 4]
y = ["hello", "world"] 
z = ["hello", 1,2,3 ]

print(x)
print(y)
print(z)


x = [1, 2, 3, 4]
//0번째 있는거 리턴
print(x[0])
//위치에 있는거 바꿔치기 가능
x[3] = 10
print(x)
결과값도출->[1, 2, 3, 10]


//리스트에서 자주 쓰이는 함수
#lenth함수
x = [1, 2, 3, 4]

num_elements = len(x)
print(num_elements)

#sort함수
x = [4, 2, 3, 1]

y = sorted(x) //반드시 y로 따로 받아줘야됨. print안에 또 함수 넣을 수 없음.
print(y)


#sum함수
x = [4, 2, 3, 1]

z = sum(x)
print(z)

//for문으로 배열 값(element) 하나씩 순서대로 프린트
x = [4, 2, 3, 1]
y = ["hello", "there"] //이것도 포함.

for n in x:
 print(n)

//엘레먼트 위치찾기 (인덱스함수)
x = [4, 2, 3, 1]
y = ["hello", "there"]
print(x.index(3))

print("hello" in y)
-> return true

if "hello" in y:
  print("hello 가 있어요")


#튜플
x = (1, 2, 3)
y = ('a', 'b', 'c')
z = (1, "hello", "there")

# print(x + y)
# print('a' in y)
# print(z.index(1))

# mutable (가변)  vs immutable (불변)
x[0] = 10 -> 에러남. 튜플은 한번 정한값 고칠수 없음






