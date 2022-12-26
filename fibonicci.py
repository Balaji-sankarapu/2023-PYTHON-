import math
def perfectsquare(x):
    s=int(math.sqrt(x));
    return s*s==x;
def fibonacci(n):
    return perfectsquare(5*n*n+4) or perfectsquare(5*n*n-4);
for i in range (1,11):
    if (fibonacci(i)==True):
        print(i,"fibonacci number");
    else:
        print(i,"not a fibonacci number");
