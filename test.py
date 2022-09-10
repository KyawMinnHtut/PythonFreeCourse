def hello():
    print("Hello called")
x = hello
#x()

def invoke(func):
    print("Invoke called")
    func
invoke(hello())