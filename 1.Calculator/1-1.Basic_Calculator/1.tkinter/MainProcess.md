```mermaid
graph TD
    A([시작]) --> B[라이브러리 불러오기 <br> tkinter, messagebox]
    B --> C[calculate 함수 정의]
    C --> D[메인 창 설정 <br> 제목: 간단한 GUI 계산기 <br> 크기: 400x300]
    D --> E[화면 위젯 배치 <br> 입력창 3개, 버튼, 결과 레이블]
    E --> F[창 실행 및 대기 <br> window.mainloop]
    F --> G([종료])