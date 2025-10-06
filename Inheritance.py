from ClassAndObjTest import calculator

class Childcls(calculator):
      num2 = 200

      def __init__(self):
          calculator.__init__(self,3, 10)

      def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = Childcls()
print(obj.getCompleteData())