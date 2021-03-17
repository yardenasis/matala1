hours=input("enter hours")
rate=input("enter rate")
hours=float(hours)
rate=float(rate)
def computePay (hours,rate):
	if(hours>40):
		pay=(hours-40)*rate*1.5+40*rate
	else:
		pay=hours*rate
	return pay
print(computePay(hours,rate))