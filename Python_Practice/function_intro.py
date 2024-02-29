def greet():
    print("hi")
    print("turjo")
    pass
def greet1(subject):
    print("teach",subject)
# greet1("physics")
# greet1("chemistry")    

def sum(x,y):
    add=x+y
    pass
def greet3(name,dept,sub="math",):
    print("hi",name)
    print('subject',sub)
    print('dept',dept)
# greet3("turjo",dept="amth",sub="cs")    

def add(*numbers):
    c=0
    for i in numbers:
        c=c+i
    print(f"sum if{c}")

def info_person(** kwargs):
    for key,value in kwargs.items():
        print(key,value)

info_person(name="tujo",age=31,dept="cse")
info_person(name="zahid",age=21,)