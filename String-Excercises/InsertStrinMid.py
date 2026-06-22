STR1 = input("First string: ")
STR2 = input("Second string: ")
len1 = len(STR1)
# len2 = len(STR2)
mid=int(len1/2)
FINAL=STR1[:mid]+STR2+STR1[mid:]
print("Final output is:"+FINAL)


#STR1 = Santhosh
#STR2 = Soumya
#output = SantSoumyahosh