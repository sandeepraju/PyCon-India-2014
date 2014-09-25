import time
import json
import requests

while True:
    # dequeue the job from the queue of type `sms`
    try:
        response = requests.get('http://localhost:8080/dequeue/sms/')

        if response.status_code == 200:
            # successful dequeue.
            r = json.loads(response.text)
            print r['payload']  # process the payload here.

            queue_id = r['queue_id']
            job_id = r['job_id']
            # mark the job as completed successfully by
            # sending a finish request.
            requests.post(
                'http://localhost:8080/finish/sms/%s/%s/' % (queue_id, job_id)
            )
        elif response.status_code == 404:
            # no job found (either queue is empty or none
            # of the jobs are ready yet).
            print 'waiting for jobs'
            time.sleep(0.25)  # wait before retrying if needed.
    except Exception as e:
        print 'Something went wrong!'
        time.sleep(5)  # retry after 5 seconds.
