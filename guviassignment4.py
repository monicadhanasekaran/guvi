def ode(r) :
	if((r%2)==0):
		print("eve") 
		return True
	else:
		print("odd")
		return False
 
 
r=int(raw_input())
ode(r)