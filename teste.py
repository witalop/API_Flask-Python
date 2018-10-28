import json

users = []

email_list=[i[email] for i in users]
user = '{"name":"Witalo Pietler","email":"witalopietler@gmail.com","birth_date":{"dia":28,"mes":1,"ano":1999}}'

user = json.loads(user)
if len(users)!=0:
    if user[email] in email_list:
        print ('Este endereço de email já foi cadastrado!')
else:
    user['id'] = int(max(users))+1
    users.append(user)
    print ('id: '+ str(user['id']))

print(users)