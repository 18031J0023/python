n=int(input("enter a number \n"))
if n<=100:
	if n%2==0:
		if n>=2 and n<=5:
			print("NotWeird")
		if n>=6 and n <=20:
			print("Weird")
		if n>20:
			print("NotWeird")
	else:
		print("Weird")
else:
	print("out of range")