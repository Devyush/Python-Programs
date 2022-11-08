def patRow(n):
    if (n==0):
        return
    print("$", end='')
    patRow(n-1)
def patCol(x,y=1):
    if (x<y):
        return
    patRow(y)
    print("\n",end='')
    patCol(x,y+1)
i=int(input("Enter the number of rows: "))
patCol(i)
