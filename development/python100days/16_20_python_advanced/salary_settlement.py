# 工资结算系统
"""
月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
"""

from abc import ABCMeta, abstractmethod
class Employee(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """
        抽象方法，后续子类需要实现
        """
        pass

class Manager(Employee):

    def get_salary(self):
        return 15000.0

class Programmer(Employee):

    def __init__(self, name,hours = 0):
        super().__init__(name)
        self.hours = hours

    def get_salary(self):
        return 200 * self.hours

class Salesman(Employee):

    def __init__(self,name,sales = 0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05

class EmployeeFactory:
    """
    创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）
    """
    @staticmethod
    def create(emp_type,*args,**kwargs):
        employee_types = {'M':Manager,'P':Programmer,'S':Salesman}
        emp_cls = employee_types[emp_type.upper()]
        return emp_cls(*args,**kwargs) if emp_cls else None

def main():

    emps = [
        EmployeeFactory.create('M','Tommy'),
        EmployeeFactory.create('P','John',100),
        EmployeeFactory.create('S','Arthur',2000)
    ]
    for emp in emps:
        print(f'{emp.name} : {emp.get_salary():.1f}')

if __name__ == '__main__':
    main()