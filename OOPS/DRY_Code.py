# class - blueprint of the object
# class name should start with a capital letter
# class name can only start with a letter or underscore
class Employee:
    # __init__ = constructor
    # constructor - used to initialize variables
    # we don't have to call this method
    # it is called automatically when we create object
    def __init__(self, emp_id, emp_name, emp_dept, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_dept = emp_dept
        self.emp_salary = emp_salary
        self.company = "Brain Mentors"

    def showDetails(self):
        print("Company :", self.company)
        print("Name is :", self.emp_name)
        print("ID is :", self.emp_id)
        print("Department is :", self.emp_dept)
        print("Salary is :", self.emp_salary)


ram = Employee(101,"Ram","IT",45000)
ram.showDetails()

shyam = Employee(102,"Shyam","IT",50000)
shyam.showDetails()