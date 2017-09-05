#!/usr/bin/env python 
# encoding=utf8
#dailymoe database formater
#writin by Ahmad Mahfouz
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import csv
import demjson



def Product_title(title):
	data = {}
	if len(title) <=1 :
		data['zh'] = "NULL"
		data['en'] = "NULL"
		return data 
	try:
		titles = demjson.decode(title)
		zh =   titles['zh'].strip()
		en =  titles['en'].strip()
		data['zh'] = zh
		data['en'] = en

	except:
		en =  title.strip()
		data['en'] = title.strip()
		data['zh'] = title.strip()


	return data

def Product_image(image):
	if image.endswith(".jpg") or image.endswith(".png"):
		return image
	else:
		return "default.jpg"

def Product_specification(specification):
	data = {}
	try:
		specification = demjson.decode(specification)
		data['zh']= specification['zh']
		data['en']= specification['en']
		return data
	except:

		data['zh']= "NULL"
		data['en']= "NULL"
		return data

def Product_Stock(stock):
	try:
		int(stock)
		return stock
	except:
		return 0

def  Product_Summery(summary):
	data = {}

	try:
		summary = demjson.decode(summary)
		data['zh'] = summary['zh']
		data['en'] = summary['en']
	except:
		data['zh'] = "NULL"
		data['en'] = "NULL"

	return data

def Product_Content(content):

	data = {}
	try:
		content = demjson.decode(content)
		data['zh'] = content['zh']
		data['en'] = content['en']
	except:
		data['zh']= "NULL"
		data['en']= "NULL"

	return data

def Product_Price(price):
	# print price
	if price == None:
		return 0
	price = price.strip()

	if "red" in price:
		return 0

	if float(price) > 0 :
		return price
	else:
		return 0

def Products():
	with open('proudcts.csv','rb') as products:
		spamreader = csv.DictReader(products)
		for row in spamreader:
		#print spamreader.fieldnames     
			if row['category_id'] == None:	
				continue
			print "#" * 10
			print "Catregory ID : %s" % row['category_id']
			#//title


			titles = Product_title(row['title'])
			print "china title %s" %titles['zh']
			print "english title %s " %titles['en'] 
			specs = Product_specification(row['specification'])
			print "china specs %s" %specs['zh']
			print "english specs %s" %specs['en']

			#//images
			print Product_image(row['listimg_url'])

			# stock
			print "stock : " + str(Product_Stock(row['stock']))

			# summery

			summery = Product_Summery(row['summary'])
			print "china summary:  %s" %summery['zh']
			print "english summary:  %s" %summery['en']

			content = Product_Content(row['content'])
			print "china content: %s " % content["zh"]
			print "english content: %s " % content["en"]
			# print row['price']
			print "price:  %s"  % Product_Price(row['price'])

# print Products()


def Categories():
	with open('categories.csv','rb') as categories:
#with open('categories.csv','rb') as categories:
		spamreader = csv.DictReader(categories)
		for row in spamreader:
			#print ', '.join(row)
			print "#" * 10
			print "ID: " +  row['\xef\xbb\xbfid']
			print "Parent ID: " +  row['parent_id']
			try:
				titles = demjson.decode(row['title'])
				print "China Title : " + titles['zh']
				print "Englis Title : " + titles['en']
			except:
				print row['title']

def Users():
	# ['\xef\xbb\xbfid', 'group_id', 'user_name', 'password', 'salt', 'email', 'nick_name', 'avatar', 'sex', 'birthday', 'telphone', 'mobile', 
	# 'qq', 'first_name', 'last_name', 'address', 'live_address', 'home_address', 'safe_question', 'safe_answer', 'amount', 'point', 'exp', 
	# 'status', 'reg_time', 'reg_ip', 'city_id', 'last_ip', 'lastlogintime', 'this_ip', 'thislogintime', 'is_top', 'marital_status', 
	# 'highest_degree', 'industry', 'position', 'monthly_income', 'native', 'constellation', 'signature', 'promotion_id', 
	# 'promotion_code', 'is_setdraw', 'drawing_password', 'drawing_salt', 'pwd_strength', 'account_security_level', 'id_card', 'is_idcardactive', 
	# 'mobile_code', 'mobile_code_time', 'is_mobileactive', 'usermobiletemp', 'email_code', 'email_code_time', 'is_emailactive', 'useremailtemp', 
	# 'fpwd_m_code', 'fpwd_m_code_time', 'fpwdmobiletemp', 'fpwd_e_code', 'fpwd_e_code_time', 'fpwdemailtemp', 'fpwd_enable_time',
	#  'money', 'total_commission', 'current_commission', 'used_commission', 'fund_money', 'risk_money', 'stop_money', 'frozen_money', 
	#  'is_promoed', 'wxuser_id', 'is_setpay', 'pay_password', 'pay_salt', 'real_name', 'mobile_bind_status', 'email_bind_status', 'now_point', 
	#  'next_point', 'mass_status']
	with open('users.csv','rb') as user:
		spamreader = csv.DictReader(user)
		print spamreader.fieldnames
		for row in spamreader:
			print row['user_name']
			print row['email']
			print row['sex']
			print row['birthday']
			print row['telphone']
			print row['mobile']
			print row['first_name']
			print row['last_name']
			print row['last_name']
			print row['real_name']
			print "#" * 10
			

print Users()