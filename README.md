# OECD_Daily_py

Analyze OECD Daily data. 

###Daily object and MultiDays object

```python
d1 = Daily("filename1.csv")

d2 = Daily("filename2.csv")

d = d1 + d2 

```


Combining Daily object will form a MultiDays object. 

###Analyze.py
Analyze.py contains most of the core functions. 

Analyze Object will take in either Daily object or MultiDays object

```python
an = Analyze(d)

an.ip_freq(300)  # show the top 300 most frequently visited IPs
an.detail()      # classify IPs by registered and unregistered users
an.print_registered_user(30) # top 30 registered users
an.print_unregistered_user(30) # top 30 unregistered users
IP = '192.168.1.1'
result = an.GeoIP("IP")  
# GeoIP function use ipinfo's API to check for IP details, it will return a JSON file
print(result.get('city'))

an.item_count(10) #most frequently downloaded content

an.Analyze_by_session(10)

#most frequently visited session id
#thier IPs, and content downloaded
```