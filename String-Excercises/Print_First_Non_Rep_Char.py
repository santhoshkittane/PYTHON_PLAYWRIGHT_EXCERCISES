inp = input("Input any String Value:")
dictionary = dict()
char=''
for i in list(inp):
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
for key, value in dictionary.items():
    if value == 1:
        char = key
        if char.isupper():
            print(f'{char} is the First Capital Appeared ')
            break
        else:
            print("No Single Capital Letter present")

