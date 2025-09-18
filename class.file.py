class marks:
    def __init__(self,m1,m2,m3,):
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def calculate(self):
        tot=m1+m2+m3
        avg=tot/3
        print('total marks',tot)
        print('average',avg)
m1=int(input("enter m1:"))
m2=int(input("enter m2:"))
m3=int(input("enter m3:"))      
od=marks(m1,m2,m3)
od.calculate()

        
        
