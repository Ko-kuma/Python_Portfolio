#Gui_Calculator.py

#파이썬의 기본 gui 생성 라이브러리 
#as는 별칭 tk 라는 별칭으로 불러들이기 쉽게 만듬 
import tkinter as tk


# [수정] 실제 계산만 담당하는 함수를 따로 만들었습니다.
# [수정 이유] 버튼 클릭 처리 함수(calculate)가 입력, 계산, 출력까지 모두 담당하면 길어지기 때문에
# 계산 규칙을 별도 함수로 분리해서 읽기 쉽고 수정하기 쉽게 만들었습니다.
def calculate_result(num1, op, num2):
    if op == "+":
        return num1 + num2, None

    elif op == "-":
        return num1 - num2, None

    elif op == "*":
        return num1 * num2, None

    elif op == "/":
        # [오류 방지] num2가 0이면 나눗셈 과정에서 ZeroDivisionError가 발생할 수 있습니다.
        # [수정 이유] 계산 전에 0인지 확인해서 프로그램이 멈추지 않고 안내 문구를 보여주기 위해서입니다.
        if num2 == 0:
            return None, "0으로 나눌 수 없습니다"

        return num1 / num2, None

    # [오류 방지] +, -, *, / 이외의 연산자는 계산할 수 없습니다.
    # [수정 이유] 사용자가 잘못 입력한 이유를 결과 영역에 알려주기 위해서입니다.
    return None, "잘못된 연산자 입니다."

# 계산 함수
def calculate():
    #예외처리
    try:
        #.get : entrty 입력 창에서 사용자의 입력문자 가져오기
        num1 = float(entry_num1.get())

        # [오류 가능성] 연산자 앞뒤에 공백이 있으면 "+"와 " +"를 서로 다른 값으로 판단합니다.
        # [수정] strip()으로 앞뒤 공백을 제거했습니다.
        # [수정 이유] 사용자가 실수로 공백을 입력해도 올바른 연산자로 처리하기 위해서입니다.
        op = entry_op.get().strip()

        num2 = float(entry_num2.get())

    #ValueError(값 변환 과정 오류)
    except ValueError:
        # [오류 가능성] 숫자가 아닌 값을 입력하면 float() 변환 과정에서 ValueError가 발생합니다.
        # [수정] 오류 팝업 대신 결과 라벨에 안내 문구를 표시합니다.
        # [수정 이유] 0 나누기, 잘못된 연산자, 숫자 입력 오류를 같은 위치에 보여줘서 사용자가 덜 헷갈리게 하기 위해서입니다.
        result_label.config(text="숫자를 올바르게 입력하세요")
        return

    result, error_message = calculate_result(num1, op, num2)

    if error_message:
        #text는 화면에 표시할 문자열
        result_label.config(text=error_message)
        return

    # .config()
    # 이미 생성된 Label의 글자를 수정함
    # [수정] :g 형식을 사용했습니다.
    # [수정 이유] 3.0처럼 불필요한 소수점이 붙는 경우를 줄여 결과를 더 자연스럽게 보여주기 위해서입니다.
    result_label.config(text=f"결과 : {result:g}")


# GUI 창 생성
#tk 별칭 .TK()메인창 생성
window = tk.Tk()

#창의 제목(.title)
window.title("간단한 GUI 계산기")

#.geometry(창 크기 설정)
window.geometry("400x300")


# 첫 번째 숫자 입력
# Label : GUI 화면에 글자를 출력하는 기능
# 콘솔의 print()와 비슷하지만 GUI 창 내부에 출력됨
label1 = tk.Label(window, text="첫 번째 숫자")
# .pack()
# GUI 요소를 화면에 배치(출력)하는 기능
label1.pack()

# Entry
# 사용자가 값을 입력할 수 있는 입력창 생성
entry_num1 = tk.Entry(window)
entry_num1.pack()


# 연산자 입력
label2 = tk.Label(window, text="연산자 (+, -, *, /)")
label2.pack()

entry_op = tk.Entry(window)
entry_op.pack()


# 두 번째 숫자 입력
label3 = tk.Label(window, text="두 번째 숫자")
label3.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()


# 계산 버튼
# Button
# 클릭 가능한 버튼 생성

# command=calculate
# 버튼 클릭 시 calculate() 함수 실행
calc_button = tk.Button(window, text="계산하기", command=calculate)
#pady는 공백(여백) 10칸
calc_button.pack(pady=10)


# 결과 출력
result_label = tk.Label(window, text="결과 : ")
result_label.pack()


# GUI 실행
# mainloop()
# GUI 창이 계속 실행되도록 무한 대기 상태 유지
window.mainloop()
        
