# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import requests
import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_customer_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url='http://127.0.0.1:8080/api/voice/gen_route'
        data={'phone_number':tracker.get_slot('phone_number')}
        response = requests.post(url, data=json.dumps(data)).json()
        if response:
            name=response.get('name')
            dispatcher.utter_message(text="Hello {}!".format(name))
        else :
            dispatcher.utter_message(text="Hello New User!")
        return []
