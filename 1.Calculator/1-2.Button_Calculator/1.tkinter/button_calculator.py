#버튼식 계산기.py

#tkinter 라이브러리 : GUI 프로그램 생성 가능 
import tkinter as tk
#tkinter 기능 중 messagebox의 팝업창 기능 가져오기
from tkinter import messagebox

#click_button 함수 생성
def click_button(value):
    #entry.get() : current_text변수가 입력된 코드의 입력값 가져오기
    current_text = entry.get()
    #entry.delete(0, tk.END) : 기존의 계산식의 삭제
    entry.delete(0, tk.END)
    #tk.END : 입력창의 맨 끝 위치에 넣어라 
    #insert : 지정위치에 문자열 삽입
    entry.insert(tk.END, current_text + value)

#clear_entr 함수 생성
def clear_entry():
    entry.delete(0, tk.END)

#calculate 함수 생성
def calculate():
    #예외처리
    try:
        expression = entry.get()
        # eval : 문자열을 코드로 실행
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    #Exception : Exception 추가로 해당 오류에 대한 정확한 오류 표기
    except Exception:
        #tkinter모듈의 messagebox 기능 오류를 팝업창화
        messagebox.showerror("오류", "계산식을 다시 확인하세요.")
        entry.delete(0, tk.END)


#tk.TK : GUI창 생성
root = tk.Tk()
#title : 창 이름
root.title("Tkinter 버튼 계산기")
#geometry : 가로x세로 크기
root.geometry("300x400")

#Entry : 입력창 생성
#font=("Arial", 24) : 글꼴 및 크기
#justify="right" : 오른쪽 정렬
entry = tk.Entry(root, font=("Arial", 24), justify="right")
#grid : 격자(표)형태로 위젯 배치, 행(row)과 열(column)을 이용해 위젯 배치
#row=0 : 0번째행, column=0 : 0번째 열, columnspan=4 : 4칸을 차지
#padx=10 : 좌우 여백, pady=10 : 상하 여백  
#sticky="nsew" :n = north  (위) s = south  (아래) e = east   (오른쪽) w = west   (왼쪽) 
#nsew 셀 전체를 꽉채워라, 셀 크기에 맞춰 늘어남 
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

#리스트 배치 별로 배치 
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

# enumerate() : 인덱스와 값을 동시에 반환
# row_index : 행 번호
# row : 현재 행의 데이터
for row_index, row in enumerate(buttons):
    # column_index : 열 번호
    # button_text : 버튼에 표시할 문자
    for column_index, button_text in enumerate(row):

        if button_text == "=":
            button = tk.Button(
                root,
                text=button_text,
                font=("Arial", 18),
                command=calculate
            )
        else:
            button = tk.Button(
                root,
                text=button_text,
                font=("Arial", 18),
                command=lambda value=button_text: click_button(value)
            )

        button.grid(
            row=row_index + 1,
            column=column_index,
            padx=5,
            pady=5,
            sticky="nsew"
        )

clear_button = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    command=clear_entry
)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.columnconfigure(i, weight=1)

for i in range(6):
    root.rowconfigure(i, weight=1)


root.mainloop()