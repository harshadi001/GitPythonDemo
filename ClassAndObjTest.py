
class calculator:
    num = 566   # class variable
    # calling default constructor
    def __init__(self,a, b):

        self.first = a
        self.second = b
        print("i am called automatically")

    def getdata(self):
        print("now Executing method in class")

    def summation(self):
        return self.first + self.second + calculator.num


obj = calculator(3, 8)
obj.getdata()
print(obj.summation())

obj1 = calculator(10, 2)
obj1.getdata()
print(obj1.num)