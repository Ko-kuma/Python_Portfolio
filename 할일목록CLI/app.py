# app.py
# 웹(브라우저) 버전 진입점 — Streamlit이 HTML/CSS/JS로 자동 변환해주는 부분.
# todo_list.py, storage.py를 그대로 재사용한다.
# 화면에 뭘 어떻게 보여줄지만 다를 뿐, 할 일을 추가/삭제/완료하는 로직은 동일하다.

import streamlit as st
from todo_List import todoList
from storage import save_tasks, load_tasks

st.set_page_config(page_title="할 일 목록", page_icon="📝")
st.title("📝 할 일 목록")

# st.session_state: 브라우저에서 버튼을 누를 때마다 이 파일 전체가 다시 실행되는데,
# 그때마다 todo 데이터가 초기화되지 않도록 세션에 저장해두는 저장소.
# (클래스와 파일 입출력에서 배운 "프로그램 종료 시 변수가 사라지는 문제"와 비슷한 문제를, Streamlit은 session_state로 해결한다)
if "todo" not in st.session_state:
    st.session_state.todo = todoList()
    st.session_state.todo.tasks = load_tasks()

todo = st.session_state.todo   # 매번 새로 안 만들고, 세션에 저장된 걸 그대로 씀

# ---- 할 일 추가 ----
new_task = st.text_input("새로운 할 일을 입력하세요")
if st.button("추가"):
    if new_task:                       # 빈 문자열이면 추가하지 않음 (Truthy/Falsy, Day3)
        todo.add_task(new_task)          # CLI와 완전히 동일한 메서드 재사용
        save_tasks(todo.tasks)
        st.rerun()                        # 화면을 새로 그려서 방금 추가한 항목이 바로 보이게 함

st.divider()

#할 일 목록 표시
if not todo.tasks:
    st.write("할 일이 없습니다.")
else:
    for index, task in enumerate(todo.tasks):   # enumerate로 순번+값 동시 추출
        col1, col2, col3 = st.columns([1, 6, 2])   # 화면을 세 칸으로 나눔: 체크박스 / 제목 / 삭제버튼

        with col1:
            checked = st.checkbox("", value=task.done, key=f"done_{index}")
            if checked != task.done:            # 체크 상태가 바뀌었을 때만 반영
                # 체크박스는 켜고/끄고 양방향이 다 필요해서, 한 방향만 처리하는
                # complete_task() 대신 속성을 직접 바꾼다 (CLI는 "완료 처리"만 있으면 충분했음)
                task.done = checked
                save_tasks(todo.tasks)
                st.rerun()

        with col2:
            if task.done:
                st.markdown(f"~~{task.title}~~")   # 완료된 항목은 취소선으로 표시
            else:
                st.markdown(task.title)

        with col3:
            if st.button("삭제", key=f"del_{index}"):
                todo.remove_task(index)             # CLI와 완전히 동일한 메서드 재사용
                save_tasks(todo.tasks)
                st.rerun()