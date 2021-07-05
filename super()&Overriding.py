class A:
    classvar1 = "I am a class var in Class A"

    def __init__(self):
        self.instance = "I am an instance var in constructor of Class A"
        self.classvar1 = "I am classvar of Class A"
    
class B(A):
    classvar1 = "I am a Class var in Class B"

    def __init__(self):
        self.instance = "I am an instance var in constructor of Class B"
        super().__init__() #If I put this in before assigning self.instance  of Class B and print the value of instance by print(b.instance), the result will be "I         am an instance var of Class B"
        
        self.classvar1 = "I am classvar of Class B" #If I put this before the super().__init__ the result will be "I am classvar of Class A"

a = A()
b = B()

print(b.instance)
print(b.classvar1)
