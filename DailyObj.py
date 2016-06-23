"""
Code written by William CAO June 2016

Calculate certain appeareance frequencies


Lists that can be accessed
self.identityid, self.sessionid, self.ip_add, self.item_id, self.source
self.time, self.day, self.hour, self.period

functions:
convert(), time_freq(), ip_freq(), itme(), item_count(), detail()
"""

import csv 
from collections import Counter


class DailyObj:
	def __init__(self,path):
		self.path = path

	def convert(self):
		self.identityid = []
		self.time = []
		self.sessionid = []	
		self.ip_add = []
		self.item_id = [] 
		self.source = []

		with open(self.path,newline='') as csvfile:
			reader = csv.reader(csvfile,delimiter=',')
			for row in reader:
				self.identityid.append(row[1])
				self.time.append(row[2])
				self.sessionid.append(row[3])
				self.ip_add.append(row[4])
				self.item_id.append(row[6])
				self.source.append(row[9])
		
		#get rid of the labels
		self.time.pop(0)
		self.identityid.pop(0)
		self.sessionid.pop(0)
		self.ip_add.pop(0)
		self.item_id.pop(0)
		self.source.pop(0)

		#split the time 
		self.split()

		#create a dict
		self.result = dict()
		for idx in range(0,len(self.ip_add)):		
			if self.result.get(self.ip_add[idx])is None:
				self.result[self.ip_add[idx]] = [self.identityid[idx]]
			else:
				if self.identityid[idx] not in set(self.result.get(self.ip_add[idx])):
					self.result.get(self.ip_add[idx]).append(self.identityid[idx])
					



	def split(self):
		self.day = []
		self.hour = []
		self.period = []
		for a in self.time:
			divide = a.split(" ")
			self.day.append(divide[0])
			self.hour.append(int(divide[1].split(".")[0])) #disregard minutes and seconds
			self.period.append(divide[2])

	def time_freq(self):
		#convert to 24 H format
		for idx in range(0,len(self.period)):
			if (self.period[idx] == "AM") and (self.hour[idx]==12):
				self.hour[idx]-=12
			if (self.period[idx] == "PM") and (self.hour[idx]!=12):
				self.hour[idx]+=12
		h_list = Counter(self.hour).most_common(24) #showing how many results
		for h in h_list:
			print("Time: {}:00 (GMT+2), page view: {} \n".format(h[0],h[1]))

	#how many session ids per IP address
	def session(self):
		session = dict()
		for idx in range(0,len(self.ip_add)):
			if session.get(self.ip_add[idx]) is None:
				session[self.ip_add[idx]] = [self.sessionid[idx]]
			else:
				if self.sessionid[idx] not in set(session.get(self.ip_add[idx])):
					session.get(self.ip_add[idx]).append(self.sessionid[idx])
		return session

	#how many IPs per session
	def Analyze_by_session(self,num_of_item):
		IPs = dict()

		for idx in range(0,len(self.sessionid)):
			if IPs.get(self.sessionid[idx]) is None:
				IPs[self.sessionid[idx]] = [self.ip_add[idx]]
			else:
				if self.ip_add[idx] not in set(IPs.get(self.sessionid[idx])):
					IPs.get(self.sessionid[idx]).append(self.ip_add[idx])

		
		session_Download = dict()

		for idx in range(0,len(self.sessionid)):
			if session_Download.get(self.sessionid[idx]) is None:
				session_Download[self.sessionid[idx]] = [self.item_id[idx]]
			else:
				if self.item_id[idx] not in set(IPs.get(self.sessionid[idx])):
					session_Download.get(self.sessionid[idx]).append(self.item_id[idx])


		most_freq_sessionid = Counter(self.sessionid).most_common(num_of_item)
		print("Most frequently visited session ids: \n")
		for s in most_freq_sessionid:
			print("Session ID: {}, visited {} time(s).".format(s[0],s[1]))
			print("IP: {}".format(IPs.get(s[0])))
			print("The session downloaded {} items. \n Deatils: \n {} \n\n".format(len(session_Download.get(s[0])),session_Download.get(s[0])))
	
	def ip_freq(self,num_of_item):
		ip_freq = Counter(self.ip_add)
		self.most_frequent = ip_freq.most_common(num_of_item)

	#IP correspond to item
	def item(self):
		item = dict()
		for idx in range(0,len(self.ip_add)):
			if item.get(self.ip_add[idx]) is None:
				item[self.ip_add[idx]] = [self.item_id[idx]]
			else:
				if self.item_id[idx] not in set(item.get(self.ip_add[idx])):
					item.get(self.ip_add[idx]).append(self.item_id[idx])
		return item

	def item_count(self,num_of_item):
		c = Counter (self.item_id)
		item_list = c.most_common(num_of_item)
		for i in item_list:
			print("Content: {} | Download volume: {} \n".format(i[0],i[1]))

	#print out the detail information
	def detail(self):
		itemDict = self.item()
		sessionDict = self.session()
		for ip in self.most_frequent:
			print("IP: {} visited the sites {} times. ".format(ip[0],ip[1]))
			print("Identity ID: {}".format(self.result.get(ip[0])[0]))
			print("This IP address downloaded {} contents".format(len(itemDict.get(ip[0]))))
			#print(itemDict.get(ip[0]))
			print("Number of session ID: {}".format(len(sessionDict.get(ip[0]))))
			print("Session ID: {}".format(sessionDict.get(ip[0])))
			print("\n \n \n")
	
	


if __name__ =="__main__":

	#Example
	f1 = DailyObj("oecddaily20160531.csv")
	#convert to clean data
	f1.convert()
	#most frequently visited time of the day
	f1.time_freq()
	#most frequently visited IP address
	f1.ip_freq(10)
	#detail information 
	f1.detail()
	#most frequently downloaded content
	f1.item_count(10)
	#most frequently visited session id
	f1.Analyze_by_session(10)
	"""
	for ip in f1.most_frequent:
		identity = f1.result.get(ip[0])
		if len(identity) > 1:
			print(ip)
			print(identity)
			print("\n")
	"""


	

	