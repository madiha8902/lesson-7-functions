# def intro():
#     print("hello")
# intro()
def intro(name):
    print("hello I am ",name)

n=input("enter your name here")
intro(n)

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def divi(a,b):
    return a / b
def mult(a,b):
    return a * b
def power(a):
    return a**2
no1=int(input("enter no1"))
no2=int(input("enter no2"))

print("sum",add(no1,no2))
print("differnce",sub(no1,no2))
print("quotient",divi(no1,no2))
print("product",mult(no1,no2))
print("power",power(2))