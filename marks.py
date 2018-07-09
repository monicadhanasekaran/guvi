m1=int(raw_input())
m2=int(raw_input())
m3=int(raw_input())
reg=int(raw_input())
name=raw_input()
total=m1+m2+m3
average=total/3
print "the total=",total
print "the average=",average
if(average>=88) and (average<=100):
	print("s")
elif(total>=78) and (average<=87):
	print("a")
elif(average>=58) and (average<=67):
	print("b")
elif(average>=50) and (average<=57):
    print("c")
else:
	print("fail")