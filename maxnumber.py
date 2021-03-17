def maxnumber (numlist):
    currMax =-1
    for num in numlist:
        if (num>currMax):
            currMax=num
    return(currMax)
print(maxnumber([13,14,15,16,17]))