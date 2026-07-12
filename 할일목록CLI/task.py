#Task.py
#할 일 하나를 나타내는 클래스

class Task :
    def __init__(self, title, done=False) :
        #인스턴스 변수 : 현재 할 일의 제목
        self.title = title
        # 인스턴스 변수 : 완료 여부(bool 플래그)
        self.done = done
        
    def __str__(self):
        #print(task)했을 때 사람이 읽기 쉬운 형태로 
        status = "v" if self.done else " "
        return f"[{status}] {self.title}"

    def to_dict(self) :
        return {"title" : self.title, "done" : self.done}
    