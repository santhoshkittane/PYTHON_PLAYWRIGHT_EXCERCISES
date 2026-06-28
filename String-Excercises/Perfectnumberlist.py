def perfect_number(n):
    j = int(n/2)+1
    tot=0
    for i in range(2,j):
        if n%i==0:
            tot+=i
    if (tot+1) == n:
        return True

n=input("Enter a +ve Number of your choice:")
tot=[1]
for i in range(2,int(n)):
    if perfect_number(i):
        tot.append(i)
print(tot)
