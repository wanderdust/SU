## Prediction Model B
* named_activity{"activity":"turn on"}
  - action_utter_activity
  - slot{"activity":"turn on"}

## help path Prediction Model B
* greet
  - utter_greet
* filler_sentence1_heating
  - utter_filler_ans1
* filler_sentence2_music
  - utter_filler_ans2
  
## Named Selection Model C
* named_selection{"appliance":"Oven"}
  - action_utter_response
  - slot{"appliance":"Oven"}
  
## Cancel Interaction
* cancel_interaction
  - utter_cancel
  
## List Selection
* list_selection{"option":"first one"}
  - utter_appliances_option
  
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
