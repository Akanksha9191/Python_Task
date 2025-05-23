# 1)Write a program which contains one class named as Demo.
# That class contains one class variable as value
# There are two instance methods of class as Fun and Gun which displays values of instance variables
# Initialise instance variable in constructor by accepting the values from user
# After creating the class create the two objects of Demo class as
# Obj1 =Demo(11,21)
# Obj2 = Demo(51,101)

# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()


class Demo:
    demo_val = 0
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
    
    def Fun(self):
        print(f'Fun: \n value1 = {self.val1} \n value2 = {self.val2}')
        
    def Gun(self):
        print(f'Gun: \n value1 = {self.val1} \n value2 = {self.val2}')

Obj1 =Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()
print('')
Obj1.Gun()
Obj2.Gun()
