class A:
    def say_hello(self):
        print("Hello from A")

class B(A):
    def say_hello(self):
        print("Hello from B")

class C(A):
    def show(self):
        print("Hi from C class")
    def say_hello(self):
        print("Hello from C")
class D(B,C):
    def say_hello(self):
        super().say_hello()
        print("hello from D")
        A.say_hello(self)
d_1=D()
d_1.say_hello()    
print(D.mro())  
