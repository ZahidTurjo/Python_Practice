def hcf(x,y):
   
    if x>y:
        small=y
    else:
        small=x    
    for i in range(1,small+1):
        if (x%i ==0) and (y%i == 0):
            highest=i
    return highest                    



   
print(hcf(60,30))