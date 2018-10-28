from flask import Flask, request
import json

def str_user(user):
    return 'name: '+user['name']+' email: '+user['email']+ ' birth date: '+user['birth_date']

app = Flask(__name__)

users = []
email_list=[i[email] for i in users]
contador = 0

@app.route('/')
def home():
    return 'Home'

@app.route('/api/v1/user', methods=['POST'])
def postJson():
    global contador
    global email_list

    if request.method ==  'POST':
        user = request.get_data(as_text=True)
        user = json.loads(user)
        if user['email'] in email_list:
            return 'ERRO: Este endereço de email já foi cadastrado!'
        user['id'] = contador +1
        contador =+ 1
        email_list.append(user['email'])
        users.append(user)
        return 'id: '+ str(user['id'])
    #teste com:  curl -X POST --data '{"name":"Witalo Pietler","email":"witalopietler@gmail.com","birth_date":"28/01/1999"}' "http://127.0.0.1:5000/api/v1/user"

@app.route('/api/v1/user')
def getLimit(): 
    if request.args['limit'] == '':
        limit = 10
    else:
        limit = int(request.args['limit'])
    
    if len(users)<=limit:
        out =''
        for i in users:
            out = out + str_user(i)
            out = out + '\n'
        return out
    else:
        out= ''
        for i in users[0:limit]:
            out = out + str_user(i)
            out = out + '\n'
        return out
        
@app.route('/api/v1/user/<int:userid>', methods=['GET', 'DELETE'])
def userId(userid):
    global users
    if request.method == 'GET':
        for i in users:
            if userid == i['id']:
                return str_user(i)
        return 'ERRO: Este ID não existe!'
    if request.method == 'DELETE':
        for i in users:
            if userid == i['id']:
                users.remove(i)
                return 'Usuário deletado!'
        return 'ERRO: Este ID não existe'

app.run(use_reloader=True)