import urllib2

def main():

	nums = ["12402051955", "13014549285", "12408885745", "13017871566"]

	for num in nums:
		response = urllib2.urlopen("https://rest.nexmo.com/sms/json?api_key=6bcf5019&api_secret=af5073ab&from=15022193792&to=" + num + "&text=The%20Party%20is%20ON!%20I%20have%20Margaritas!")

main()

