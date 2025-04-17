employees = {
    1:{"name":"Anu" , "age":24 , "department":"Accounts"},
    2:{"name":"Bhuvanesh" , "age":25 , "department":"Security"},
    3:{"name":"Anish" , "age":24 , "department":"Accounts"},
    4:{"name":"Anusha" , "age":23 , "department":"Management"},
    5:{"name":"Bhavya" , "age":26 , "department":"Electronics"}
}
print("Employees in the company:")
for employee in employees.values():
    print(employee["name"])
sum=0
for employee in employees.values():
    sum+=employee["age"]
print("average age:",sum//len(employees))
#print(avg)
employees[6]={"name":"Santosh","age":29,"department":"Accounts"}
print(employees)
Remove_employee =employees.pop(4)
print(employees)