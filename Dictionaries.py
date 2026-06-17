a = {"Name":"Santhosh",
     "Age":40,
     "Address":"Bangalore",
     "Companies":["ALTISOURCE","CGI","ACCIONLABS"],
     "JOB":{"Role":"SSE",
      "SALARY":"21K"}}
#print(a)
test = a.keys().__contains__("JOB")
test2 = a.keys().__sub__("JOB")
#print(a)
test3 = a.keys().__contains__("INFY")
print(f'Keys are {a.keys()}')
test4 = a["Companies"]
print(f'Values are {test4}')
print(f'TEST VALUE TEST {test}')
print(f'TEST VALUE TEST3 {test3}')
print(f'Value of AGE is {a["Age"]}')
print(test2)
print(test3)
