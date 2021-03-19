import threading 
import os 

def print_cube(n):
	for i in range(n): #start =0 stop=n-1  step=1
		print("cube : ",i*i*i," Name of Thread : ",threading.current_thread().name,
" Name of Process : ",os.getpid()) #getpid() inbuilt function 


def print_square(n):
	for i in range(n):
		print("square : ",i*i," Name of Thread :",threading.current_thread().name," Name of Process :",os.getpid())




t1=threading.Thread(target=print_square,args=(5,),name="t_square")
#t1 user defined object of Thread class
t2=threading.Thread(target=print_cube,args=(5,),name="t_cube")
#t2 user defined object of Thread class
t1.start() #execute thred then use start() inbuilt function which define Thread class
t1.join()
t2.start()
#t2.join()
print("Done")
	
