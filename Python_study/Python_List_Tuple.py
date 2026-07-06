# list

fruits = ["사과", "바나나", "포도"]
# [] 리스트를 만들고 , 로 구분

# indexing 순서로 값 꺼내기(인덱스는 0부터 시작)
# 값을 추출하는 행위를 인덱싱이라 하는 것 
fruits = ["사과", "바나나", "포도"]
print(fruits[0]) #사과   
print(fruits[1]) #바나나
# 음수 인덱스는 맨뒤에서부터 시작 
print(fruits[-1]) #포도(fruits[2]도 동일 값)

# 값 추가/삭제/ 수정
fruits = ["사과", "바나나", "포도"]
fruits.append("수박") # 맨뒤에 값을 추가
#fruits = ["사과", "바나나", "포도","수박"]
print(fruits[3])# 수박
fruits.remove("바나나")#값으로 찾아서 삭제
#fruits = ["사과","포도","수박"]
print(fruits) #["사과","포도","수박"]
fruits[0] = "딸기" #인덱스 값 수정
#fruits = ["딸기","포도","수박"]
print(fruits) #["딸기","포도","수박"]

# Slicing 일부만 잘라내기
numbers = [10, 20, 30, 40, 50]
print(numbers[1:3])#1번 인덱스 부터 3번인덱스전까지
#[20, 30]
print(numbers[:2]) #처음부터 2번인덱스 전까지
#[10, 20]
print(numbers[2:]) #2번인덱스 부터 마지막 인덱스까지 
#[30, 40, 50]

# len() 리스트의 개수 세기
fruits =["사과","바나나","포도"]
print(len(fruits))

#len 함수는 리스트에서만 사용하는게 아닌 여러 함수에서도 글자 수나 항목개수 반환으로 많이 사용

#끼워넣기, 반환 및 삭제, 오름차순 정렬, 값이 몇개 있는지, 값이 몇번째인덱스에 있는지
numbers = [3,1,4,1,5]

numbers.insert(0,100) # 0번 인덱스에 100을 끼워 넣기 
# 0번에 100이가면서 인덱스가 한칸씩 밀림
print(numbers)# [100, 3, 1, 4, 1, 5]
numbers.pop() # 맨 뒤 값을 꺼내면서 삭제 → 5가 반환되고 리스트에서 사라짐
print(numbers)# [100, 3, 1, 4, 1]
numbers.sort()# 오름차순 정렬
print(numbers)# [1, 1, 3, 4, 100]
numbers.count(1) # 값이 몇개 있는지 셈
print(numbers.count(1)) # 2
numbers.index(4) # 값이 몇 번째 인덱스에 있는지 찾음
print(numbers.index(4)) # 3

#pop과 remove의 차이는 무엇을 지우는가의 차이도 있지만 반환값의 차이도 있음
#자세한 내용은 블로그 참조

#중첩 리스트
grid=[[1,2,3],[4,5,6]]
print(grid[0]) #[0번째 행 전체의 값 출력]
#[1,2,3]
print(grid[0][1]) # [0번째 행 1번째 인덱스 출력]
#[2]


#튜플 - 튜플은 불변 Immutable을 기억
point = (3, 5)   # 소괄호 ( )로 튜플을 만듦
print(point[0])   # 3 (인덱싱은 리스트와 동일하게 사용 가능)

#point[0] = 10     # TypeError, 튜플이 수정 불가능한 값 이기 때문

#튜플 언패킹 
point = (3, 5)
x, y = point   # 튜플 안의 값을 각각 x와 y에 나눠 담음
print(x)   # 3
print(y)   # 5

#튜플 변환 
point = (3, 5)
point = point + (7,)   # (3, 5, 7)
print(point) #새로운 튜플 생성

#튜플변환 리스트 변환 후 다시 튜플로 변환
point = (3, 5)
 
point_list = list(point)   # 튜플 → 리스트로 변환 (이제 수정 가능해짐)
point_list[0] = 10          # 리스트니까 인덱스로 수정 가능
point = tuple(point_list)   # 다시 리스트 → 튜플로 변환
 
print(point)   # (10, 5)