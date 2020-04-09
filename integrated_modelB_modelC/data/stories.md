## help path Prediction Model B
* greet
  - utter_greet
* filler_sentence1_heating
  - action_utter_sentence_one
* filler_sentence2_music
  - action_utter_sentence_two
  
## Named Selection Model C
* named_selection{"appliance":"Oven"}
  - action_utter_response
  - slot{"appliance":"Oven"}
  
## List Selection Model C
* list_selection{"selection":"first one"}
  - action_utter_response_list
  - slot{"selection":"first one"}
  
## Cancel Interaction
* cancel_interaction
  - utter_cancel
  
## List Option
* list_option
  - utter_appliances_option

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
