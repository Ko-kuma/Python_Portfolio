#Calculator.py(간단한 계산기 만들기)

#코드 실행시 출력될 문장
print("파이썬을 활용한 간단한 계산기")

#float형으로 입력 받을 실수형 변수(소숫점을 입력 받기 위해 )
num1 = float(input("첫 번째 숫자 입력 : "))
#연산자를 입력받을 문자열 변수
op = input("연산자 입력(+, -, *, /) :")
num2 = float(input("두 번째 숫자 입력 : "))

#if 조건문 비교연산자 == 사용
if op == "+" :
    print("결과 :", num1 + num2)

elif op == "-" :
    print("결과 :", num1 - num2)

elif op == "*" :
    print("결과 :", num1 * num2)

elif op == "/" :
    #if안의 if문 사용으로 오류 방지 및 num2의 값이 0일 때 오류 방지
    #ZeroDivisionError에러 방지용 
    if num2 == 0 :
        print("0으로 나눌 수 없습니다")
    
    else :
        print("결과 :", num1/ num2)

else :
    print("잘못된 연산자 입니다.")
