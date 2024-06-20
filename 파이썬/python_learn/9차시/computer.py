class Computer():
    
    def __init__(self,brand,OS,RAM):
        self.brand = brand
        self.OS = OS
        self.RAM = RAM

    def display(self,price):
        print(f'회사명 : {self.brand}, 운영 체제 : {self.OS}, 메모리용량 : {self.RAM}, 가격 : ${price}')
    
computer1 = Computer('ASUS', 'Window', '16GB')
computer1.display(2000)