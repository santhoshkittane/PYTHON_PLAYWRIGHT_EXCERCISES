def my_decorator(func):
    def wrapper():
        inp = input("Enter a number till Fibonacci Expected: ")
        result=func(int(inp))
        print(result)
    return wrapper

@my_decorator
def fibonacci(n):
    fin = [0, 1]
    for i in range (2,int(n)):
        fin.append(fin[i-1]+fin[i-2])
        if int(n)<
    return fin

fibonacci()

