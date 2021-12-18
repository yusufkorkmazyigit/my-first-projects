#def square(num): return num ** 2

square=lambda num: num**2
numbers = [1,3,5,9,10,4]

# result=square(8)
# result= list(map(square,numbers))
# for item in map(square,numbers):
#     print(item)
# square=lambda num: num**2

def check_even(num): return num%2==0
check_even=lambda num: num%2==0
#result=list(filter(lambda num: num%2==0 ,numbers))

result=list(filter(check_even,numbers))

print(result)