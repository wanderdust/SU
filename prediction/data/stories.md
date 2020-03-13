## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## help path
* greet
  - utter_greet
* filler_sentence1
  - utter_filler_ans1

## help path
  * greet
    - utter_greet
  * filler_sentence2_music{"splitpoint": "my"}
    - utter_filler_ans2
  * filler_sentence2_music{"splitpoint": "the"}
    - utter_filler_ans2
  * filler_sentence2_music{"splitpoint": "a"}
    - utter_filler_ans2

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
* filler_sentence1{"filler": "hmmmm"}
    - utter_filler_ans1
* filler_sentence1{"filler": "ehh"}
    - utter_filler_ans1
* filler_sentence1{"filler": "hmmmm"}
    - utter_filler_ans1
* filler_sentence1{"filler": "haaaa"}
    - utter_filler_ans1
    - utter_goodbye
