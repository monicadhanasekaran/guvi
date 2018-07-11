n=int(raw_input())
if(n<1):
	for i in range(2,n):
		if(n%i)==0:
			print("it is  a not prime num")
		else:
			print("it is a prime num")
else:
	print("it is  not a prime num")