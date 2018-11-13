import json
import requests
import sys


countArgs = len(sys.argv)

if sys.argv[1] == 'get':
    if sys.argv[2] == '-l':
        if countArgs == 3:
            limit = ''
        else:
            limit = str(sys.argv[3])
        url = 'http://127.0.0.1:5000/api/v1/user?limit=' + limit
    elif sys.argv[2] == '-i':
        id_ = sys.argv[3]
        url = 'http://127.0.0.1:5000/api/v1/user?user=' + id_
    r = requests.get(url)
    print (r.json())

elif sys.argv[1] == 'add':
    name = sys.argv[2]
    email = sys.argv[3]
    birth_date = sys.argv[4]
    user = {"name":name,"email":email,"birth_date":birth_date}
    r = requests.post(url='http://127.0.0.1:5000/api/v1/user', json=user)
    print (r.json())

elif sys.argv[1] == 'del':
    id_ = sys.argv[2]
    r = requests.delete(url='http://127.0.0.1:5000/api/v1/user/'+id_)
    print (r.json())