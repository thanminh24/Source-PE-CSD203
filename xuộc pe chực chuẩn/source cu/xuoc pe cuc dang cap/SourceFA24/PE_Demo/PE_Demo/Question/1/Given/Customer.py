class Customer:
    def __init__(self, name="", age=-1):
        self.Name = name
        self.Age = age
    def __repr__(self):
        return f"({self.Name}, {self.Age})"    