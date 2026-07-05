#산술 연산자
price = 1000 # price 변수 선언 및 1000저장
quantity = 3 #quantity 변수 선언 및 3 저장
total = price * quantity #total 변수 선언 및 price * quantity값의 곱한 값 저장
print(total) # 3000

#비교 연산자 
age = 20 # age변수 선언 및 20 저장
print(age >= 18) #True, age가 18보다 크거나 같다.

print(1=="1") #Fasle, 이유는 정수와 문자열이여서 값이 다르기 때문

#논리 연산자 
height = 130 #height 변수 선언 및 130 저장
weight = 45 # weight 변수 선언 및 45 저장
can_ride = height >= 120 and weight <= 100 # height가 120보다 크거나 같을 때 그리고 weight가 100보다 작거나 같을 때
print(can_ride) #True, 두값이 모두 참 조건이기 때문

#멤버십 연산자
fruits = ["사과", "바나나", "포도"] #fruits변수 선언 및 리스트 저장 
#리스트는 아직 배우지 않은 개념이다.
#리스트는 0부터 시작한다는 걸 알고 있자
#코드에 보이는 리스트가 3이라고 해서 포도가 3이 아니다
#사과부터 0~2의 인덱스를 가지고 있다

print("사과"in fruits) # True , 해당 리스트 안에 포함
print("수박" not in fruits) # True, 해당 리스트안에 미포함

