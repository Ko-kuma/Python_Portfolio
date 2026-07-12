#할 일 목록을 파일에 저장하고 불러오는 기능

#표준 라이브러리 모듈 
#파이썬은 {}를 딕셔너리로 인식하기 때문에 json모듈을 불러올 필요가 있음
import json 

from task import Task

FILENAME = "tasks.json"

def save_tasks(tasks, filename=FILENAME) :
    """할 일 목록(task 리스트)을 json 파일로 저장"""
    data = []
    # 반복문으로 각 task를 딕셔너리로 변환
    for task in tasks :
        data.append(task.to_dict())
    
    #with문으로 파일 쓰기    
    with open(filename, "w", encoding="utf-8") as f : 
        #한글 깨짐 방지 + 보기 좋게 들여쓰기
        json.dump(data, f, ensure_ascii = False, indent =2 )
        
def load_tasks(filename=FILENAME) :
    """저장된 JSON파일에서 할 일 목록을 불러온다. 파일이 없으면 빈 목록으로 시작"""
    
    tasks = []
    try :
       with open(filename, "r", encoding= " utf-8") as f:
           data = json.load(f)
           #딕셔너리 목록을 다시 Task 인스턴스로 변환
           for item in data :
               tasks.append(Task(item["title"], item["done"]))
    
    #첫 실행시 파일이 없는 경우 에러 방지
    except FileNotFoundError :
        print("저장된 할 일 목록이 없습니다. 새로 시작합니다.")
        
    return tasks

                   
               