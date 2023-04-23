
class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary= emp_salary
        self.emp_department=emp_department
    def assign_department(self,new_department):
        self.emp_department=new_department
    def print_employee_details(self):
        print(f"Employee ID:{self.emp_id}\nEmployee Name:{self.emp_name}\nSalary:{self.emp_salary}\nDepartment:{self.emp_department}")
        print ("---------------------------------------------------------------------")
    def calculate_salary(self,salary,hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            Overtime_amt = (overtime*(salary/50))
            self.emp_salary = self.emp_salary+Overtime_amt
            
employee1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee("MARTIN", "E7900", 50000, "SALES")
employee4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

print("Original Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
# Change the departments of employee1 and employee4
employee1.assign_department("OPERATIONS")
employee4.assign_department("SALES")
# Now calculate the overtime of the employees who are eligible:
employee2.calculate_salary(45000, 52)
employee4.calculate_salary(45000, 60)
print("Updated Employee Details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()
