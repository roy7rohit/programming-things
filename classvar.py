class Employee:

    # age = []
    pay_raise = 2

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mail.com'

    def fullname(self):
       # print('%s %s %d %s' %(self.first, self.last, self.pay, self.email))
        return f'{self.first} {self.last} {self.pay} {self.email}'

    # def emp_age(self, age):
    #     emp_age.age.append()
    def raise_amount(self):
        self.pay = int(self.pay * self.pay_raise)

e1 = Employee('rath', 'wayne', 90000)
e2 = Employee('max', 'lucas', 80000)
# print(e1.pay_raise)
print(e1.fullname())
print(Employee.pay_raise)
print(e2.fullname())

# print(Employee.emp_age('roy', 23))
