#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	ap = input()
	s=ap.lower()
	vowel=0
	for i in range(len(s)):
		if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
			vowel=vowel+1
	print(vowel)
	

if __name__== "__main__":
	main()
