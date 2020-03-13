from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet


class CompletionForm(FormAction):

    def name(self) -> Text:
        """Unique identifier of the form"""
        
        return "completion_form"
        
## 1- slot mapping: check for: noun, verb, split point
## 2- validate values of noun, verb, split point
## 3- match sentence with completion


    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
##        return ["noun", "verb", "splitpoint"]
        return ["verb", "splitpoint"]

    def slot_mappings(self) -> Dict[Text, Any]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
##            "noun": self.from_entity(entity="noun", intent=["affirm", "deny"),
            "verb": self.from_entity(entity="verb", intent="incomplete"),
            "splitpoint": self.from_entity(entity="splitpoint", intent="incomplete"),
        }
        
        

  
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
      ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        ##dispatcher.utter_message(template="utter_submit")
        return []
    
    
    
class CompletionModel(Action):

     def name(self) -> Text:
     
         return "completion_model"
         
         
     def run(self, dispatcher, tracker, domain):
     
         verb = tracker.get_slot('verb')
         
         ##dispatcher.utter_message(template="utter_complete")
         
         ##print(verb)
         
         return[SlotSet("noun", "light")]
       