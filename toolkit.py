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
    print("hello",title,name)
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
# sec 9
def check_even(n):
    if n % 2 == 0:
        print(n, "is evan")
    else:
        print(n,"is odd")
check_even(4)
check_even(7)
# sec 10
def summarize(items):
    sum=0
    for num in items:        
        sum+=num
    print("sum:", sum)
    maxnum=items[0]
    for i in items:
        if i>maxnum:
            maxnum=i
    print(maxnum)
    min_num=items[0]
    for i in items:
        if i<min_num:
            min_num=i
    print(min_num)
summarize([400,900,499,109,500])
#part 2 sec 1
def show_all(*args):
    for arg in args:
        print(arg)
show_all("radio","maps","flashlight") 
#sec 2
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key,":",value)
show_profile(name="Agent X", level=7, active=True)
#sec 3
def power(base, exponent=2):
    print(base**exponent)
power(3) 
power(3,3)   
power(exponent=4,base=2) 
# sec 4
def repeat(text, times):
    print(text*times)
repeat("moishi",8) 
#sec 5
def flatten_and_print(nested):
    for y in nested:
        for x in y:
            print(x)  
flatten_and_print([[1,2],[4,5],[6,7]])

