# if 조건문
age = 17 # age 변수 선언 및 17 저장

if age >= 19: #조건 1 : age가 19보다 크거나 같을 때 
    print("성인입니다")       # 조건이 참일 때 실행
else:
    print("미성년자입니다")   # 조건이 거짓일 때 실행
    
# elif
score = 85 # score변수 선언 및 85저장

if score >= 90: # score가 90보다 크거나 같을 때
    print("A등급")
elif score >= 80: # score가 80보다 크거나 같을 때
    print("B등급") 
elif score >= 70: # score가 70보다 크거나 같을 때
    print("C등급")
else: # 모든 조건이 만족하지 못할 때
    print("F등급")
    
#조건 1확인 후 조건 2에서 만족하기 때문에 나머지 조건은 확인 하지 않음.


#중첩 조건문 if안의if
has_ticket = True #has_ticket변수 선언 및 True 저장
height = 130 #height 변수 선언 및 130 저장

if has_ticket: #조건 1 : has_ticket이 true 일 시
    if height >= 120: #조건 1이 통과되어 입장이 됬지만 2번째 규정 height가 120보다 크거나 같을 때 
        print("입장 가능") 
    else: # 조건 1 통과 시 두번째 규정에서 조건에 만족하지 못할 시 
        print("보호자 동반 필요")
else: # 조건 1 미 통과 시 
    print("티켓을 구매하세요")
    
# 위 조건을 논리연산자를 활용 더 깔끔하게 작성
if has_ticket and height >= 120:
    print("입장 가능")
#두 조건이 참이여야 하기 때문에 이렇게 작성하면 가독성 좋은 코드 완성

# 한줄 if문 비추천
age = 20

# 한 줄 if문: 값을 만드는 게 아니라 그냥 실행만 함
if age >= 19: print("성인입니다")

# 지금까지 쓰던 여러 줄 방식과 완전히 같은 동작
if age >= 19:
    print("성인입니다")
    
# 삼항 연산자 
age = 20

# 기존 방식 (4줄)
if age >= 19:
    status = "성인"
else:
    status = "미성년자"

# 조건부 표현식 (1줄, 결과는 완전히 동일)
status = "성인" if age >= 19 else "미성년자"

#Truthy(참)와 Falsy(거짓)(자동 참/거짓 판별)
name = ""

if name:
    print(f"이름: {name}")
else:
    print("이름이 비어있습니다")   # 빈 문자열은 Falsy라서 여기 실행됨