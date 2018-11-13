import json
import requests

o = 0
while o =! 'exit':
    o = input('Option: ')
    if o == 'GET':
        limit = input('limit: ')
        url = 'http://127.0.0.1:5000/api/v1/user?limit=' + limit
        r = requests.get(url)

    elif o == 'POST':
        user = input('User: ')
        r = requests.post(url=http://127.0.0.1:5000/api/v1/user, content=user)

    elif o == 'DELETE':
        pass