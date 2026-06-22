str1 = "Emma is a Emma data scientist who knows Emma Python. Emma works at a Emma google."
print(str1+"====is the INPUT STRING")
str = input("Enter a String:")
last_pos = str1.rfind(str)
print(f"Last Position of {str}:{last_pos}")
first_pos = str1.find(str)
pos=input("Which position required:")
last_pos = str1.find(str,int(pos)+1)
print(f"{pos} Position of {str}:{last_pos}")

