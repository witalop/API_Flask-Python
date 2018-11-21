from flask import jsonify
import json
import requests
import sys

command_line = {'command':sys.argv[1], 'args':dict([arg.split('=', maxsplit=1) for arg in sys.argv[2:]])}
print(command_line)

if command_line['command'] == 'get':
    if 'limit' in command_line['args'].keys():
        print (requests.get('http://127.0.0.1:5000/api/v1/user?limit=' + command_line['args']['limit']).json())
    elif 'id' in command_line['args'].keys():
        print (requests.get('http://127.0.0.1:5000/api/v1/user?user=' + command_line['args']['id']).json())
    else: print('Invalid arguments!')

elif command_line['command'] == 'add':
    if  command_line['args'].keys() == ['name', 'email', 'birth_date']:
        print (requests.post('http://127.0.0.1:5000/api/v1/user', json=command_line['args']).json())
    else: print('Invalid arguments!')

elif command_line['command'] == 'del':
    if 'id' in command_line['args'].keys():
        print (requests.delete('http://127.0.0.1:5000/api/v1/user/'+ command_line['command']['id']).json())
    else: print('Invalid arguments!')

else: print('Invalid command')