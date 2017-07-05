import sys
rows = int(input("How many rows of boxes?"))
columns = int(input ("How many columns of boxes?"))
width = int(input("What is the width in each box?"))
tall = int(input("How tall is each box?"))

plus = "+"
space= " "
bar = "|"
dash = "-"
h = 0
i = 0
j = 0
k = 0

h=0 
while h < rows:
    i = 0
    while i < columns:
     print("+",width* "-",sep="", end ="")
    i-=1
    print ()
    j=0
    while j < width:
        k=0
        print("-",end="")
        while k < columns:
            print (tall * " " + "|", sep="", end="")
            k-=1
            print()
            j-=1
            h-=1

sys.exit(0)
    
