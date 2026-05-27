#Gui_Calculator.py

#파이썬의 기본 gui 생성 라이브러리 
#as는 별칭 tk 라는 별칭으로 불러들이기 쉽게 만듬 
import tkinter as tk
#tkinter의 기능 중 messagebox만 불러옴
from tkinter import messagebox

# 계산 함수
def calculate():
    #예외처리 
    try:
        #.get : entrty 입력 창에서 사용자의 입력문자 가져오기
        num1 = float(entry_num1.get())
        op = entry_op.get()
        num2 = float(entry_num2.get())

        if op == "+":
            result = num1 + num2

        elif op == "-":
            result = num1 - num2

        elif op == "*":
            result = num1 * num2

        elif op == "/":
            #ZeroDivisionError에러 방지용 
            if num2 == 0:
                #text는 화면에 표시할 문자열 
                result_label.config(text="0으로 나눌 수 없습니다")

                return

            else:
                result = num1 / num2

        else:
            result_label.config(text="잘못된 연산자 입니다.")
            return
        
        # .config()
        # 이미 생성된 Label의 글자를 수정함
        result_label.config(text=f"결과 : {result}")

    #ValueError(값 변환 과정 오류)
    except ValueError:
        #messagebox를 불러옴 
        #.showerror로 messagebox에 오류 메시지 팝업창을 띄움
        messagebox.showerror("에러", "숫자를 올바르게 입력하세요")


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
        