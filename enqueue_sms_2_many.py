import json
import uuid
import requests

# enqueue 10000 jobs
for i in xrange(10000):
    response = requests.post(
        'http://localhost:8080/enqueue/sms/2/',
        data=json.dumps({
            # generate unique job_id for each request
            'job_id': str(uuid.uuid4()),
            'interval': 3000,  # means a rate of 1 job per second
            'payload': {'message': 'hello, world - from queue 2'}
        }),
        headers={'Content-Type': 'application/json'}
    )
    print json.loads(response.text)
