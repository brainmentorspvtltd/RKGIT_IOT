# class - blueprint of the object
# class name should start with a capital letter
# class name can only start with a letter or underscore
class Employee:
    emp_id = None
    emp_name = None
    emp_dept = None
    emp_salary = None
    company = "Brain Mentors"


ram = Employee()
ram.emp_id = 101
ram.emp_name = "Ram"
ram.emp_dept = "IT"
ram.emp_salary = 45000

print("Company :",ram.company)
print("Name is :",ram.emp_name)
print("ID is :",ram.emp_id)
print("Department is :",ram.emp_dept)
print("Salary is :",ram.emp_salary)


shyam = Employee()
shyam.emp_id = 102
shyam.emp_name = "Shyam"
shyam.emp_dept = "IT"
shyam.emp_salary = 50000

print("Company :",shyam.company)
print("Name is :",shyam.emp_name)
print("ID is :",shyam.emp_id)
print("Department is :",shyam.emp_dept)
print("Salary is :",shyam.emp_salary)