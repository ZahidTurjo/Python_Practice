student_name= {
    "jenny":92,
    "harry":78,
    "dimpy":56,
    "rahul":41,
    "aniket":99,
    "prem":34,
    "turjo":70

}

for i in student_name:
    marks=(student_name[i])
    if marks>90 and marks<=100:
        print(f"{i} is got A+")
    elif marks>80 and marks<=90:
        print(f'{i} is got A')    
    elif marks>70 and marks<=80:
        print(f'{i} is got B+')    
    elif marks>60 and marks<=70:
        print(f'{i} is got B')    
    elif marks>50 and marks<=60:
        print(f'{i} is got c')    
    elif marks>40 and marks<=50:
        print(f'{i} is got D') 
    else:   
        print(f'{i} is got F')
    