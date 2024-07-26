class calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b 

    def pow(self):
        return self.a ** self.b
        
a = float(input("Enter the number: "))
b = float(input("Enter the 2_number: "))        
q = input(": ")

obj = calc(a, b)

if q == 'add' or q == 'addison' or q == 'plus':
    print(obj.add())
elif q == 'sub' or q == 'substraction' or q == 'minus' :
    print(obj.sub())
elif q == 'mul' or q == 'multiplication' or q == 'multiply' :
    print(obj.mul())
elif q == 'div' or q == 'divison' or q == 'divide':
    print(obj.div())
else:
    print('error 404 not found')
