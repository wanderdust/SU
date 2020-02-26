## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## help path
* greet
  - utter_greet
* filler_sentence
  - utter_filler_ans

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

## interactive_story_1
* greet
    - utter_greet
* filler_sentence{"filler": "hmmmm"}
    - utter_filler_ans
* filler_sentence{"filler": "ehh"}
    - utter_filler_ans
* filler_sentence{"filler": "hmmmm"}
    - utter_filler_ans
* filler_sentence{"filler": "haaaa"}
    - utter_filler_ans
    - utter_goodbye
