# Student management

class Student:
    def __init__(self):
        self.Name = ''
        self.Age = 0
        self.Percentage =0.0
    
    def AddDetails(self):
        print('Enter Student Name: ')
        self.Name = input()
        
        print('Enter Student Age: ')
        self.Age = int(input())
        
        print('Enter Student percentage: ')
        self.Percentage= float(input())
        
    def DisplayDetails(self):
        print('____________Student Details____________')
        print(f'Student Name: {self.Name}')
        print(f'Student Age: {self.Age}')
        print(f'Student Percentage: {self.Percentage}')

student1= Student()
student1.AddDetails()
student1.DisplayDetails()