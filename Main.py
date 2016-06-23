from Daily import Daily
from MultiDays import MultiDays
from Analyze import Analyze 
import os
from os import listdir
from os.path import isfile,join
import sys
from functools import reduce

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
an.time_freq()
#most frequently visited IP address
an.ip_freq(10)
	
#detail information 
an.detail()
	
#most frequently downloaded content
an.item_count(10)

#most frequently visited session id
#thier IPs, and content downloaded
an.Analyze_by_session(10)
