n=int(input("enter a number: "))
def factorial(n):
     if(n<2):
         return 1
     else:
         return n * (factorial(n-1))

answer= factorial(n)
print("The factorial of",n,"is:",answer)