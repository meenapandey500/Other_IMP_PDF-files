import threading 
import os

def cube(n):

	for i in range(n):
		print("cube ",i*i*i,"C_thread_name",threading.current_thread().name,"Process id",os.getpid())
	

def square(n):
	for i in range(n):
		print("square ",i*i,"C_thread_name",threading.current_thread().name,"Process id",os.getpid())


if __name__=='__main__':
	
	t1=threading.Thread(target=cube,args=(5,),name="t_cube")
	t2=threading.Thread(target=square,args=(5,),name="t_square")

	t1.start()
	t1.join()

	t2.start()
	t2.join()
	
