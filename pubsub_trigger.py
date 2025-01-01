import os
from google.cloud import pubsub_v1
import json


project_id = os.getenv("PROJECT_ID")
sub_id = os.getenv("SUB_ID")

print("started ---- listening the surrounding")
subscriber = pubsub_v1.SubscriberClient()
subscripion_path = subscriber.subscription_path(project_id,sub_id)

def callback(msg):
    
    try :
        
        print(f"Received message: {msg.data.decode('utf-8')}")
        print(f"==> got here {msg} ")

        msg.ack()

    except Exception as e :
        print("smth went wrong :  => ",e)
        msg.nack()


subscriber_pull = subscriber.subscribe(subscripion_path,callback)


try :

    #continously listenig 
    subscriber_pull.result()

except KeyboardInterrupt :
    subscriber_pull.cancel()

    print("---done")