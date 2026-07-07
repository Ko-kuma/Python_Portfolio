#dictinary 기본 구조

person = {
    "name": "혜진", # Key : Value
    "age": 30,
    "job": "developer",
}

#위 딕셔너리에서 값 꺼내기 및 추가 및 수정하기
print(person["name"]) # key에 저장되있는 값 꺼내기

person["job"] = "backend developer"   # 이미 있는 key면 값을 수정
person["city"] = "판교"  # 없는 key면 새로 추가

print(person) #{'name': '혜진', 'age': 30, 'job': 'backend developer', 'city': '판교'}

#값이 없는 key 접근 시 오류 print(person["phone"])   # KeyError: 'phone' 

#get 사용법 
print(person.get("phone"))   # None (에러 대신 None 반환)
print(person.get("phone", "없음"))   # "없음" (None대신 없음으로 기본값을 직접 지정 가능)

#pop (딕셔너리는 key로 값을 꺼내며 삭제)
person = {"name": "혜진", "age": 30}
age = person.pop("age")   # "age" key의 값을 꺼내면서 삭제
print(age)                  # 30
print(person)                # {"name": "혜진"}

#딕셔너리 합치기  update()
default_settings = {"theme": "light", "language": "ko"}
user_settings = {"theme": "dark"}

default_settings.update(user_settings)   # user_settings의 내용으로 덮어씀
print(default_settings)   # {"theme": "dark", "language": "ko"}

#중첩 딕셔너리
user = {
    "name": "혜진",
    "address": {
        "city": "판교",
        "zipcode": "13529",
    },
}
print(user["address"]["city"])   # 판교 (key를 두 번 이어서 접근)

#키, 값 쌍을 한번에 순회하기 for문 사용

person = {"name": "혜진", "age": 30}

for key in person.keys():   # key만 순회
    print(key)

for value in person.values():   # value만 순회
    print(value)

for key, value in person.items(): # key와 value를 동시에 순회
    print(key, value)
    
#Key가 있는지 확인(멤버십연산자 사용)
person = {"name": "혜진", "age": 30}
print("name" in person)   # True (key 확인)
print("혜진" in person)   # False (value는 in으로 확인 안 됨)

#셋(set) 
#셋과 딕셔너리의 {}대괄호의 차이는 :콜론이냐 , 쉼표이냐, {}빈괄호는 딕셔너
#기본 구조
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)   # {1, 2, 3} — 중복이 자동으로 제거됨 중복되는 값이 아닌 하나만 사용됨


#값 추가 삭제 
fruits = {"사과", "바나나"}
fruits.add("포도")        # 값 추가
fruits.remove("바나나")   # 값 삭제 (없는 값 삭제 시도하면 에러)
fruits.discard("수박")    # 값 삭제 (없어도 에러 안 남, remove보다 안전)


#집합 연산 - 교,합,차집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)   # {3, 4} — 교집합 (둘 다 있는 값)
print(a | b)   # {1, 2, 3, 4, 5, 6} — 합집합 (둘 중 하나라도 있는 값)
print(a - b)   # {1, 2} — 차집합 (a에는 있고 b에는 없는 값)
print(a ^ b)   # {1, 2, 5, 6} — 대칭차집합 (겹치지 않는 값들만)

#frozenset -set의 변하지않는 값 불변 버전

tags = frozenset(["python", "fastapi"])
# tags.add("django")   # AttributeErrortags = frozenset(["python", "fastapi"])은 수정 불가frozenset은 수정 불가


#변환 방법
# 얼어있는 상태
frozen = frozenset([1, 2, 3])

# set()을 사용하여 녹이기 (frozenset -> set), 결국 형변환
thawed = set(frozen)
thawed.add(4)  # {1, 2, 3, 4}

# frozenset()을 사용하여 다시 얼리기 (set -> frozenset), 다시 형변환
refrozen = frozenset(thawed)
# refrozen.add(5)  # AttributeError 발생 (수정 불가능)

