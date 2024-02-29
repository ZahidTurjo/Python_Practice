data=[
    {
        "name":"turjo",
        "roll":20,
        "age":22,
        "course":"python"
    },
    
    {
        "name":"zahid",
        "roll":11,
        "age":21,
        "course":"java"
    }
    
]
print("data before\n",data)

# new_data={"name":"sam",
#           "roll":22,
#           "age":18,
#           "course":"c++"
#           }
# data.append(new_data)
# print(data)
def add_new_student(name,roll,age,course):
    new_data={
        "name":name,
        "roll":roll,
        "age":age,
        "course":course
    }
    data.append(new_data)
    print(data)



add_new_student("sam",22,18,"c++")
