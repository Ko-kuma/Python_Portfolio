#예외처리 기본 구조
try:
    age = int("스물다섯")   # 문자열을 숫자로 못 바꿔서 에러 발생
    print(age)
except:
    print("숫자로 변환할 수 없습니다")   # 에러가 나면 여기가 실행됨

print("프로그램은 계속 진행됩니다")   # try/except 덕분에 여기까지 도달함

#지금까지 연습의 오류들 예외처리로 해결
data = {"name": "혜진"}

try:
    print(data["age"])
except KeyError:                # 딕셔너리에 없는 key로 접근할 때 나는 에러
    print("해당 key가 없습니다")

numbers = [1, 2, 3]
try:
    print(numbers[10])
except IndexError:              # 리스트 범위를 벗어난 인덱스로 접근할 때 나는 에러
    print("인덱스 범위를 벗어났습니다")

try:
    result = 10 / 0
except ZeroDivisionError:       # 0으로 나눌 때 나는 에러
    print("0으로 나눌 수 없습니다")
    
    
#예외 처리의 올바른 구조

try:
    value = int("abc")
except Exception:   # 상위 범주를 먼저 써버림
    print("일반 에러")
except ValueError:  # 절대 여기까지 도달 못 함, 위에서 이미 다 잡혔음
    print("값 에러")

# 올바른 순서
try:
    value = int("abc")
except ValueError:          # 구체적인 것부터 먼저 확인
    print("값 에러")
except Exception:            # 나머지는 여기서 처리
    print("일반 에러")
    
    
#as 에러메시지 직접 확인 
try:
    age = int("스물다섯")
except ValueError as e:
    print(f"에러 발생: {e}")   # 에러 발생: invalid literal for int() with base 10: '스물다섯'


#else-try : else에러가 안났을때만 실행

try:
    age = int("25")
except ValueError:
    print("숫자 형식이 아닙니다")
else:
    print(f"변환 성공: {age}살")   # 에러가 안 났을 때만 실행
    
#finally 실행되든 안되든 항상 실행
try:
    file_content = "파일 내용을 읽는 중..."
    print(file_content)
except Exception as e:
    print(f"에러: {e}")
finally:
    print("작업 종료")   # 성공하든 실패하든 항상 출력됨
    
#raise 예외 직접 발생

def set_age(age):
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없습니다")   # 직접 에러를 발생시킴
    return age

set_age(-5)   # ValueError: 나이는 음수가 될 수 없습니다

#예외처리 커스텀해보기
class InsufficientBalanceError(Exception):   # 나만의 에러 종류 정의
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("잔액이 부족합니다")
    return balance - amount

try:
    withdraw(1000, 5000)
except InsufficientBalanceError as e:
    print(e)   # 잔액이 부족합니다
    
#트레이스백 읽는 법은 자료 참고