#!/usr/bin/env python
# coding=utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from BeautifulSoup import BeautifulSoup
import requests
from Queue import Queue
from threading import Thread
from threading import Lock
import sqlite3
from datetime import datetime



lock = Lock()
q = Queue(maxsize=0)
num_threads = 20
erros = open('errors.txt','a')


def  StoreDb(TargetID,name,price,details,indication,usage,usage_details,image):
	print "[ %s ]trying to save %s" % (datetime.now(),TargetID)
	lock.acquire()
	conn = sqlite3.connect('database.db')
	query = "INSERT INTO DATA (ID,NAME,price,details,indication,usage,usage_details,image)  VALUES (?,?,?,?,?,?,?,?)" 

	data = [TargetID,name,price,details,indication,usage,usage_details,image]

	conn.execute(query,data);

	conn.commit()
	conn.close()
	lock.release()


def Clean(data):
	try:
		data = data.replace("&nbsp;", " ")
		data = data.replace("*" ,"\n*")
	except:
		data = "NULL"
	return data

def PriceClean(price):
	try:
		price = price.decode('utf-8')
		price = price.replace("السعر:","")
		price = price.replace("جنية", "")
		price = price.strip()
		price = price.split(" ")[0]
		return  price
	except:
		return "NULL"

def Grab(TargetID):

	url = "http://sitename.com/index.php?route=product/product&product_id=%s" %TargetID
	try:
		r = requests.get(url)
	except:
		erros.write(x,"\n")
		return None
   	# print url
	soup = BeautifulSoup(r.text)

	try:
		name = soup.title.text
		if "!" in name:
			return None

	except:	
		name = "NULL"

	try:
		price = soup.find("div",{"class":"price"}).text
	except:
		price = "NULL"

	try:
		details = soup.find("div",{"id":"tab-description"}).text
	except:
		details = "NULL"

	try:
		indication = soup.find("div",{"id": "tab-indication"}).text
	except:
		indication = "NULL"

	try:
		usage = soup.find("div",{'id':"tab-direction"}).text
	except:
		usage = "NULL"
	try:
		usage_details = soup.find("div",{'id':"tab-effect"}).text
	except:
		usage_details = "NULL"
	try:
		image = soup.find("img",{'id':'cloud-zoom'})['src']
	except:
		image = "NULL"

	name = name
	price = PriceClean(price)
	detials = Clean(details)
	indication = Clean(indication)
	usage = Clean(usage)
	usage_details = Clean(usage_details)
	image = image
	StoreDb(TargetID,name,price,details,indication,usage,usage_details,image)

	return TargetID

def FireThreads(q):
	while True:
		TargetID = q.get()
		Grab(TargetID)
		q.task_done()


z = []
for x in range(46086,289947):
#for i in range(1,10):
#	q.put(i)
	z.append(x)

z.reverse()


for y in z:
	q.put(y)

for i in range(num_threads):
	worker = Thread(target=FireThreads, args=(q,))
	worker.setDaemon(True)
	worker.start()

q.join()
