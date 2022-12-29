def calculate_hcf(x,y):
    if x>y:
       smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
    return hcf
n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
print("hcf is",calculate_hcf(n1,n2))
