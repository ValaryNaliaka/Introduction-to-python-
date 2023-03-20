#payroll system
class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        print("display id",self.id,"display name",self.name)
class SalaryEmployee(Employee):
    def __init__(self, id, name,salary):
        Employee.__init__(self, id, name)
        self.salary=salary
    def calculate_payroll(self):
        print("print salary employee",SalaryEmployee)
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name,salary,commission):
        SalaryEmployee.__init__(self, id, name,salary)
        self.commission=commission
        CommissionEmployee=self.commission+self.salary
    def calculate_payroll(self):
        print("print commission employee",CommissionEmployee)
class HourlyEmployee(Employee):
    def __init__(self, id, name,salary,hours):
        Employee.__init__(self, id, name)
        self.hours=hours
        self.salary=salary
        HourlyEmployee=self.hours*self.salary
    def calculate_payroll(self):
        print("hourly employee",HourlyEmployee)
hourly=HourlyEmployee(4532, 'ANN',3000,4)
hourly.calculate_payroll()
comm=CommissionEmployee(4532,'ANN' , 3000, 500)
comm.calculate_payroll()
salary=SalaryEmployee(4532, 'ANN', 3000)
salary.calculate_payroll()
