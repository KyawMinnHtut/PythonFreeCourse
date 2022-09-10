#Call Stack and Stack Frame
def first():
    a = "First"
    print("First function is callled.")
    return second()
def second():
    b = "Second"
    print("Second function is callled.")
    return third()
def third():
    c = "Third"
    print("Third function is called.")
    return 10
x = first()
print(x)

# factoraial_function(5)
#     5! = 5 * 4 * 3 * 2 * 1
#     4! = 4 * 3 * 2 * 1
#     3! = 3 * 2 * 1
#     2! = 2 * 1
#     1! = 1
#     n! = n * (n-1)!

#Recursive Function    =====>requires call stack
def fact(n):
    if n == 1:  #base case
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
#Imperative Loop        =====> can't cause call stack error
def imperative_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * 1
    return fact
print(fact(5))


#First Class Function
#Rule 1 -> function can be stored in variable
#Rule 2 -> function can be passed as parameter
#Rule 3 -> function can be returned from function
def hello():
    print("Hello called")
x = hello
x()

def invoke(func):
    print("Invoke called")
    func
invoke(hello())

def get_another_fun():
    print("Invoked get another")
    return hello
get_another_fun()()

#Lanbda Function
def square(x):
    return x * x
print(square(5))
lambda_square = lambda x: x*x #one line statement
print(lambda_square(5))