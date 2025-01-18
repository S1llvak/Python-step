class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
       
     print(f"Ім'я: {self.name}, Зарплата: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
       
        super().__init__(name, salary)
        self.department = department

    def describe(self):
        
        super().describe()
        print(f"Відділ: {self.department}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
     
        super().__init__(name, salary)
        self.programming_language = programming_language

    def describe(self):
       
        super().describe()
        print(f"Мова програмування: {self.programming_language}")

if __name__ == "__main__":
    manager1 = Manager("Євген", 80000, "IT")
    developer1 = Developer("Владік", 6000, "Python")
    developer2 = Developer("Нікіта", 6500, "JavaScript")

    print("Інформація про працівників:")
    print("---------------------------")
    manager1.describe()
    print("---------------------------")
    developer1.describe()
    print("---------------------------")
    developer2.describe()