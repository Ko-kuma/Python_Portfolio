#반복문 (코드가 반복해서 실행되는 1회 단위는 iteration(이터레이션))

#임시변수 선언 및 리스트 값 꺼내기
for fruit in ["사과", "바나나", "포도"] :
    print(fruit)

#여기서 선언된 fruit는 임시변수 

#선언된 변수에 저장된 값 꺼내기
fruits = ["사과", "바나나", "포도"]

for fruit in fruits: # fruits 안의 값을 하나씩 꺼내서 fruit에 담음
    print(fruit)  # "사과" → "바나나" → "포도" 순서로 출력

#정해진 횟수만 반복(range)
for i in range(5):   # 0, 1, 2, 3, 4 다섯 번 반복
    print(i)  #인덱스는 0부터 시작 0~4까지 반복 

#세개의 인자 값으로 출력 
for i in range(2, 10, 2):   # 2부터 시작, 10 전까지, 2씩 증가
    print(i)  # 2, 4, 6, 8 출력

#문자열 순회
for char in "안녕":
    print(char)   # "안" → "녕" 순서로 출력
    

#순번과 값을 함께 꺼내기
fruits = ["사과", "바나나", "포도"]

#순번과 값을 함께 꺼내기 - enumerate
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 사과
# 1 바나나
# 2 포도              
#index는 임시변수일 뿐 구분하기 쉽게 하기 위해 index라고 한 것
#변수명이 어떤 것이든 상관없음 첫번째 변수가 가르키는 것은 enumerate임


#enumerate() 없이 순번을 직접 관리하면 번거로움
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1   # 매번 직접 1씩 증가시켜야 함
    
#중첩 반복문 
for i in range(1, 3):        # 바깥 반복: 1, 2
    for j in range(1, 3):    # 안쪽 반복: 각 i마다 1, 2
        print(i, j)
# 1 1
# 1 2
# 2 1
# 2 2


#조건이 참인동안 반복 while
count = 0

while count < 3:  # count가 3보다 작은 동안 계속 반복
    print(count)
    count += 1  # count = count + 1과 같음 (반복마다 1씩 증가)

#다른 예제
while True:   # 조건이 항상 True라 겉보기엔 무한 반복
    answer = input("종료하려면 q를 입력하세요: ")
    if answer == "q":
        break     # 조건을 만족하면 여기서 직접 빠져나감
    

#break문
users = ["철수", "영희", "혜진", "민수"]

for user in users:
    if user == "혜진":
        print(f"{user}님을 찾았습니다")
        break  # 찾은 순간 나머지는 확인할 필요 없으니 종료
    
#for-else / while-else
#반복문에도 `else`를 붙일 수 있는데, 이 `else`는 반복문이 `break`로 중간에 끊기지 않고 끝까지 다 돌았을 때만 실행


numbers = [1, 3, 5, 7]

for n in numbers:
    if n % 2 == 0:
        print("짝수 발견!")
        break
else:
    print("짝수가 없습니다") # break 없이 반복문이 끝까지 돌았으므로 실행됨
