import urllib
import urllib2
import json

def main():


#	response = urllib2.urlopen("http://localhost:8080/mockTesla/login")
#	print response.read()
	#array = json.loads(response)

#	for i in array:
#		print i

#	employees_array = json.loads(employees)



	url = 'http://localhost:8080/mockTesla/login'
	values = {'cookie-jar' : 'cookies.txt',
	          'header' : 'Content-Type: application/x-www-form-urlencoded',
	          'data-binary' : 'user_session%5Bemail%5D=string&user_session%5Bpassword%5D=string' }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page

main()