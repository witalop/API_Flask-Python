from flask import Flask, request
from fakeDb import fakeDB
import json

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
            return self.db.addUser(user)
#teste com:  curl -X POST --data '{"name":"Witalo Pietler","email":"witalopietler@gmail.com","birth_date":"28/01/1999"}' "http://127.0.0.1:5000/api/v1/user"
        
        if request.method == 'GET':
            limit = request.args['limit']
            return self.db.getUserLimit(limit)
            
    def userId(self, userId):
        userId = int(userId)
        if request.method == 'GET':
            return self.db.getUserId(userId)

        if request.method == 'DELETE':
            return self.db.delUser(userId)
#teste com: curl -X DELETE "link"

app =service()
app.server.run(use_reloader=True)