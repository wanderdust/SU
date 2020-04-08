# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionUtterResponse(Action):

    def name(self) -> Text:
        return "action_utter_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        appliance = tracker.get_slot("appliance")
        activity = tracker.get_slot("activity")
        dispatcher.utter_message(text="Okay. I will {} the {} for you!".format(activity, appliance))

        return [SlotSet("appliance", appliance)]

class ActionUtterActivity(Action):

    def name(self) -> Text:
        return "action_utter_activity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        activity = tracker.get_slot("activity")
        dispatcher.utter_message(text="Which appliance should i {} for you? (Named Selection)".format(activity))

        return [SlotSet("activity", activity)]
