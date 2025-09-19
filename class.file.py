class marks:
    def __init__(self,m1,m2,m3,):
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def calculate(self):
        self.tot=self.mark1+self.mark2+self.mark3
        self.avg=self.tot/3
        print('total marks',self.tot)
        print('average',self.avg)
    def display(self):      
        print("m1:",self.mark1)
        print("m2:",self.mark2)
        print("m3:",self.mark3)
m1=int(input("enter m1:"))
m2=int(input("enter m2:"))
m3=int(input("enter m3:"))
if m1>40 and m2>40 and m3>40:
    print("pass")
else:
    print("fail")
od=marks(m1,m2,m3)
od.display()
od.calculate()

        
        
