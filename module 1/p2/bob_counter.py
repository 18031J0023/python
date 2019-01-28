'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
	s = input()
	ap=s.lower()
	count=0
	for i in range(len(ap)-2):
		if ap[i]=='b' and ap[i+1]=='o' and ap[i+2]=='b':
			count=count+1
	print(count)

if __name__== "__main__":
	main()
