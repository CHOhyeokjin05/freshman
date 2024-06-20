class CoffeeMenu():

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def disp_info(self):
        print(f'Name: {self.name}\nPrice: {self.price}원')

coffee1 = CoffeeMenu('Espresso', 3000)
coffee1.disp_info()

coffee2 = CoffeeMenu('아이스아메리카노', 2500)
coffee2.disp_info()

coffee3 = CoffeeMenu('까페라떼', 4000)
coffee3.disp_info()