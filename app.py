from flask import Flask, jsonify, request  
app = Flask(__name__)

List = [ {
    "data": [
        {
            "Contact": "9987644456",
            "Name": "Raju",
            "done": False,
            "id": 1
        },
        {
            "Contact": "9876543222",
            "Name": "Rahul",
            "done": False,
            "id": 1
        }
    ]
 } ]

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/add-Data', methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status': 'Error',
            'message': 'Please Provide the Data'
        }, 400) 

    contact = { 'id': List[-1]['id'] + 1,
     'Name': request.json['Name'],
      'contact': request.json.get('contact', ""),
       'done': False }

    List.append(contact)
    return jsonify({
        'status': 'SUCCESS',
        'message': 'Task Added Successfully'
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        'data': List 
        })

if __name__ == '__main__':
    app.run(debug = True)
