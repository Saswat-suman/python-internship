# creating class
class Person:

    # __init__ to initialize all attributes
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # introduce method to print a staement about thre person
    def introduce(self):
        return (f"{self.name} is a {self.age} year old {self.gender}")
    
# creating a object of class Person and prinitng a statement about him/her
obj = Person("Saswat",19,"male")
print(obj.introduce())
