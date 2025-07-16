from abc import ABC , abstractmethod
from time_manage import teme

class Calculator(ABC): 
    def __init__(self , name):
        self.name = name
        
    @abstractmethod
    def SelectOption(self): 
        pass

class Casio(Calculator): 
    def __init__(self , name ): 
        super().__init__(name )
        
    @teme   
    def SelectOption(self):
        o = input("Please select from the following options [ + - *] :  ")
        if o == "+" : 
            x = int(input("n1 : "))
            y = int(input("n2 : "))
            print( x + y)
            return o
        if o == "-" : 
            x = int(input("n1 : "))
            y = int(input("n2 : "))
            print( x - y)
        if o == "*" : 
            x = int(input("n1 : "))
            y = int(input("n2 : "))
            print( x * y)
           
               
if __name__ == "__main__" :                   
    calculator = Casio("Casio Calculator")
    calculator.SelectOption()