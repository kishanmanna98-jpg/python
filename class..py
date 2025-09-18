class stud:
    def __init__(self,x,y,z):
        self.sno=x
        self.sname=y
        self.sage=z
    def disp(self):
        print("student no:",self.sno)
        print("stunden name:",self.sname)
        print("student age:",self.sage)
x=int(input("enter roll.no"))
y=input("enter name")
z=int(input("enter age"))
ob=stud(x,y,z)
ob.disp()
