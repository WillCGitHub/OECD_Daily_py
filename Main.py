from Daily import Daily
from MultiDays import MultiDays
from Analyze import Analyze 
import os
from os import listdir
from os.path import isfile,join
import sys
from functools import reduce
import sys



#do not read in hidden files
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

filePath ="Dataset"
fileList = listdir_nohidden(filePath)
process_list = []

for file in fileList:
	#get file path name
	file = join(filePath,file)
	temp = Daily(file)
	process_list.append(temp)


multi = reduce(lambda x,y: x+y, process_list)

print(multi)

an = Analyze(multi)
#an.time_freq()
#most frequently visited IP address

#increase this number in order to fulfill the 
#number of results to show in registered and 
#unregistered user.
an.ip_freq(300)


	
#detail information 
an.detail()

#There might not enough registered user to show.
#output registered user 
fileName = "Registered_User_{}_{}".format(an.day[0],an.day[-1])

with open('Result/{}.txt'.format(fileName), 'w') as f:
	sys.stdout = f
	an.print_registered_user(30)

#output unregistered user
fileName = "Unregistered_User_{}_{}".format(an.day[0],an.day[-1])
sys.stdout = open('Result/{}.txt'.format(fileName), 'w')
an.print_unregistered_user(30)


#most frequently downloaded content
#an.item_count(10)

#most frequently visited session id
#thier IPs, and content downloaded
#an.Analyze_by_session(10)

