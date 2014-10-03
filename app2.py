#!flask/bin/python
from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

#tasks = [
#    {
#        'id': 1,
#        'drink': u'Buy groceries',
#        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
#        'done': False
#    }
#]

@app.route('/')
def form():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug = True)


#@app.errorhandler(404)
#def not_found(error):
#    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.route('/post/', methods = ['POST'])#, 'GET'])
def create_task():
    #if not request.json or not 'drink' in request.json:
    #    abort(400)
    
    #                     json
    drink_index = request.form['drink']
    strong = request.form['strong']
    #drink_index = request.json.get('drink', "")
    #strong = request.json.get('strong', ""),
    
    if drink_index != None and strong != None:
        drink_index = int(drink_index)
        strong = int(strong)

        print "Drink:", drink_index
        print "Strong:", strong

        return jsonify( { 'drink_index' : drink_index, 'strong' : strong } ), 200
    
    else:
        return jsonify( { 'Error' : 'Must have drink_index and strong as parameters.'})


