
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

    def add_task(self):
        pass

    def mark_task(self):
        self.status = True

    def list_tasks(self):
        pass

    def __str__(self):
        desc = f"Описание: {self.description}, Срок: {self.deadline}, {'Выполнено' if self.status else 'Не выполнено'}"
        return desc


task1 = Task("Написать программу", "2024-04-20")
task2 = Task("Пройти курс по Python", "2024-07-31")
print(task1.__str__())
print(task2.__str__())
