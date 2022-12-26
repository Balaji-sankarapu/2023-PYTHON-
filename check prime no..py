num=int(input("Enter the number="))
if num>1:
    for i in range(3,int(num/2)+1):
        if (num%i)==0:
            print(num,"not a prime number")
            break
        else:
            print(num,"prime number")
else:
      print(num,"not a prime number")
