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


class ActionUtterSentenceOne(Action):

    def name(self) -> Text:
        return "action_utter_sentence_one"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Do you mean Heating? or Do you mean Music?")

        return [SlotSet("appliance1", "Heating"), SlotSet("appliance2", "Music")]

class ActionUtterSentenceTwo(Action):

    def name(self) -> Text:
        return "action_utter_sentence_two"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Do you mean Music? Do you mean TV? or Do you mean Heating?")

        return [SlotSet("appliance1", "Music"), SlotSet("appliance2", "TV"), SlotSet("appliance3", "Heating")]


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

class ActionUtterResponseList(Action):

    def name(self) -> Text:
        return "action_utter_response_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        selection = tracker.get_slot("selection")

        global appliance

        if selection == "first one":
            appliance = tracker.get_slot("appliance1")
        elif selection == "second one":
            appliance = tracker.get_slot("appliance2")
        elif selection == "third one":
            appliance = tracker.get_slot("appliance3")

        activity = tracker.get_slot("activity")
        dispatcher.utter_message(text="Okay. I will {} the {} for you!".format(activity, appliance))

        return [SlotSet("appliance", appliance)]

