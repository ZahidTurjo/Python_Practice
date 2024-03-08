
class Bike:
    def __init__(self) -> None:
        self.no_of_tyres=2

    def start(self):
        print("start with kick")
class Scooty:
    def __init__(self) -> None:
        self.no_of_tyres=2

    def start(self):
        print("self start")
class Bike:
    def __init__(self) -> None:
        self.no_of_tyres=4

    def start(self):
        print("start with key")
s=Scooty()
b=Bike()
s.start()
b.start()