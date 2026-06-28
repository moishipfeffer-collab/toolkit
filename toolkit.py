#part 1 sec 1
def greet(name):
    print("hello",name)
greet("agent x")
#sec 2
def add(a, b):
    print(a+b)
add(3,4)   
#sec 3
def sqware(n):
    print(n**2)
sqware(5)     
#sec 4
def greet_with_title(name,title="agent"):
    print(title,name)
greet_with_title("moishi")
greet_with_title("moishi","rachel")
# sec 5
def describe(name, level, active):
    print("name:",name ,"level:",level,"active:",active)
describe(name="moishi",active=True,level=5)
# sec 6
def multiply(a, b=2):
    print(a*b)
multiply(9,9) 
#sec 7
def print_largest(a, b, c):
    if c >= a and c >= b:
        print(c)
    elif a >= c and a >= b:
        print(a)
    elif b >= c and b >= a:
        print(b)
print_largest(4,4,1)
# sec 8
def show_fahrenheit(c):
   print((c*9/5)+32) 
show_fahrenheit(0)
show_fahrenheit(100)
show_fahrenheit(37.5)



