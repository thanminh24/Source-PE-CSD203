class Employee:
    def __init__(self, name="",age="", salary=-1):
        self.Name = name
        self.Age = age
        self.Salary = salary
    def __repr__(self):
        return f"({self.Name}, {self.Age}, {self.Salary})"    