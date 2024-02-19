
matrix=[[1,1,1],
        [1,1,1],
        [1,1,1]
        ]

position=input("enter the position where u hide money =")
row_number=int(position[0])
colum_number=int(position[1])
matrix[row_number-1][colum_number-1]="X"

print(matrix)
