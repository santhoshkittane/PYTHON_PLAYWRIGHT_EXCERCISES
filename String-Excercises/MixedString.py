def my_decorator(function):
    def wrapper(test111, test222):
        # str1=input("Enter the first string: ")
        # str2 = input("Input another String Value:")
        str3 = function(test111, test222)
        print("Final String is ", str3)
    return wrapper

@my_decorator
def stringmix(str1,str2):
    final=""
    s1_length=len(str1)
    s2_length=len(str2)
    str2=str2[::-1]
    length = s1_length if s1_length>s2_length else s2_length
    for i in range(length):
        if i<s1_length:
            final+=str1[i]
        if i<s2_length:
            final+=str2[i]
    return final

str1 = input("Input any String Value:")
str2 = input("Input another String Value:")
# print("Final String is ",stringmix(str1,str2))

stringmix(str1,str2)