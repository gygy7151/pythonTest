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
#안녕! 나는 이자아야

#변수를 복수로 가질때 출력값이 동일한것을 수정하려면? 새로운 함수를 만들어야 한다.
#'__init__' 이 함수는 Person이라는 오브젝트를 만들때 self를 첫 인자로 받 우리가 pass로 쓸 변수들을 새로 설정할 수 있게 해준는데 여기선 name으로 설정했다.
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("안녕! 나는" + self.name + "야")

wonie = Person("워니")
michael = Person("미카엘")
jenny = Person("제니")

wonie.say_hello()
michael.say_hello()
jenny.say_hello()

# 안녕! 나는워니야
# 안녕! 나는미카엘야
# 안녕! 나는제니야


#'__init__'함수에 pass로 쓸 변수'age'를 새롭게 추가해보자.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_introduce(self):
        print("안녕! 나는 " + self.age + "살이구 " + self.name + "이라고 해~ 만나서 반갑다!^^힣")

jenni.say_introduce("제니", 20) #(x)
#NameError: name 'jenni' is not defined 

jenni = Person("제니", 20) #이렇게 jenni라는 객체를 선언해주고 호출해야 된다.
jenni.say_introduce()
#print("안녕! 나는 " + self.age + "살이구 " + self.name + "이라고 해~ 만나서 반갑다!^^힣")
TypeError: can only concatenate str (not "int") to str #self.age는 int로 들어오는데 str로 타입변경해주어야됨

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_introduce(self):
        print("안녕! 나는 " + str(self.age) + "살이구 " + self.name + "이라고 해~ 만나서 반갑다!^^힣")

ijaa = Person("Ijaa", 20)
ijaa.say_introduce()
#! 나는 20살이구 Ijaa이라고 해~ 만나서 반갑다!^^힣

#상속(heritance)
앞서 이전에 Person이라는 클래스를 만들었는데
이번엔 Police랑 Programmer를 만들어 보자.
경찰이랑 Programmer이라는 클래스는 서로 다른걸 할 수 있어야 된다.
단 경찰과 프로그래머는 Person을 상속받도록 한다.

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다"+ to_arrest)

class Programmer(Person):
    def coding(self, to_coder):
        print(to_coder + "님, 지금 열나게 코딩중이세요")

jenni = Person("제니", 12)
wooni = Programmer("워니", 29)
ijaa = Police("이자아", 22)

jenni = Person("제니", 12)
wooni = Programmer("우니", 29)
itzy = Police("이찌", 22)
# 안녕! 나는 20살이구 Ijaa이라고 해~ 만나서 반갑다!^^힣
# 안녕! 나는 12살이구 제니이라고 해~ 만나서 반갑다!^^힣
# 안녕! 나는 29살이구 우니이라고 해~ 만나서 반갑다!^^힣

wooni.coding("우니")
#우니님, 지금 열나게 코딩중이세요
wooni.arrest("우니")
#AttributeError: 'Programmer' object has no attribute 'arrest'
#다른 클래스의 경우 상속받은게 없으니깐 당연히 안됨.


#패키지랑Package 모듈Module
패키지란? 어떤 기능들을 구현하는 모듈들의 합임.
예를 들면 날씨정보를 알아보는 패키지도 있고
위치정보를 알아보는 패키지도 있음
라이브러리라고 하는게 파이썬에선 "패키지"임

모듈이란? 코드를 잘 모아서 기능하나를 구현해놓은 파일.

그러면 패키지란 왜있냐?
내가 개발자인데 날씨정보를 알아보는 패키지를 하나만들었어
근데 개발자들은 만든걸 공유하고 싶잖아
내가 이미써놓은 코드를 그대로 다운받아서 사용가능하게끔 하는거임.

# animal package
# dog, cat modules
# dog, cat modules can say "hi"

# 패키지를 만들려면 항상 폴더를 만들어야됨
# 폴더이름이 패키지 이름이 됨
# 모듈의 이름은 파일 이름이 됨

dog.py
cat.py
파일 만들고 각각 
'dog.py'파일에는
class Dog:
    def hi(self):
        print("bark!") #개가 안녕하는 소리


'cat.py'파일에는
class Cat:
    def hi(self):
        print("meowww~") #고양이가 안녕하는 소리
함수를 각각 만들어 준다.

패키지를 만들려면 하나 더 추가해줘야되는 파일이 있다.
바로 __init__.py
해당 파일 생성후 어떤걸 말해줘야 되나면?
이 animal패키지가 어떤 모듈들의 합인지 위 파일안에 말해줘야됨.
__init__.py에서 
from .cat import Cat # . <- "이 폴더에 있는" cat.py이라는 파일에서 Cat이라는 클래스를 갖고와줘
from .dog import Dog # . <- "현재 폴더에 있는" dog.py이라는 파일에서 Dog라는 클래스를 갖고와줘
#from .cat import*라고 하면 cat모듈에 있는 모든 코드를 다 불러와요

그다음에 main.py에서#(만약 파일이 없으면 main.py라는 파일을 생성하세요:) 
main.py
from animal import dog # animal패키지에서 dog라는 모듈을 갖고와줘
from animal import cat # animal패키지에서 cat이라는 모듈을 갖고와줘

d = dog.Dog() #instance
d.hi()

c = cat.Cat()
c.hi()
# bark!
# meowww~

#근데 뭔가 중복되는 것 같아서 아래와 같이 해주면
from animal import * # animal 패키지가 갖고 있는 모듈을 다 불러와

d = Dog()
c = Cat()

d.hi()
c.hi()
# bark!
# meowww~

#코드를 좀더 잘 정리하기 위해 '모듈화 한다' 라고 이야기한다.


#geopy 패키지 활용
main.py

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Ijaa")
location = geolocator.geocode("Seoul, South Korea")

print(location.raw)
# {'place_id': 258410442, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright', 'osm_type': 'relation', 'osm_id': 2297418, 'boundingbox': ['37.4285424', '37.7013911', '126.7644328', '127.1838054'], 'lat': '37.5666791', 'lon': '126.9782914', 'display_name': '서울, 노원구, 대한민국', 'class': 'boundary', 'type': 'administrative', 'importance': 0.6297939847554467, 'icon': 'https://nominatim.openstreetmap.org/ui/mapicons//poi_boundary_administrative.p.20.png'}

print(location.longitude)
# 126.9782914

print(location.latitude)
# 37.5666791

#실생활 적용예제를 만들어 보자

#라이브러리와 API[문자를 보내는 실생활서비스를 만들어보자]
라이브러리란? 다른개발자가 패키지를 공유해놓은것
API란 개발자들이 코드를 통해서 데이터를 가져갈 수 있도록 만들어 놓은 길 같은것.
예를들어 날씨정보를 가져오고싶다면 기상청 api코드를 써서 그 정보를 가져오는것.
이번에는 문자를 보낼 수 있게 해주는 api랑 라이브러리를 이용해서 문자를 보내보자

우선 아래 사이트에 들어가서 회원가입하고
 https://www.twilio.com
 
 Trial Number랑 Account SID랑 AUTH TOKEN를 따로 저장해놓는다.

 우리가 어떤 사이트에 들어갈때 로그인이 필요한것처럼:)
 
다시 replit.com으로 돌아와서
package 메뉴를 클릭후
'twilio.api'를 검색한다
두번째줄 twilio옆에 플러스 버튼을 클릭한다

version 6.55.0
Twilio API client and TwiML generator

그리고 twilio 사이트에 돌아가서 pythoh quickstart에 있는
예제코드를 그대로 아래와 같이 복사 붙여넣기 한다.

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] #우리가 가져온 값으로 바꿔줘야됨
auth_token = os.environ['TWILIO_AUTH_TOKEN'] #상동
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="안녕 뭐해?", #문자발신내용
                     from_='+15017122661', #발신인
                     to='+15558675310' #수신인
                 )

print(message.sid)

#위와같이 했으나 아래와 같이 ModuleNotFoundError와 KeyError가 뜸
//ModuleNotFoundError
#Traceback (most recent call last):
#   File "/opt/virtualenvs/python3/lib/python3.8/site-packages/twilio/rest/resources/imports.py", line 3, in <module>
#     from urlparse import parse_qs
# ModuleNotFoundError: No module named 'urlparse'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "main.py", line 4, in <module>
#     from twilio.rest import Client
# Traceback (most recent call last):
#   File "/opt/virtualenvs/python3/lib/python3.8/site-packages/twilio/rest/resources/imports.py", line 3, in <module>
#     from urlparse import parse_qs
# ModuleNotFoundError: No module named 'urlparse'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "main.py", line 4, in <module>
#     from twilio.rest import Client
# Traceback (most recent call last):
#   File "/opt/virtualenvs/python3/lib/python3.8/site-packages/twilio/rest/resources/imports.py", line 3, in <module>
#     from urlparse import parse_qs
# ModuleNotFoundError: No module named 'urlparse'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "/opt/virtualenvs/python3/lib/python3.8/site-packages/twilio/rest/resources/imports.py", line 3, in <module>
#     from urlparse import parse_qs
# ModuleNotFoundError: No module named 'urlparse'

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
# Traceback (most recent call last):
#   File "main.py", line 4, in <module>
#     from twilio.rest import Client
#   File "/opt/virtualenvs/python3/lib/python3.8/site-packages/twilio/rest/__init__.py", line 1, in <module>
#     from .base import set_twilio_proxy
#   File "/opt/virtualenvs/python3/lib/python3.8/site-packages/twilio/rest/base.py", line 6, in <module>
#     from twilio.rest.resources import Connection
#   File "/opt/virtualenvs/python3/lib/python3.8/site-packages/twilio/rest/resources/__init__.py", line 5, in <module>
#     from .base import (
#   File "/opt/virtualenvs/python3/lib/python3.8/site-packages/twilio/rest/resources/base.py", line 15, in <module>
#     from ... import __version__
# ImportError: cannot import name '__version__' from 'twilio' (unknown location)
#  
#위 내용이 프린트되면 문자가 발송안된것..
//KeyError
#wilio: raise KeyError(key) from None
# Traceback (most recent call last):
#   File "main.py", line 8, in <module>
#     account_sid = os.environ['TWILIO_ACCOUNT_SID'] #우리가 가져온 값으로 바꿔줘야됨
#   File "/usr/lib/python3.8/os.py", line 675, in __getitem__
#     raise KeyError(key) from None
# KeyError: 'TWILIO_ACCOUNT_SID'

그래서 아래와 같이 수정함

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ='ACeaa4794455b9f751fbacdce13a20c650'
auth_token ='4a0ec15d2661e5775d6018f5a35d0a83'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="자니?(feat.ex-BF)",
                     from_='+15017122661',
                     to='+821012341234'
                 )

print(message.sid)

#근데 만약 처음에 twilio 가입할때 인증(verified)했던 번호외에 다른 번호로 메세지 보내고 싶으면 아래와 같이 또 에러 발생
#스팸방지를 위해그런거라고 하니 참고하길 바람:)
#다른번호도 인증하거나 미인증번호에도 메세지 보낼 수 있는 twilio 신규번호를 구매할것.
twilio.base.exceptions.TwilioRestException: 
HTTP Error Your request was:

POST /Accounts/ACeaa4794455b9f751fbacdce13a20c650/Messages.json

Twilio returned the following information:

Unable to create record: The number  is unverified. Trial accounts cannot send messages to unverified numbers; verify  at twilio.com/user/account/phone-numbers/verified, or purchase a Twilio number to send messages to unverified numbers.

More information may be available here:

https://www.twilio.com/docs/errors/21608
















#세션과 쿠키의 차이
#양쪽의 key가 맞아야됨
#쿠키가 없으면 서버에 저장이 안됨
#추후 빌트인된 오브젝트 또한 공부 필요(내일)

