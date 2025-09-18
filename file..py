try:
    n=int(input("enter a number:"))
    y=20/n
except ZeroDivisionError:
    print('it a diving y')
else:
    print(y)
finally:
    print('bye')
    
