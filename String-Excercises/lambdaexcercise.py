inp = ["Test", "Test1", "Test2", "Test3", "Test4","Test5 Test6"]
swap = lambda x: [i.split()[::-1] for i in x]

print("After Changing : ",swap(inp))

multiply = lambda x: x *10
print("After Multiplying by 100 : ",multiply("a"))