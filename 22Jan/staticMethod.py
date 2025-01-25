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

    @staticmethod
    def isOpen(day):
        if day == "sunday":
            return False
        else:
            return True

# priti = Employee('Priti','pore',67000)
print(Employee.isOpen("mond"))