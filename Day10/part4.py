#fetching pages form server

import http.client
c= http.client.HTTPSConnection("docs.python.org")# page to be fetched
c.putrequest("GET","/3/tutorial/index.html")
c.putheader("someheader","somevalue")
c.endheaders()

r = c.getresponse()
data = r.read()
filename = open("filename.html",'w')
filename.write(str(data,'utf-8'))
#print(data)
c.close()