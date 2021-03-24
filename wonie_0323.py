#변수 variable
x = 1
y = 2

print(x)
print(y)

z = "안녕"
print(z)

#타입 type(숫자/number)

x = 1
y = 2
z = 1.2

print(x + y)
print(x - y)
print(x * y) 
print(x % y) #x를 y로 나눈 값의 나머지
print(x ** y) #x를 y번 제곱한 값

#타입 type(문자열/syntax)

x = "hello"
y = 'by4'

z= """
안녕하세요
블루불페입니다.

"""

print(x)
print(y)
print(z)

#syntaxCasting
#TypeError
print("너 혹시 몇살이니?" + 3) 
print("너 혹시 몇살이니?" + str(3이야?)

#suscess
print("너 혹시 몇살이니?" + str(3) +str("은 안돼?"))


x = 4
y = "4"

print(x)
print(str(x) + y)

#result
#4
#44

#TypeError
print(str(x+ y))

#불리안: boolean

x = True
y = False

print(x)
print(y)

#typeerror
x = true
y = false

#if조건문
if 0 > 0 or 2 > 1:
  print("Hello")
  
x = 3
if x > 2:
    print("Hello")


 x = 5
if x > 5:
    print("Hello")
else:
  print("Hi")
#Hi

  x = 3
if x > 5:
    print("Hello")
elif x == 3:
  print("Hi")
else:
  print("hallo")
#Hi

#함수문 function
def chat():
     print("영희:  나? 나는 20")

chat()
#"영희:  나? 나는 20"


#파라미터 활용 함수1
def chat(name1, name2):
     print("%s: 나? 나는 20" % name1)
 print("%s: 나? 나는 20" % name2)

chat("철수","영희")

#
def chat(name1, name2, age):
     print("%s: 나? 나는 20" % name1)
 print("%s: 나? 나는 %d" % (name2, age))

chat("철수","영희", int(3))


#파라미터 활용 함수2

def dsum(a, b):
      result = a + b
  return result #return은 dsum이라는 함수호출값을 특정 변수에 담아주는 매소드기능을함.

a = 1 #a선언
b = 2 #b선언
c = a + b

dsum(a, b) #그냥 dsum만 해도 출력안됨.
d = dsum(a, b) #반드시 변수 d로 대입시켜줘야됨
#만약 return이 아니라 print이면 변수d로 함수dsum(a, b)값이 넘겨지지않음
#위 이유때문에 print(d)를 할경우 "none"값이 출력안됨.


#하지만 print일경우 dsum함수 호출하면 입력된 파라미터값활용 함수값 출력됨.
def dsum(a, b):
      result = a + b
  print(result)

dsum("a", "b") #ab로 값이 출력됨.
d = dsum(a, b) #but, dsum함수값이 d로 대입이 안되기때문에 print(d)값은 nono이됨.



print(d)
#3이나옴

e = dsum("a", "b")
print(e)
#ab나옴

x = 1
y = 2 
z= x + y


# 먼저 이름과 나이를 받아라
# 나이가 10살 미만이면 "안녕"이라고 말해라
# 나이가 10살에서 20살 사이면 "안녕하세요"라고 말해라
# 그외에는 "안녕하십니까"라고 말해라

def whoYou(name, age)
if age < 10:
    print ("안녕? 나는 $d살 %s이라고해." % (name, age)) #if문안에선 2개이상 못사용함. 평서문에서만 가능.
elif age >= 10 or age <= 20:
    print ("안녕하세요! 저는 %d살 %s입니다." %(name, age))
else:
    print ("안녕하십니까! %d살 %s입니다. 만나서 반갑습니다. " %(name,age))

whoYou("블루불페", 3):

#안됌ge가 int라 변수는 str만 받을 수 있음...

def whoYou(name, age):
     if age < 10:
    print ("안녕? 나는"+ age +"살  "+ name + "이라고해")
 elif age >= 10 and age <= 20:
    print ("안녕하세요! 저는 "+ age +"살 "+ name +"입니다.")
 else:
    print ("안녕하십니까! "+ age +"살 " + name +"입니다. 만나서 반갑습니다.")

whoYou("블루불페", 3)

#애도 안됌. age가 int라 변수는 str만 받을 수 있음...





