## happy path
* greet
 - utter_greet


## complete utterance
* incomplete
 - completion_form
 - form{"name": "completion_form"}
 - form{"name": null}
 - utter_slots_values
 - completion_model
 - utter_complete

* thankyou
 - utter_noworries
 

## say goodbye
* goodbye
  - utter_goodbye

## interactive_story_1
##* greet
##    - utter_greet
##* incomplete
##    - completion_form
##    - utter_slots_values
##* incomplete{"verb": "turn on", "splitpoint": "my"}
##    - completion_form
##    - utter_slots_values
##* incomplete
##    - completion_form
##    - utter_slots_values
