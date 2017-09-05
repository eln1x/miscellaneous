#!/usr/bin/env python
from Queue import Queue
from threading import Thread
from datetime import datetime
from time import sleep
print datetime.now()
num_threads = 20 ## 20 process that will work 
data =  [ x for x in range(20)]  # this will genrate  a list  like [0, 1, 2, 3, 4, 5, 6, 7, 8,  => 10000 ]
q = Queue(maxsize=0)  # we will move data items to this Queue letter  


#your app logic here 
def Operation(item):
	#this task take item and print it  no more  
	#example 2*2
#	print item
    sleep(item)
    return None


## here we run threads
def FireThreads(q):
	while True:   ## infinty looop to get  all items 
		item = q.get()  # we get item from queue 
		Operation(item)   # we run our logic againest this  item 
		q.task_done()  # we remove it from queue 


## add the data  to the queue 
for item  in data:
	q.put(item)   ### putting our data in the queue

for i in range(num_threads):    # create 20 thread 
	worker = Thread(target=FireThreads, args=(q,))  # prepare  the  thread with the 
	worker.setDaemon(True)   # make the parrent process running 
	worker.start()   # run the task 

q.join()  # Blocks until all items in the queue have been gotten and processed.
print datetime.now() 
