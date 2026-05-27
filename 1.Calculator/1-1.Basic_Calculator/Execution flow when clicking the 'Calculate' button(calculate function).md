```mermaid
graph TD
    Start([calculate 함수 시작]) --> GetInput[입력창에서 값 가져오기<br>entry_num1.get, entry_op.get, entry_num2.get]
    
    GetInput --> Convert[숫자 입력값을 float형으로 변환]
    
    Convert -- 변환 실패: ValueError --> ValueErr[에러 팝업창 출력<br>숫자를 올바르게 입력하세요]
    ValueErr --> End([함수 종료])
    
    Convert -- 변환 성공 --> CheckOp{연산자 확인}

    CheckOp -- "+" --> Add[result = num1 + num2]
    CheckOp -- "-" --> Sub[result = num1 - num2]
    CheckOp -- "*" --> Mul[result = num1 * num2]

    CheckOp -- "/" --> CheckZero{num2 == 0 ?}

    CheckZero -- Yes --> ZeroErr[결과 레이블 변경<br>0으로 나눌 수 없습니다]
    ZeroErr --> End

    CheckZero -- No --> Div[result = num1 / num2]

    CheckOp -- 그 외 문자 --> Invalid[결과 레이블 변경<br>잘못된 연산자 입니다]
    Invalid --> End

    Add --> ShowResult[결과 레이블 변경<br>결과 출력]
    Sub --> ShowResult
    Mul --> ShowResult
    Div --> ShowResult

    ShowResult --> End