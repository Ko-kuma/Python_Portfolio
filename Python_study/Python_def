#함수 사용 및 호출
def greet(name):   # greet이라는 이름의 함수를 정의
    return f"안녕, {name}!"  # 결과를 돌려줌(반환)

message = greet("혜진")   # 함수를 호출(사용)
print(message)   # 안녕, 혜진!

#docstring 독스트링 
def greet(name):
    """이름을 받아서 인사말 문자열을 만들어 반환한다."""
    return f"안녕, {name}!"

print(greet.__doc__)   # 이름을 받아서 인사말 문자열을 만들어 반환한다.
#주석과의 차이임 프로그램에서 인식 가능하냐, 못하냐
print(help(greet))   # 독스트링을 포함한 함수 설명을 보여줌


#매개변수
def greet(name, greeting="안녕"):   # greeting은 기본값 "안녕"을 가짐
    return f"{greeting}, {name}!"

print(greet("혜진"))            # 안녕, 혜진! (greeting 생략 → 기본값 사용)
print(greet("혜진", "반가워"))   # 반가워, 혜진! (직접 지정하면 기본값 무시)

#가변 자료형(리스트, 딕셔너리)
def add_item(item, cart=None):
    if cart is None:
        cart = []   # 호출될 때마다 새로운 리스트가 만들어짐
    cart.append(item)
    return cart

print(add_item("사과"))    # ['사과']
print(add_item("바나나"))  # ['바나나'] 

#인자(위치인자, 키워드 인자)
def introduce(name, age, job):
    return f"{name}, {age}세, {job}"

# 위치 인자: 순서대로 값이 매칭됨
print(introduce("혜진", 30, "developer"))

# 키워드 인자: 이름을 지정해서 순서 상관없이 값을 넘김
print(introduce(job="developer", name="혜진", age=30))


#*args 개수가 정해지지 않은 위치 인자

def total(*args):  # 몇 개가 들어오든 args라는 튜플로 묶임
    return sum(args)

print(total(1, 2, 3))       # 6
print(total(1, 2, 3, 4, 5)) # 15

#*kwargs 개수가 정해지지 않은 키워드 인자

def print_profile(**kwargs):   # 어떤 키워드 인자든 kwargs라는 딕셔너리로 묶임
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="혜진", age=30, job="developer")
# name: 혜진
# age: 30
# job: developer

#스코프 - 함수 안과 밖의 변수
def calculate():
    result = 100   # 지역변수, calculate 함수 안에서만 존재

calculate()
#print(result)   # NameError 함수 밖에서는 result가 존재하지 않음

#람다식 - 이름없는 한 줄 함수

def square(x):
    return x ** 2

# 같은 기능을 람다로
square_lambda = lambda x: x ** 2

print(square(4))          # 16
print(square_lambda(4))   # 16