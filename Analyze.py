""" 
Analyze data 
Daily object or MultiDays object
"""
 
from collections import Counter

class Analyze(object):
	"""docstring for Analyze"""
	def __init__(self, dataPackage):
		self.dataPackage = dataPackage
		self.split_time()

	def split_time(self):
		self.day = []
		self.hour = []
		self.period = []
		for t in self.dataPackage.time:
			divide = t.split(" ")
			self.day.append(divide[0])
			self.hour.append(int(divide[1].split(".")[0])) #disregard minutes and seconds
			self.period.append(divide[2])

	def identity(self):
		idDict = dict()
		for idx in range(0,len(self.dataPackage.ip_add)):		
			if idDict.get(self.dataPackage.ip_add[idx])is None:
				idDict[self.dataPackage.ip_add[idx]] = [self.dataPackage.identityid[idx]]
			else:
				if self.dataPackage.identityid[idx] not in set(idDict.get(self.dataPackage.ip_add[idx])):
					idDict.get(self.dataPackage.ip_add[idx]).append(self.dataPackage.identityid[idx])
		return idDict

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
		for idx in range(0,len(self.dataPackage.ip_add)):
			if session.get(self.dataPackage.ip_add[idx]) is None:
				session[self.dataPackage.ip_add[idx]] = [self.dataPackage.sessionid[idx]]
			else:
				if self.dataPackage.sessionid[idx] not in set(session.get(self.dataPackage.ip_add[idx])):
					session.get(self.dataPackage.ip_add[idx]).append(self.dataPackage.sessionid[idx])
		return session

	#how many IPs per session
	def Analyze_by_session(self,num_of_item):
		IPs = dict()

		for idx in range(0,len(self.dataPackage.sessionid)):
			if IPs.get(self.dataPackage.sessionid[idx]) is None:
				IPs[self.dataPackage.sessionid[idx]] = [self.dataPackage.ip_add[idx]]
			else:
				if self.dataPackage.ip_add[idx] not in set(IPs.get(self.dataPackage.sessionid[idx])):
					IPs.get(self.dataPackage.sessionid[idx]).append(self.dataPackage.ip_add[idx])

		
		session_Download = dict()

		for idx in range(0,len(self.dataPackage.sessionid)):
			if session_Download.get(self.dataPackage.sessionid[idx]) is None:
				session_Download[self.dataPackage.sessionid[idx]] = [self.dataPackage.item_id[idx]]
			else:
				if self.dataPackage.item_id[idx] not in set(IPs.get(self.dataPackage.sessionid[idx])):
					session_Download.get(self.dataPackage.sessionid[idx]).append(self.dataPackage.item_id[idx])


		most_freq_sessionid = Counter(self.dataPackage.sessionid).most_common(num_of_item)
		print("Most frequently visited session ids: \n")
		for s in most_freq_sessionid:
			print("Session ID: {}, visited {} time(s).".format(s[0],s[1]))
			print("IP: {}".format(IPs.get(s[0])))
			print("The session downloaded {} items. \n Deatils: \n {} \n\n".format(len(session_Download.get(s[0])),session_Download.get(s[0])))

	def ip_freq(self,num_of_item):
		ip_freq = Counter(self.dataPackage.ip_add)
		#self.most_frequent used in self.detail()
		self.most_frequent = ip_freq.most_common(num_of_item)

	#IP correspond to item
	def item(self):
		item = dict()
		for idx in range(0,len(self.dataPackage.ip_add)):
			if item.get(self.dataPackage.ip_add[idx]) is None:
				item[self.dataPackage.ip_add[idx]] = [self.dataPackage.item_id[idx]]
			else:
				if self.dataPackage.item_id[idx] not in set(item.get(self.dataPackage.ip_add[idx])):
					item.get(self.dataPackage.ip_add[idx]).append(self.dataPackage.item_id[idx])
		return item

	def item_count(self,num_of_item):
		c = Counter (self.dataPackage.item_id)
		item_list = c.most_common(num_of_item)
		for i in item_list:
			print("Content: {} | Download volume: {} \n".format(i[0],i[1]))

	#print out the detail information
	def detail(self):
		itemDict = self.item()
		sessionDict = self.session()
		identityDict = self.identity()
		for ip in self.most_frequent:
			print("IP: {} visited the sites {} times. ".format(ip[0],ip[1]))
			print("Identity ID: {}".format(identityDict.get(ip[0])[0]))
			print("This IP address downloaded {} contents".format(len(itemDict.get(ip[0]))))
			#print(itemDict.get(ip[0]))
			print("Number of session ID: {}".format(len(sessionDict.get(ip[0]))))
			print("Session ID: {}".format(sessionDict.get(ip[0])))
			print("\n \n \n")

if __name__ =="__main__":
	pass
