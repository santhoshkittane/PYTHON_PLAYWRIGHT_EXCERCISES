a = [1,2,3,4,'a','b','c',1.5,1.8,"hello world",1.5]

var = 1.5


#print(a.pop())
print(f'The popped out value is {a.pop(a.index(var))}')
print(a)
a.append("hello world")
a+=["how are you","Good Bye"]
print(a)
a.insert(7,1.5)
print(a)
if a.__contains__(1.8):
    print('1.8 is present in the list')
if a.__contains__(4):
    print('4 is present in the list')
else:
    print('1.9 is not present in the list')
print(a.count(1.8))
var = 'Enter the value to check for:'
# if a.__contains__(var):
#     print('Value is present in the list')
# else:
#     print('Value is not present in the list')
# print(f'Overall number of items in list is {len(a)}')
if '.' in var:
    var = float(var)
else:
    var = int(var)

if a.__contains__(var):
    print('Value is present in the list')
else:
    print('Value is not present in the list')
print(f'Overall number of items in list is {len(a)}')

