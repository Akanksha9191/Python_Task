# 5)Write a program which contains one class named as Numbers.
#  Arithmetic class contains one instance variables as Value.
#  Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.

class Numbers:
    
    Arithmetic = 20
    
    def __init__(self):
        self.value= []
        
    def AccessValues(self):
        size = int(input('Size of Values = '))
        print('Enter a value:  ')
        for i in range(size):
            value = input()
            self.value.append(value)
        print(self.value)
            
    def CheckPrime(self):
       pass
            
    
def main():
    num = Numbers()
    num.AccessValues()
    num.CheckPrime()
if __name__ == "__main__":
    main()
        
        
        
        