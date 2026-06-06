from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def default():
    return f'Hello World'

@app.route('/<name>')
def hello(name):
    return f'Hello {name}!'

@app.route('/handle_params')
def _handle_routes():
    if "name" in request.args.keys() and "id" in request.args.keys():
        id = int(request.args.get('id'))
        name = request.args.get('name')
        return f'Hey {name} you Id is {id}'
    else:
        return f'url not found'

@app.route('/handle_methods', methods=['GET','POST'])
def handle_methods():
    if request.methods=='GET':
        return f'it is a get request'
    elif request.methods=="POST":
        return f'it is post request'

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True)