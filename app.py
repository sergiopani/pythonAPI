#Tell python that we want to be able to flask
from flask import Flask,jsonify,request,render_template
#__name__ tells an unic name 
app = Flask(__name__)

#Diccionari with a lot of stores
stores = [
    {
        'name': "La tienda de Sergio",
        'items':[
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]
@app.route('/')
def home():
    return render_template('index.html')
#Tell our app what request its going to undertand??

#POST -> Used to recieve deta
#GET -> Used to send data back only
#Tell the app to start running at the specific port

#POST /store data:{name}
#Only accesible by a post request because the default on browsers is a GET
@app.route('/store',methods=['POST'])
#Accest the data of request
def create_store():
    #The browser send us some json data
    request_data = request.get_json();
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
#<string:name> is a flask sintax to make obligatory a name parametrer and to be string formated
@app.route('/store/<string:name>')#http://127.0.0.1:5000/store/some_name
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})

#GET /store
@app.route('/store')#http://127.0.0.1:5000/store/some_name
def get_stores():
    #Return a JSON, the problem is that json is not dictionari, so we have to jsonnify
    #Convert our list of stores, to a dictionari becouse jason only understand dictionary
    return jsonify({'stores':stores})

#POST /store/<string:name>
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json
    for store in stores: 
        if store['name'] == name:
            store['items'].append({
                'name':request_data['name'],
                'price': request_data['price']
            })
            return jsonify({'New item Added': stores[len(stores)-1]})
    return jsonify({'message': 'Store not found!'})

#GET /store/<string:name>/item
#GET /store
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})


app.run(port=5000)
