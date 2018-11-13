import json

class fakeDB(object):
    def __init__(self):
        self.users = []
        self.emails = []
        self.counter = 0

    def addUser(self, user):
        if user['email'] in self.emails:
            return 'ERRO: Este endereço de email já foi cadastrado!'
        user['id'] = self.counter +1
        self.counter =+ 1
        self.emails.append(user['email'])
        self.users.append(user)
        return 'id: '+ str(user['id'])
    
    #def get_users(self, limit=10):
    def getUserLimit(self, limit):
        if limit == '':
            limit = 10
        else:
            limit = int(limit)
        if len(self.users)<=limit:
            return json.dumps(self.users)
        else:
            return json.dumps(self.users[len(self.users)-limit-1:len(self.users)-1]) #Reduzir 
    
    def getUserId(self, userId):
        for i in self.users:
                if userId == i['id']:
                    return json.dumps(i)
        return 'ERRO: Este ID não existe'

    def delUser(self, userId):
        for i in self.users:
            if userId == i['id']:
                self.users.remove(i)
                return 'Usuário deletado!'
        return 'ERRO: Este ID não existe'
