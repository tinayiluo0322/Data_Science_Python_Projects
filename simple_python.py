print("hello world!")
y=7
x=12
print(x)
z=x*y
print(z)
z**2

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        fact=1
        for i in range(n):
            fact*=i+1
        return fact

num=4
print(f"{num}!={factorial(num)}")

q=[[1,2,3],[4,5,6],[7,8,9]]
print(q)