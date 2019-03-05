def func1():
	print("hii")
	print("hello")
func1()

def func2(a):
	print("hi"+a)
func2("namitha")	

def func3(a,b,c):
	d=a+b+c
	print(a,b,c,d)
func3(2,5,6)

def func4(university="IITB"):
	print("I am in" + "\t"+ university)
func4("IITG")
func4("IITD")
func4()	

def func5(a,b):
	print("hii other function")
	c=a+b
	return c

def func6():
	print("hello,i am going to call other function")
	s=func5(2,7)
	print("addition is",s)
func6()	





'''
user@user:~$ python3 functions.py
hii
hello
hinamitha
2 5 6 13
I am in	IITG
I am in	IITD
I am in	IITB
hello,i am going to call other function
hii other function
addition is 9
'''