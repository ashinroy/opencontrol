import os
def check(i):
	memsize=os.popen("smartctl -a /dev/sda")
	a=memsize.readlines()
	x=''
	x= x+a[50+i][37]
	x= x+a[50+i][38]
	x= x+a[50+i][39]
	y=''	
	y=y+a[50+i][43]
	y=y+a[50+i][44]
	y=y+a[50+i][45]
	z=''
	z=z+a[50+i][49]
	z=z+a[50+i][50]
	z=z+a[50+i][51]
	
	return x,y,z
smartdata = {'ReadErrorRate' : check(0) ,'SpinUpTime' : check(1),'StartStopCount' : check(2)}
print smartdata['ReadErrorRate'] ,smartdata['SpinUpTime'],smartdata['StartStopCount']




