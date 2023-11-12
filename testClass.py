class Circle(object):  # 继承了object()的属性；
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return self.r**2*self.pi


circle1 = Circle(1)
print(circle1.r)
print(circle1.get_area())
