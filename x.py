import math
def rx(a=1,b=1,c=0):
	delta=math.sqrt((b**2)-4*(a*c))
	x1=(-b-delta)/(2*a)
	x2=(-b+delta)/(2*a)
	return x1,x2 
print(rx(2,8,6))

