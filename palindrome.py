def palindrome(s):
   return s==s[::-1]
s=str(input("enter the input value="))
ans=palindrome(s)
if ans:
    print("palindrome")
else:
    print("not a palindrme")
