user_input = input('Enter your name: ')
print(f'User entered {user_input}')
s = ''.join(e for e in user_input)
if(s == s[::-1]):
    print(f'{user_input}'+' is a palindrome')
else:
    print(f'{user_input} is not a palindrome')