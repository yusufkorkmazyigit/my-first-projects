y=0
x=1
a=int(input("Fibonacci diziniz kaça kadar olsun: "))
while x+y<a:
    x=x+y
    y=x+y
    print(x)
    print(y)