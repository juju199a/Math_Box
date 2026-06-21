def add(a,b) :
	return a+b

def subtract(a,b) :
	return a-b

def multiply(a,b) :
	return a*b

def divide_new(a, b):
	return a/b

def mod(a,b):
	if b == 0: return 0
	return a%b

def get_Median(a, b):
	return (a+b)/2

def get_Remainder(a,b) :
	return a//b

def get_Abs(num):
	if num>=0:
		return num
	else:
		return -num

def square(a):
	return a*a

def get_Percent(a,b):
	return (a/b) * 100

def get_Sum_ver1(n):
	return n(n+1)/2

def factorial(n):
	num = 1
	while n >= 1:
		num = num + n
		n = n - 1
	return num

def emergency():
	print("emergency")