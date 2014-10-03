# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import RPi.GPIO as GPIO
import time
import serial

# Initialize the Flask application
app = Flask(__name__)

lcky = 11
strng = 13
sel = 15
lft = 19
rght = 21


# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return 'Send a drink number and a 0/1 for a strong drink.' #render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/post/', methods=['POST'])
def handle_post():
    #name=request.form['yourname']
    drinkNumber = request.form['drink']
    strong = request.form['strong']

    print "Drink:", drink
    print "Strong:", strong
    
    print "Begin Set-up"

    ser = serial.Serial('/dev/tty.usbmodem1421', 9600) #/dev/ttyAMA0

    print "Writing Drink Number"

    ser.write(drinkNumber)
    time.sleep(.25)

    print "Writing Strong Number"

    ser.write(strong)
    time.sleep(.25)


'''
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(lcky, GPIO.OUT, pull_up_down = GPIO.PUD_UP) # lucky seven
    GPIO.setup(strng, GPIO.OUT, pull_up_down = GPIO.PUD_UP) # strong
    GPIO.setup(sel, GPIO.OUT, pull_up_down = GPIO.PUD_UP) # select


    GPIO.setup(lft, GPIO.OUT, pull_up_down = GPIO.PUD_UP) # left
    GPIO.setup(rght, GPIO.OUT, pull_up_down = GPIO.PUD_UP) # right

    while True:
    
	    if drinkNumber < 0:
	    	GPIO.output(lcky, 0)
	    	time.sleep(500)
	    	GPIO.output(lcky, 1)
	    	time.sleep(9500)
	    
	    if strong:
	    	GPIO.output(strng, 0)
	    	time.sleep(500)
	    	GPIO.output(strng, 1)
	    	time.sleep(2500)
	    
	    else:
	    	spin = drinkNumber % 8;
	    
	    if drinkNumber >= 8:
	    	spin = 8 - spin
	    	
	    	for n in range(spin):
	    		GPIO.output(lft, 0)
	    		time.sleep(500)
	    		GPIO.output(lft, 1)
	    		time.sleep(500)
	    
	    else:
	    	for n in range(spin):
		    	GPIO.output(right, 0)
		    	time.sleep(500)
		    	GPIO.output(right, 1)
		    	time.sleep(500)
	    
	    GPIO.output(sel, 0)
	    time.sleep(500)
	    GPIO.output(sel, 1)
	    time.sleep(20000)


    GPIO.cleanup()
'''
	
    print "Done"
    
    return 'OK\n' #render_template('form_action.html', name=name, email=email)


# Run the app :)
if __name__ == '__main__':
  app.run( )#host="0.0.0.0", port=int("80"))
