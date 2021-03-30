#클래스와 오브젝트
클래스는 붕어빵을 굽는 빵틀
오브젝트는 인스턴스라고도 불리는데 빵이다
즉 클래스를 이용해 만들어낸 물체.
#object = instance

class Person:
    def say_hello(self):
        print("안녕!")

say_hello() #(x)이렇게 하면 NameError가 뜬다.

p = Person() //class를 특정 변수에 담고
p.say_hello() //변수로 함수를 호출한다.
#안녕!

#변수는 class안에 들어갈 수 있다.
class Person:
    p = Person() #(x)이건 클래스를 p변수에 대입시킨것.
    def say_hello(self):
        print("안녕!")

p = Person()
p.say_hello() 


#Answer
class Person:
    name = "이자아"

    def say_hello(self):
        print("안녕! 나는" + self.name + "야")

p = Person()
p.say_hello()
















#세션과 쿠키의 차이
#양쪽의 key가 맞아야됨
#쿠키가 없으면 서버에 저장이 안됨
#추후 빌트인된 오브젝트 또한 공부 필요(내일)

