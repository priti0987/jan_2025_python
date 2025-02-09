#oop : object oreintation programming
#inheretance
#encapsulation : hiding data
#polymorfism
#abstraction
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

harry = Employee("harry_name", "das", 10000)

print(harry.sal)
print(harry.fname)
print(harry.lname)
print(harry.increment)
harry.increase()
print(harry.sal)
print("__dict",harry.__dict__)
print(Employee.__dict__)
print(Employee.number_of_emp)

Employee.change_increment(2)
harry.increase()
print(harry.sal)