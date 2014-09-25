import json
import requests

response = requests.post('http://localhost:8080/interval/sms/1/',
                         data=json.dumps({'interval': 5000}),
                         headers={'Content-Type': 'application/json'})
