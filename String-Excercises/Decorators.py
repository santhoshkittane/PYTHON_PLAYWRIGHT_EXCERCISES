def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def my_decorator2(func):
    def wrapper():
        print("Something is happening before the function is called.<<INSIDE DECORATOR 2>>>")
        func()
        print("Something is happening after the function is called.<<INSIDE DECORATOR 2>>>")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

@my_decorator2
def say_hello2():
        print("Hello2!")

say_hello()
say_hello2()