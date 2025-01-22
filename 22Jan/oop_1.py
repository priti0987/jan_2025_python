#oop : object oreintation programming
#inheretance
#encapsulation : hiding data
#polymorfism
#abstraction
print("oop")
class Employee:
    def __init__(self,fname,lname,sal):
        self.fname= fname
        self.lname=lname
        self.sal=sal

harry=Employee("harry_name","das",10000)

print(harry.sal)
print(harry.fname)
print(harry.lname)