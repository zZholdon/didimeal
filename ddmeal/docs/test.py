import httplib, urllib
params = urllib.urlencode({'username':"cjs", 'password':"cjs"})
headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain"}
conn = httplib.HTTPConnection("127.0.0.1:8000")
conn.request("POST", "/ddmeal/login/", params, headers)
response = conn.getresponse()
print response.status
data = response.read()
conn.close()

import httplib, urllib
params = urllib.urlencode({'username':"cjs", 'password':"cjs"})
headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain"}
conn = httplib.HTTPConnection("didimeal.sinaapp.com")
conn.request("POST", "/ddmeal/login/", params, headers)
response = conn.getresponse()
print response.status
data = response.read()
conn.close()

# index
import httplib, urllib
headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain"}
conn = httplib.HTTPConnection("didimeal.sinaapp.com")
conn.request("GET", "/ddmeal/index/")
conn.add_header('cookie', 'username=cjs')
response = conn.getresponse()
print response.status
data = response.read()
conn.close()

