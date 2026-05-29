#Calculator.py(간단한 계산기 만들기)


# [수정] 계산 로직을 별도 함수로 분리했습니다.
# [수정 이유] 입력을 받는 부분과 실제 계산하는 부분을 나누면 코드가 더 읽기 쉽고,
# 나중에 GUI 계산기에서도 같은 계산 규칙을 확인하거나 수정하기 쉬워집니다.
def calculate_result(num1, op, num2):
    #if 조건문 비교연산자 == 사용
    if op == "+":
        return num1 + num2, None

    elif op == "-":
        return num1 - num2, None

    elif op == "*":
        return num1 * num2, None

    elif op == "/":
        # [오류 방지] 기존 코드처럼 0으로 나누면 ZeroDivisionError가 발생할 수 있습니다.
        # [수정 이유] 계산 전에 num2가 0인지 먼저 확인해서 프로그램이 멈추지 않게 합니다.
        if num2 == 0:
            return None, "0으로 나눌 수 없습니다"

        else:
            return num1 / num2, None

    else:
        # [오류 방지] +, -, *, / 이외의 값을 입력하면 계산할 수 없습니다.
        # [수정 이유] 잘못된 연산자를 입력했을 때 사용자에게 이유를 알려주기 위해 메시지를 반환합니다.
        return None, "잘못된 연산자 입니다."


#코드 실행시 출력될 문장
print("파이썬을 활용한 간단한 계산기")

# [오류 가능성] 기존 코드는 숫자가 아닌 값을 입력하면 ValueError로 프로그램이 바로 종료될 수 있었습니다.
# [수정] 숫자 입력과 계산 실행을 try/except로 감쌌습니다.
# [수정 이유] 잘못된 입력을 하더라도 사용자에게 안내 메시지를 보여주고 안전하게 종료하기 위해서입니다.
try:
    #float형으로 입력 받을 실수형 변수(소숫점을 입력 받기 위해 )
    num1 = float(input("첫 번째 숫자 입력 : "))

    # [오류 가능성] 연산자 앞뒤에 공백이 있으면 "+"와 " +"를 서로 다른 값으로 판단합니다.
    # [수정] strip()으로 앞뒤 공백을 제거했습니다.
    # [수정 이유] 사용자가 실수로 공백을 입력해도 올바른 연산자로 처리하기 위해서입니다.
    op = input("연산자 입력(+, -, *, /) :").strip()

    num2 = float(input("두 번째 숫자 입력 : "))

    result, error_message = calculate_result(num1, op, num2)

    # [수정] 계산 함수가 결과와 오류 메시지를 함께 반환하도록 했습니다.
    # [수정 이유] 계산 성공(result)과 계산 실패(error_message)를 명확하게 구분하기 위해서입니다.
    if error_message:
        print(error_message)

    else:
        # [수정] :g 형식을 사용했습니다.
        # [수정 이유] 3.0처럼 불필요한 소수점이 붙는 경우를 줄여 결과를 더 자연스럽게 보여주기 위해서입니다.
        print(f"결과 : {result:g}")

except ValueError:
    print("숫자를 올바르게 입력하세요")
