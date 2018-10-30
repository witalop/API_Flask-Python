from flask import Flask, request
from fakeDb import fakeDB
import json

def str_user(user):
    return 'name: '+user['name']+' email: '+user['email']+ ' birth date: '+user['birth_date']

class service(object):
    def __init__(self):
        self.db = fakeDB()
        self.server = Flask(__name__)
        self.server.add_url_rule('/', 'home', self.home)
        self.server.add_url_rule('/api/v1/user', 'user', self.user, methods=['POST', 'GET'])
        self.server.add_url_rule('/api/v1/user/<int:userId>', 'userId', self.userId, methods=['GET', 'DELETE']) 
    
    def home(self):
        return 'Homepage'

    def user(self):
        if request.method == 'POST':
            user = request.get_data(as_text=True)
            user = json.loads(user)
            if user['email'] in self.db.emails:
                return 'ERRO: Este endereço de email já foi cadastrado!'
            user['id'] = self.db.counter +1
            self.db.counter=+ 1
            self.db.emails.append(user['email'])
            self.db.users.append(user)
            return 'id: '+ str(user['id'])
#teste com:  curl -X POST --data '{"name":"Witalo Pietler","email":"witalopietler@gmail.com","birth_date":"28/01/1999"}' "http://127.0.0.1:5000/api/v1/user"
        
        if request.method == 'GET':
            if request.args['limit'] == '':
                limit = 10
            else:
                limit = int(request.args['limit'])
            
            if len(self.db.users)<=limit:
                return json.dumps(self.db.users)
            else:
                return json.dumps(self.db.users[len(users)-limit-1:len(users)-1]) #Reduzir

    def userId(self, userId):
        userId = int(userId)
        if request.method == 'GET':
            for i in self.db.users:
                if userId == i['id']:
                    return str_user(i)
            return 'ERRO: Este ID não existe!'

        if request.method == 'DELETE':
            for i in self.db.users:
                if userId == i['id']:
                    self.db.users.remove(i)
                return 'Usuário deletado!'
            return 'ERRO: Este ID não existe'
#teste com: curl -X DELETE "link"

app =service()
app.server.run(use_reloader=True)