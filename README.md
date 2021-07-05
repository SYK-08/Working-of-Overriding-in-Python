# Working-of-Overriding-in-Python
#This is a document that explains the concepts of Overriding in Python OOP

In overriding class vars and instance vars in OOP of Python, there are a few things to make crystal clear.
These include the hierachy of searching methods, class vars, instance vars and functions.

~Python code2-->
class A:
	classvar1 = "This is a Class variable in Class A"
	
	def __init__(self):
		self.instance = "This is an instance variable of Class A made by a constructor"
		self.classvar1 = "This is classvar1 of Class A made by a constructor"
	
class B(A):
	classvar1 = "This is a Clas Variable in Class B"
	
	def __init__(self):
		self.instance = "This is an instance variable of Class B made by a constructor"
		self.classvar1 = "This is classvar1 of Class B made by a constructor"
		
a = A()
b = B()

print(b.classvar1)

#In the above Python3 script the __init__ in Class B is overriding the __init__ of Class A. That means that the constructor of Class A is of no use now and is therefore same as if we remove it from there.

But in some cases we may need the contents present in the __init__ of Class A, and we have a way to do that.

~Python code2--->
class A:
	classvar1 = "This is a Class variable in Class A"
	
	def __init__(self):
		self.instance = "This is an instance variable of Class A made by a constructor"
		self.classvar1 = "This is classvar1 of Class A made by a constructor"
	
class B(A):
	classvar1 = "This is a Clas Variable in Class B"
	
	def __init__(self):
		super().__init__()
		self.instance = "This is an instance variable of Class B made by a constructor."
		self.classvar1 = "This is classvar1 of Class B made by a constructor"

a = A()
b = B()

print(b.classvar1)

#Here the result will be "This is classvar1 of Class B made by a constructor".(Important): If we type the super().__init__() after assigning the values of the then the output will be "This is classvar1 of Class A mde by a constructor". It is because Python is an interpreted language and as the name says, it executes the program line by line so the values het updated if we put the super().__init__() in different places.

# And now the most interesting part, i.e., why do the results change?

In Python code 1, we noticed that there were two classvar1 named variables but their roles were different, the first one was a CLASS VARIABLE and the second one was an INSTANCE VARIABLE.

The Python interpreter follows the hierachy given below:
Instance Variables of the mentioned Class --> Instance Variables of the Super Class --> Class Variables of the mentioned Class --> Class variables of the Super Classs
