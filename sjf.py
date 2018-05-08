time1=[]
ArrivalTime=[]
BurstTime=[]
size=int(input("enter the total no. of programs"))
for i in range(size):
	time1.append(int(i+1))
	value=input("enter the arrival time of process: ")
	ArrivalTime.append(int(value))
	value=input("enter the burst time of process: ")
	BurstTime.append(int(value))
time=0
rangetime=0
small=0
for i in range(size):
	small=ArrivalTime[i]
	for j in range(i,size):
		if(BurstTime[j]>BurstTime[i]):
			if(ArrivalTime[j]<=ArrivalTime[i]):
				ArrivalTime[j]=ArrivalTime[i]+ArrivalTime[j]
				ArrivalTime[i]=ArrivalTime[j]-ArrivalTime[i]
				ArrivalTime[j]=ArrivalTime[j]-ArrivalTime[i]
				time1[j]=time1[j]+time1[i]
				time1[i]=time1[j]-time1[i]
				time1[j]=time1[j]-time1[i]
				BurstTime[j]=BurstTime[j]+BurstTime[i]
				BurstTime[i]=BurstTime[j]-BurstTime[i]
				BurstTime[j]=BurstTime[j]-BurstTime[i]
		
for i in range(size):
	while(time<ArrivalTime[i]):
		time=time+1
		print (".")
		
	print (time,"  P"+str(time1[i]))
	rangetime=time+BurstTime[i]
	while(time<rangetime):
		time=time+1
		print(time)