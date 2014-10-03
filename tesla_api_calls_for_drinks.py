import subprocess
import urllib2
import json, time, math


EARTH_CIRCUMFERENCE = 6378137     # earth circumference in meters


def main():

	# First Call to get the Cookie

	curl = ["curl", "--cookie-jar", "cookies.txt", "--include",
	"--request", "POST", "--header", "Content-Type: application/x-www-form-urlencoded",
	"--data-binary", "user_session%5Bemail%5D='mvanvleet@pillartechnology.com'&user_session%5Bpassword%5D=mhacks14",
	"https://portal.vn.teslamotors.com/login"]



#	curl = ["curl", "--cookie-jar", "cookies.txt", "--include",
#	"--request", "POST", "--header",
#	"Content-Type: application/x-www-form-urlencoded",
#	"--data-binary", "user_session%5Bemail%5D=string&user_session%5Bpassword%5D=string",
#	"http://localhost:8080/mockTesla/login"]

	subprocess.check_output(curl)

	# Second Call to get the vehicle number
#	get_vehicles = ["curl", "--cookie", "cookies.txt",
#	"--include", "http://localhost:8080/mockTesla/vehicles"]

	get_vehicles = ["curl", "--cookie", "cookies.txt",
	"--include", "https://portal.vn.teslamotors.com/vehicles"]
	
	print "Before", get_vehicles
	response = subprocess.check_output(get_vehicles)
	print "RESPONSE", response
	json_obj = split_json(response)


	# Third Call to get the location
#	url = "http://localhost:8080/mockTesla/vehicles/"
	url = "https://portal.vn.teslamotors.com/vehicles/"
	url = url + str(json_obj[0]["id"])
	url = url + "/command/drive_state"

	get_location = ["curl", "--cookie", "cookies.txt", "--include", url]

	# Location of the Drink Mixer
	x2 = -83.716246
	y2 = 42.292652

	latlong_b = (y2, x2)
	
	makeDrink = ["curl", "-X", "POST", "http://mixerpi.local:5001/makeDrink/?drink=-1&strong=1"]
	home = False
	gcd = 10
	while not home:
		
		response2 = subprocess.check_output(get_location)
		print "****************************************************"

		json_obj = split_json(response2)

		x1 = float(json_obj["longitude"])
		y1 = float(json_obj["latitude"])
		print "Longitude =", x1
		print "Latitude =", y1

		latlong_a = (y1, x1)

		gcd = great_circle_distance(latlong_a, latlong_b)
		
		print "GCD:", gcd


#		distance = math.sqrt( math.pow( (x2-x1) , 2) + math.pow( (y2-y1) , 2) )

#		if (distance <= 0.000064405){
		if gcd <= 40:  #Measured: 67498.0156822  #1906099578:
			home = True
			response = subprocess.check_output(makeDrink)
			#sendTexts()


		gcd = gcd - 1
		time.sleep(1)



def split_json(response):
	splits = response.split("\n")

	json_string = splits[len(splits) - 1]
#	print "Json String", json_string

	return json.loads(json_string)


def great_circle_distance(latlong_a, latlong_b):
    """
    >>> coord_pairs = [
    ...     # between eighth and 31st and eighth and 30th
    ...     [(40.750307,-73.994819), (40.749641,-73.99527)],
    ...     # sanfran to NYC ~2568 miles
    ...     [(37.784750,-122.421180), (40.714585,-74.007202)],
    ...     # about 10 feet apart
    ...     [(40.714732,-74.008091), (40.714753,-74.008074)],
    ...     # inches apart
    ...     [(40.754850,-73.975560), (40.754851,-73.975561)],
    ... ]
    
    >>> for pair in coord_pairs:
    ...     great_circle_distance(pair[0], pair[1]) # doctest: +ELLIPSIS
    83.325362855055...
    4133342.6554530...
    2.7426970360283...
    0.1396525521278...
    """
    lat1, lon1 = latlong_a
    lat2, lon2 = latlong_b
 
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = (math.sin(dLat / 2) * math.sin(dLat / 2) +
            math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * 
            math.sin(dLon / 2) * math.sin(dLon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = EARTH_CIRCUMFERENCE * c
    
    return d



def sendTexts():
	# "17346126336", "14129252235",
	nums = ["13017871566", "12402051955", "13014549285", "12408885745"]

	string = "Sending Texts to " + str(len(nums)) + " people"
	print string

	for num in nums:
		response = urllib2.urlopen("https://rest.nexmo.com/sms/json?api_key=6bcf5019&api_secret=af5073ab&from=15022193792&to=" + num + "&text=The%20Party%20is%20ON!%20I%20have%20Margaritas!")



def main2():
	x2 = -83.716246
	y2 = 42.292652

	latlong_b = (y2, x2)

	x1 = -83.716298
	y1 = 42.292614

	latlong_a = (y1, x1)

	gcd = great_circle_distance(latlong_a,latlong_b)
	print "GCD:", gcd



main()



