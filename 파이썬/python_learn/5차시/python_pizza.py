def circle_area(r,R):
    area1 = r**2*3.14*2
    area2 = R**2*3.14
    return area1, area2

x, y = circle_area(20,30)
print(x, y)
if x > y:
    print(x)
else:
    print(y)