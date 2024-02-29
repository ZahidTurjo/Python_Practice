import math
def cane_needed(height,width,covarage):
    no_of_cane=math.ceil((height*width)/covarage)
    print("No. of cane needed :",no_of_cane)

height=int(input("enter the height of the wall: "))
width=int(input("enter the width of the wall: "))
covarage=7

cane_needed(height,width,covarage)


