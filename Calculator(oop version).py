from functools import reduce
class calculator:
    @staticmethod
    def add(*args):
        return sum(args)
    @staticmethod
    def multiply(*args):
        return reduce(lambda x,y : x*y,args)
    @staticmethod
    def divide(*args):
        return reduce(lambda x,y:x/y,args)
    @staticmethod
    def substract(*args):
        return reduce(lambda x,y:x-y,args)
print(calculator.add(5,10,4))
print(calculator.multiply(1,2,3,5))
print(calculator.divide(100,2))
print(calculator.substract(90,20,-50,43,7))