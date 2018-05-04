
ArrivalTime=[]
BurstTime=[]
size=int(input("enter the total no. of programs"))
for i in range(size):
	value=input("enter the arrival time of process: ")
	ArrivalTime.append(int(value))
	value=input("enter the burst time of process: ")
	BurstTime.append(int(value))
time=0
rangetime=0
for i in range(size):
	while(time<ArrivalTime[i]):
		time=time+1
		print (".")
		
	print (time,"  P"+str(i+1))
	rangetime=time+BurstTime[i]
	while(time<rangetime):
		time=time+1
		print(time)