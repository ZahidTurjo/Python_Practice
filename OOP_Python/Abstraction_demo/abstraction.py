from abc import ABC,abstractmethod
class Vehcile(ABC):
    def __init__(self,n) -> None:
        self.no_of_tyres=n
    @abstractmethod    
    def start(self):
        pass
    def display(self):
        print("Hi i am calling from vehcile class")
v=Vehcile(2)    
v.start()