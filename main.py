
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

    def mark_task(self):
        self.status = True

    def __str__(self):
        desc = f"Описание: {self.description}, Срок: {self.deadline}, {'Выполнено' if self.status else 'Не выполнено'}"
        return desc


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_task()
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

    def show_current_tasks(self):
        print("Текущие задачи:")
        for task in self.tasks:
            if not task.status:
                print(task)


task_manager = TaskManager()
task_manager.add_task(Task("Написать программу", "2024-04-20"))
task_manager.add_task(Task("Пройти курс по Python", "2024-07-31"))

task_manager.show_current_tasks()

task_manager.mark_task_completed("Написать программу")
task_manager.show_current_tasks()

