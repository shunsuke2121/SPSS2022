class Calculator:
    def __init__(self):
        self.output = 0

    def add(self, a, b):
        return a+b

    def sub(self, a, b):
        return a-b

    def mul(self, a, b):
        return a*b

    def div(self, a, b):
        return a/b

    def calculation(self):
        a = int(input("1つ目の値を入力してください >"))
        calc = input("+,-,*,/ >")
        b = int(input("2つ目の値を入力してください >"))
     
     # calcによって演算方法を変える
        if calc =="+":
            self.output = self.add(a,b)
        
        if calc =="-":
            self.output = self.sub(a,b)
        
        if calc =="*":
            self.output = self.mul(a,b)
        
        if calc =="/":
            self.output = self.div(a,b)
        
        print(self.output)

calculator = Calculator()
calculator.calculation()