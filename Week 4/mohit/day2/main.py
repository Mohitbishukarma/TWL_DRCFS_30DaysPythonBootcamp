class Animal:
    def __init__(self, name:str, age:int, type_:str )-> None:
        self.name = name
        self.age = age
        self.type = type_
        self._ate = type_
    
    def __str__(self) -> str:
        return f"I Am {self.type}. I Am {self.age} yeArs old"
    
    def eat_food(self):
        return f"{self.name} has eaten food"


class Dog(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, 'DOG')


class Cat(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, 'CAT')


class Bird(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age, 'BIRD')


kAlu = Animal('kAlu', 5, 'DOG')
kAlu = Dog("kAlu", 4)
print(kAlu)

print(kAlu.eat_food())
