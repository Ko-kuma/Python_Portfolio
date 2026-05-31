#버튼식 계산기.py

# ast/operator를 사용하는 이유:
# 기존 eval()은 입력된 문자열을 Python 코드로 그대로 실행하기 때문에 계산기에는 위험합니다.
# ast로 식을 분석하고, 사칙연산 노드만 직접 계산하면 허용한 계산만 실행할 수 있습니다.
import ast
import operator

#tkinter 라이브러리 : GUI 프로그램 생성 가능
import tkinter as tk
#tkinter 기능 중 messagebox의 팝업창 기능 가져오기
from tkinter import messagebox


OPERATORS = "+-*/"
ALLOWED_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}
ALLOWED_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def set_entry_text(text):
    # Entry를 읽기 전용으로 유지하는 이유:
    # 사용자가 키보드로 Python 코드를 직접 입력하는 일을 막고, 버튼 입력만 받기 위해서입니다.
    entry.config(state="normal")
    entry.delete(0, tk.END)
    entry.insert(tk.END, text)
    entry.config(state="readonly")


def get_current_number(expression):
    # 현재 숫자에 소수점이 이미 있는지 확인하기 위해 마지막 연산자 뒤의 숫자만 가져옵니다.
    last_operator_index = -1
    for index, char in enumerate(expression):
        if char in OPERATORS:
            last_operator_index = index

    return expression[last_operator_index + 1:]


#click_button 함수 생성
def click_button(value):
    #entry.get() : current_text변수가 입력된 코드의 입력값 가져오기
    current_text = entry.get()

    if value in OPERATORS:
        # 빈 입력에서 *, /, + 로 시작하면 계산식이 성립하지 않으므로 입력을 막습니다.
        # - 는 음수 입력을 위해 예외로 허용합니다.
        if not current_text:
            if value == "-":
                set_entry_text(value)
            return

        # 연산자가 연속으로 입력되면 오류가 나기 쉬우므로 마지막 연산자를 새 연산자로 교체합니다.
        if current_text[-1] in OPERATORS:
            set_entry_text(current_text[:-1] + value)
            return

    if value == ".":
        current_number = get_current_number(current_text)

        # 한 숫자 안에 소수점이 여러 번 들어가면 잘못된 식이 되므로 중복 입력을 막습니다.
        if "." in current_number:
            return

        # .5 같은 입력은 계산 전에 0.5 형태로 바꿔서 사용자가 보기에도 명확하게 만듭니다.
        if not current_text or current_text[-1] in OPERATORS:
            current_text += "0"

    set_entry_text(current_text + value)


#clear_entry 함수 생성
def clear_entry():
    set_entry_text("")


def evaluate_node(node):
    # bool도 int의 하위 타입이므로 True/False가 숫자로 처리되지 않게 별도로 제외합니다.
    if (
        isinstance(node, ast.Constant)
        and isinstance(node.value, (int, float))
        and not isinstance(node.value, bool)
    ):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_BINARY_OPERATORS:
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        return ALLOWED_BINARY_OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_UNARY_OPERATORS:
        operand = evaluate_node(node.operand)
        return ALLOWED_UNARY_OPERATORS[type(node.op)](operand)

    # 숫자와 사칙연산 외의 문법은 모두 차단합니다.
    raise ValueError("허용되지 않은 계산식입니다.")


def safe_calculate(expression):
    # eval() 대신 ast.parse()를 사용하는 이유:
    # 문자열을 코드로 실행하지 않고, 계산식 구조만 확인한 뒤 허용된 노드만 계산하기 위해서입니다.
    parsed_expression = ast.parse(expression, mode="eval")
    return evaluate_node(parsed_expression.body)


#calculate 함수 생성
def calculate():
    expression = entry.get()

    # 빈 값에서 = 버튼을 눌렀을 때 오류 팝업이 뜨지 않도록 조용히 무시합니다.
    if not expression:
        return

    # 마지막 글자가 연산자이면 아직 계산식이 완성되지 않은 상태입니다.
    if expression[-1] in OPERATORS:
        messagebox.showerror("오류", "계산식을 완성한 뒤 다시 시도하세요.")
        return

    #예외처리
    try:
        result = safe_calculate(expression)

        if isinstance(result, float) and result.is_integer():
            result = int(result)

        set_entry_text(str(result))
    except (SyntaxError, ValueError, ZeroDivisionError):
        #tkinter모듈의 messagebox 기능 오류를 팝업창화
        messagebox.showerror("오류", "계산식을 다시 확인하세요.")
        set_entry_text("")


def main():
    # main()으로 감싸는 이유:
    # 다른 파일에서 이 모듈을 import할 때 계산기 창이 바로 실행되지 않게 하기 위해서입니다.
    global root, entry

    #tk.TK : GUI창 생성
    root = tk.Tk()
    #title : 창 이름
    root.title("Tkinter 버튼 계산기")
    #geometry : 가로x세로 크기
    root.geometry("300x400")

    #Entry : 입력창 생성
    #font=("Arial", 24) : 글꼴 및 크기
    #justify="right" : 오른쪽 정렬
    entry = tk.Entry(root, font=("Arial", 24), justify="right", readonlybackground="white")
    entry.config(state="readonly")
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


if __name__ == "__main__":
    main()
