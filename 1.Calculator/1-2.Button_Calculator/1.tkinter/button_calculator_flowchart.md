# 버튼식 계산기 순서도

```mermaid
flowchart TD
    A([프로그램 시작]) --> B[tkinter, messagebox 불러오기]

    B --> C[click_button 함수 정의]
    C --> D[clear_entry 함수 정의]
    D --> E[calculate 함수 정의]

    E --> F[메인 GUI 창 생성]
    F --> G[창 제목 설정]
    G --> H[창 크기 설정]

    H --> I[Entry 입력창 생성]
    I --> J[Entry를 grid로 배치]

    J --> K[buttons 2차원 리스트 생성]

    K --> L[바깥 for문: 행 row 꺼내기]
    L --> M[안쪽 for문: 열 button_text 꺼내기]

    M --> N{button_text가 = 인가}

    N -- 예 --> O[= 버튼 생성]
    N -- 아니오 --> P[숫자/연산자 버튼 생성]

    O --> Q[button.grid로 버튼 배치]
    P --> Q

    Q --> R{모든 버튼 생성 완료}
    R -- 아니오 --> M
    R -- 예 --> S[C 버튼 생성]

    S --> T[C 버튼 grid 배치]
    T --> U[열 크기 비율 설정]
    U --> V[행 크기 비율 설정]

    V --> W[root.mainloop 실행]
    W --> X{사용자 버튼 클릭}

    X --> Y{클릭한 버튼 종류}

    Y -- 숫자/연산자 --> Z[click_button 실행]
    Z --> Z1[Entry 기존 값 가져오기]
    Z1 --> Z2[Entry 삭제]
    Z2 --> Z3[기존 값과 새 값 삽입]
    Z3 --> W

    Y -- C 버튼 --> C1[clear_entry 실행]
    C1 --> C2[Entry 전체 삭제]
    C2 --> W

    Y -- = 버튼 --> E1[calculate 실행]
    E1 --> E2[Entry 계산식 가져오기]
    E2 --> E3[eval로 계산 실행]
    E3 --> E4{계산 성공}

    E4 -- 예 --> E5[Entry 삭제 후 결과 삽입]
    E5 --> W

    E4 -- 아니오 --> E6[messagebox 오류 팝업]
    E6 --> E7[Entry 삭제]
    E7 --> W