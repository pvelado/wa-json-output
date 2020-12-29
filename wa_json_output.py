"""
Auther: Paulo Velado

wa_json_output.py: Script connects to the an WA Assistant instance using IBM's watson assistant API, inputs a utterance, 
and returns the raw json output of the utterance entered.

"""

import ibm_watson
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


    # Enter Credentials from your Watson Assistant Service
ASSISTANT_ID = "[ENTER ASSISTANT ID HERE]"
API_KEY = '[ENTER APY KEY HERE]'
VERSION = '[ENTER VERSION]'
SERVICE_URL = '[ENTER URL HERE]'

def main():
    utterance = "[ENTER UTTERANCE HERE]"
    

    authenticator = IAMAuthenticator(API_KEY)
    assistant = AssistantV2(
        version = VERSION,
        authenticator = authenticator
    )
    assistant.set_service_url(SERVICE_URL)
    assistant.set_disable_ssl_verification(True)
    
    temp = assistant.create_session(assistant_id=ASSISTANT_ID).get_result()
    session_id = temp["session_id"]
    
    assistant.message(
        assistant_id=ASSISTANT_ID,
        session_id=session_id,
        input= {"text" : ""}
    )
        
    json_output = assistant.message(
        assistant_id=ASSISTANT_ID,
        session_id=session_id,
        input= {
            "text" : utterance,
            "options" : {
                "alternate_intents": True,
                "debug": True,
                "return_context":True,
            }
        }
    ).get_result()

    assistant.delete_session(ASSISTANT_ID,session_id )

    print(json.dumps(json_output, indent= 2))
if __name__ == '__main__':
    main()