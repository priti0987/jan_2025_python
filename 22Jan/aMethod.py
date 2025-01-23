class Employee:
    number_of_emp = 0
    increment = 10

    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
        Employee.number_of_emp+=1

    def increase(self):
        self.sal = self.sal * Employee.increment

    @classmethod
    def change_increment(cls,amt):
        cls.increment=amt

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,sal=emp_string.split("-")
        return cls(fname,lname,sal)



lvish=Employee.from_str("lovish-jacksn-30000")
print(lvish.fname)
print(lvish.sal)
print(lvish.lname)