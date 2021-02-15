from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': u'Asaawari',
        'contactnumber': u'7439076393', 
        'done': False
    },
    {
        'id': 2,
        'name': u'Amit',
        'contactnumber': u'9830332508', 
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "Message": "Please provide the data"
        },400)
    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'contactnumber': request.json.get('contactnumber', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "Status":"Success",
        "Message": "Contact added succesfully"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)