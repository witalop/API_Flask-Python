from flask import Flask, request
import json


app = Flask(__name__)

users = []
email_list=[i.email for i in users]

@app.route('/')
def home():
    return 'Home'

@app.route('/api/v1/user', methods=['POST'])
def postJson():
    if request.method ==  'POST':
        user = request.get_data()
        user = json.loads(user)
        if user.email in email_list:
            return 'Este email já está cadastrado!'
        else:
            user['id'] = len(user)+1
            users.append(user)
            return 'id: '+ user.id


app.run(use_reloader=True, debug=True)