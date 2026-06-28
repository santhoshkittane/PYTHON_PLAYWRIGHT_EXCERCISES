str1 = input("Input a string:")
reverse = lambda s: s[::-1]
print(reverse(str1))

students = [("Alice", 25,"White"), ("Bob", 20,"Red"), ("Charlie", 23,"Black")]
# sorted_students2 = sorted(students, key=lambda student: student[1],reverse=True) #Reverse sorting by taking given key
sorted_students2 = sorted(students, key=lambda students: students[1],reverse=True)
sorted_students = sorted(students) # This will Sort by taking first element
print("After Sorting in Reverse Order:",sorted_students)
print("After Sorting in Reverse Order based on particular KEY:",sorted_students2)
