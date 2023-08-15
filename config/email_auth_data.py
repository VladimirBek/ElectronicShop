import json

with open('config/emailconfig.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


EMAIL = data['email']
PASSWORD = data['password']