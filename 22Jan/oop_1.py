#oop : object oreintation programming
#inheretance
#encapsulation : hiding data
#polymorfism
#abstraction
class Employee:
    increment = 1.5
    def __init__(self,fname,lname,sal):
        self.fname= fname
        self.lname=lname
        self.sal=sal

    def increase(self):
        self.sal = self.sal* Employee.increment

harry=Employee("harry_name","das",10000)

print(harry.sal)
print(harry.fname)
print(harry.lname)
print(harry.increment)
harry.increase()
print(harry.sal)