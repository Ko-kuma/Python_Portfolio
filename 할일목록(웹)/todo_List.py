#todo_list.py
#할 일 목록 전체를 관리하는 클래스 

#Task.py의 Task 기능 가져오기
from task import Task
 
 
class todoList:
    def __init__(self):
        self.tasks = []   # Task 인스턴스를 담는 리스트 
    def add_task(self, title):
        """새 할 일을 추가하고, 추가된 Task를 반환한다."""
        new_task = Task(title)
        self.tasks.append(new_task)   # 리스트 메서드 append
        return new_task
 
    def complete_task(self, index):
        """번호로 지정한 할 일을 완료 처리한다. 성공하면 True, 없는 번호면 False를 반환."""
        try:
            self.tasks[index].done = True   # 인덱싱으로 접근 
            return True
        except IndexError:                    # 없는 번호를 입력한 경우 (Day8 예외처리)
            return False
 
    def remove_task(self, index):
        """번호로 지정한 할 일을 삭제하고, 삭제된 Task를 반환한다. 없는 번호면 None을 반환."""
        try:
            return self.tasks.pop(index)   # pop()은 삭제하면서 값을 반환 
        except IndexError:
            return None
 