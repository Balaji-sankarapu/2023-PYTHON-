n=int(input("Enter the input value="))
def r(n):
   return(int(str(n) [::-1]))
def adam(n):
    if r(n)**2==r(n**2):
        return('adam number')
    else:
        return('not a adam number')
print(adam(n))
