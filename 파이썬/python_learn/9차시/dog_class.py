class Dog:
    def __init__(self,weight,color,name):  #생성자 메소드
        self.weight = weight
        self.color = color
        self.name = name

    def bark(self):
        print('멍멍')

dog1 = Dog(20, 'white', 'bobby')

dog1.bark()
print(dog1.weight, dog1.color, dog1.name)