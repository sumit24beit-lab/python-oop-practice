class Employee:
    def __init__(self, employee_id, employee_name, basic_salary):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.basic_salary=basic_salary
    def calculate_hra(self):
        return self.basic_salary * 20/100
    def calculate_da(self):
        return self.basic_salary * 10/100
    def calculate_pf(self):
        return self.basic_salary * 12/100
    def calculate_net_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da() - self.calculate_pf()
    def display_pay_slip(self):
        print("Employee ID:", self.employee_id)
        print(f"Employee Name: {self.employee_name}\n")
        print(f"Basic Salary: ₹{self.basic_salary}")
        print(f"HRA: ₹{self.calculate_hra()}")
        print(f"DA: ₹{self.calculate_da()}")
        print(f"PF Deduction: ₹{self.calculate_pf()}\n")
        print(f"Net Salary: ₹{self.calculate_net_salary()}")
employee1=Employee("E101", "Amit Sharma", 30000)
employee2=Employee("E102", "Priya Patil", 45000)
employee3=Employee("E103", "Rahul Verma", 60000)
print("========== EMPLOYEE PAYROLL SYSTEM ==========\n")
employee1.display_pay_slip()
print("\n---------------------------------------------\n")
employee2.display_pay_slip()
print("\n---------------------------------------------\n")
employee3.display_pay_slip()


