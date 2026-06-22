STR1 = input("First string: ")
STR2 = input("Second string: ")
LEN1 = len(STR1)
LEN2 = len(STR2)
Final = STR1[0]+STR2[0]+STR1[int(LEN1/2)]+STR2[int(LEN2/2)]+STR1[LEN1-1]+STR2[LEN2-1]
print("Final output is:"+Final)

# STR1 = ABCDE
# STR2 = ASDFG
# OUTput = AACDEG
