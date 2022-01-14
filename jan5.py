def add1(n):
	return n+1

def jan5():
	print("12345")

# output:
# h
# e
# l
# l
# 0
def jan5B():
	for a in range(1, 8):
		print(a)

# ask for a number,
# and then print out all the number (each on a new 
# line) from one to the number we typed in
def jan6A():
	number = int( input("type in a number: "))
	for a in range(1, number+1):
		print(a)

jan6A()