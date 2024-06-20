class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius  #이게 없으면 c1, c2 같다고 인정 X
    
c1 = Circle(10)
c2 = Circle(10)

if c1 == c2:
    print('원의 반지름은 동일합니다.')

class Counter:
    def __init__(self, count):
        self.count = count
    def increment(self):
        self.count += 1
    def __str__(self):
        msg = '카운트값: '+ str(self.count)
        return msg

a = Counter(100)
print(a)

myList = [1,2,3,4]

if 2 in myList:  #__eq__() 메소드 호출됨.
    print(2)

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts['name'] = name
        self.contacts['mobile'] = mobile
        self.contacts['office'] = office
        self.contacts['email'] = email

    def __str__(self):
        content = f'{self.contacts['name']}\noffice phone: {self.contacts['office']}, email: {self.contacts['email']}'
        return content

obj = PhoneBook()
obj.add('kim',office='1234567', email='kim@company.com')
print(obj)