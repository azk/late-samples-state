from datetime import datetime, timedelta
import time
import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("staging-eabb77f6",  "late-samples-state-test")

def _create_event(key, val, ts=None, now_offset=None):
    if not ts:
        ts = datetime.utcnow()
    
    if now_offset:
        ts = ts + now_offset

    print key,val,ts        
    return {
        "key": str(key),
        "value": str(val),
        "timestamp": int(time.mktime(ts.timetuple()) * 1000)
    }


futures = []

offset = timedelta(days=-60)

publisher.publish(topic_path, data=json.dumps(_create_event(999,999))).result()
time.sleep(5)
for k in xrange(2):
    for v in xrange(10):
        event = _create_event(k, v, now_offset=offset)
        futures.append(publisher.publish(topic_path, data=json.dumps(event)))
        time.sleep(3)
        

for future in futures:
    future.result()



