import keyword #키워드 관련 모듈 불러오기
from decimal import Decimal

#variable(변수)
#변수 선언 및 저장
age = 25 #age라는 변수에 25라는 숫자를 저장
name = "혜진" #name이라는 변수에 문자열을 저장

#변수 이름의 규칙
#1st_place = "금메달"#(X) SyntaxError: invalid decimal literal발생 앞에 숫자가 먼저 들어가기 때문
#if = 30#(X) 예약어를 사용했기 때문 SyntaxError: invalid syntax
#us er = 50, us-er SyntaxError: invalid syntax 에러 발생 
#age와 Age 이건 실행은 되지만 age와 Age는 전혀 다른 변수라는 걸 기억

#예약어 확인 키워드
#print(keywoerd.kwlist) 현 버전의 python의 키워드 관련 예약어 전체 출력


#기본 자료형 사용 예시
a_int = 30 # int(integer) 정수
a_float = 3.24 #float(floating-point) 실수
a_string = "문자열" # "",'', str (string) 문자열
a_bool = True #True, False, bool(boolean)
a_NoneType = None #값이 없음

#int, float 사용 시 알아두면 유용한 것
population = 51_780_000 # 51780000과 완전히 같은 값
print(7 / 2)  # 3.5 → 일반 나눗셈 (항상 float로 결과가 나옴)
print(7 // 2) # 3 → 정수 나눗셈 (몫만, 소수점 버림)
print(7 % 2)  # 1  → 나머지 (짝수/홀수 판별, 순환 로직에 자주 씀)
print(2 ** 10)   # 1024  → 2의 10제곱


#부동소수점
print(0.1 + 0.2) # 예상 값 : 0.3, 실제 결과: 0.30000000000000004
# 이렇게 비교하면 안 됨
price = 0.1 + 0.2
print(price == 0.3)   # False! (0.30000000000000004 != 0.3)

# 방법 1: 반올림해서 비교
print(round(price, 1) == 0.3)   # True

# 방법 2: 정확한 소수 계산이 필요하면 decimal 모듈 사용 (실제 결제 로직에서 많이 씀)
price = Decimal("0.1") + Decimal("0.2")
print(price)   # 0.3 (정확하게 출력됨)


# type 사용법
type_age = 25
print(type(type_age))       # <class 'int'>

type_price = 9.99
print(type(type_price))     # <class 'float'>

type_name = "혜진"
print(type(type_name))      # <class 'str'>

type_is_valid = True
print(type(type_is_valid))  # <class 'bool'>

#형변환
# 문자열 → 정수
age_str = "25"
age_int = int(age_str)   # 25 (숫자로 변환됨)

# 정수 → 문자열
count = 10
count_str = str(count)   # "10" (문자열로 변환됨)

# 문자열 → 실수
price_str = "9.99"
price_float = float(price_str)  # 9.99

#여기서 int은 str 변환 안됨 `ValueError` 발생  형변환은 가능한 값만 바꿀 수 있다

