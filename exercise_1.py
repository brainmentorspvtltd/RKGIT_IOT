data = {
    "names" : ["John","Sam","Max","Nick","Joe"],
    "dept" : ["IT","HR","HR","IT","IT"],
    "salary" : [56000,68000,45000,30000,80000]
    }

name = input("Enter employee name : ")
index = data["names"].index(name)
print("Name :",name)
print("Dept :",data["dept"][index])
print("Salary :",data["salary"][index])

# Print total salary of employees in IT department
totalSalary = 0
for i in range(len(data["dept"])):
    if data["dept"][i] == "IT":
        totalSalary += data["salary"][i]

print("Total Salary :",totalSalary)









