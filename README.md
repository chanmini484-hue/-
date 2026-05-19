#내 첫 중간고사 프로그램!
import random 
from datetime import datetime #나태한 저의 상태를 꺠우치기 위해 만든 프로그램이며 프로그램을 통해 동기 부여 가능한 문장들로 프로그램을 만들었습니다.

class taskmanager:
    def __init__(self):
        self.task = []
        self.quotes =[
            "현재는 과거에서 배우고 미래는 현재로부터 만들어지는 길이다.", "고독은 사람을 보게 만드는 중요한 상태이다." ,"어디로 가는지 생각하지 말고 지금의 길을 보자." 
            , "아름다움이란 추함이 있기에 인지가 가능한 대조 현상이다."
        ]      #import random으로 만든 무작위 명언 출력 프로그램입니다.
    
        def display_welcome(self):          #datetime 과 strftime 으로 현재 시간을 나타내도록 프로그램을 짰습니다.
            print("=" * 40)
            print(f"📅 현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"💡 오늘의 명언: {random.choice(self.quotes)}")
            print("=" * 40)

        def add_task(self):        #전역 함수로 입력값의 결과의 따라 다르게 출력 되도록 프로그램 짰습니다.
            task_name =  input("추가 할 일을 입력하세요!")
            self.task.append({"task": task_name, "done": False})
            print(f"✅ '{task_name}' 작업이 추가되었습니다!.")

        def view_task(self):           
            print("\n--- [할 일 목록 ] ---")
            if not self.tasks:
                print("비어있음")
                for i, item in enumerate(self.tasks, 1):
                    status = "[V]" if item["done"] else " []"
                    print(f"{i}. {item['task']}{status}")
                print("-" * 22)
            
            def complete_task(self):      #작업 완료 결과를 출력하는 함수입니다.
                self.view_tasks()
                try:
                    index = int(input("처리할 번호를 입력하세요!")) - 1
                    self.tasks[index]["done"] = True 
                    print("🎉 작업 완료! 고생하셨습니다!.")
                except (ValueError, IndexError):
                    print("잘 못 입력하셨습니다!")

            def run(self):
                self.display_welcome()
                while True:
                    print("\n1. 보기 | 2. 추가 | 3. 완료 | 4. 종료")
                    choice = input("메뉴 선택: ")

                    if choice == '1':
                        self.view_tasks()
                    elif choice == '2':
                        self.add_tasks()
                    elif choice == '3':
                        self.complete_tasks()
                    elif choice == '4':
                        print("프로그램을 종료합니다. 고생하셨습니다!")
                        break
                    else:
                        print("올바른 버튼을 입력해주세요!")

                        #프로그램 실행 
                        # if __name__ == "__main__":
                        # app = TasksManager()
                        # app.run
                        # 참고 부탁드리겠습니다! 
****
