
import subprocess
import urllib2
import json, time, math


def main():
	get_vehicles = ["curl", "--cookie", "cookies.txt",
	"--include", "https://portal.vn.teslamotors.com/vehicles"]
	
	print "Before", get_vehicles
	response = subprocess.check_output(get_vehicles)
	print "RESPONSE", response
	json_obj = split_json(response)


	# Third Call to get the location
	url = "https://portal.vn.teslamotors.com/vehicles/"
	url = url + str(json_obj[0]["id"])
	url = url + "/command/drive_state"

	get_location = ["curl", "--cookie", "cookies.txt", "--include", url]


	while True:
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

main()