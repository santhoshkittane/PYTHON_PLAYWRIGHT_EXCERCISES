def perfect_number(n):
    j = int(n/2)+1
    tot=0
    for i in range(2,j):
        if n%i==0:
            tot+=i
    if (tot+1) == n:
        return True
    else:
        return False


inp = input("Enter your Number:")
if perfect_number(abs(int(inp))):
    print(f'{inp} is a Perfect Number')
else:
    print(f'{inp} is NOT a Perfect Number')

