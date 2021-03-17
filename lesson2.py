hours = input("enter hours")
try:
	hours=float(hours)
except:
	hours=-1

rate = input("enter rate per hour")
try:
	rate=float(rate)
except:
	rate=-1


if float(hours)>40:
	more40=hours-40.0
	pay=rate*40.0+rate*1.5*more40
	print("pay is : " ,pay)
else:
	pay=rate*hours
	print("pay is : " ,pay)