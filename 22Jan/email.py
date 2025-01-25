#dunder method
#__add__, built in method , but we can modify them as we wann


class Employee:
    number_of_emp = 0
    increment = 10

    def __init__(self, fname, lname, sal):
        self.fname = fname
        self.lname = lname
        self.sal = sal
        self.email = fname+lname+"@email.com"
        Employee.number_of_emp += 1

    def increase(self):
        self.sal = self.sal * Employee.increment

    @property
    def email(self):
        return self.fname+"."+self.lname+"@email.com"
    @email.setter
    def email(self,gemail):
        self.email = gemail


    @classmethod
    def change_increment(cls, amt):
        cls.increment = amt

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, sal = emp_string.split("-")
        return cls(fname, lname, sal)

    @staticmethod
    def isOpen(day):
        if day == "sunday":
            return False
        else:
            return True

    def __addsal__(self, other):
        return self.sal + other.sal

hrr=Employee("harry","pore",89)
pt=Employee("peter","pos",11)
print(hrr.email)
pt.lname="daas"
print(pt.email)