num=int(input("Enter the input value="))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print(num,"armstrong number")
else:
    print(num,"not a armstrong number")
