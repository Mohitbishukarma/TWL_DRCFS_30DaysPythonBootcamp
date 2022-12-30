# oop in python

class Workshop:
    var = 1


print(Workshop().var)

class animal:
    name = "Jarman Seford"
    age = 4
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"My name is {self.name} and my age is {self.age}"


print(animal.name)


a = animal("fyche",3)
