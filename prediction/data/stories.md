## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## help path
* greet
  - utter_greet
* filler_sentence1_heating
  - utter_filler_ans1
* filler_sentence2_music
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

## predict_location
* identify_location
  - utter_identify_location

## interactive_story_1
* greet
    - utter_greet
* filler_sentence1_heating{"filler": "hmmmm"}
    - utter_filler_ans1
* filler_sentence1_heating{"filler": "ehh"}
    - utter_filler_ans1
* filler_sentence1_heating{"filler": "hmmmm"}
    - utter_filler_ans1
* filler_sentence1_heating{"filler": "haaaa"}
    - utter_filler_ans1
    - utter_goodbye

## interactive_story_1
* filler_sentence2_music{"verb": "turn on", "splitpoint": "my"}
    - utter_filler_ans2
* filler_sentence2_music{"verb": "turn on", "splitpoint": "my"}
    - utter_filler_ans2

## interactive_story_1
* identify_location{"verb": "Turn down", "noun": "heat", "splitpoint": "the"}
    - utter_identify_location
* identify_location{"verb": "Turn up", "noun": "heat", "splitpoint": "the"}
    - utter_identify_location
* identify_location{"verb": "Turn up", "noun": "heat", "splitpoint": "the"}
    - utter_identify_location
* identify_location{"verb": "Turn down", "noun": "heat", "splitpoint": "the"}
    - utter_identify_location
* noun

## interactive_story_1
* filler_sentence1_heating{"verb": "increase", "splitpoint": "the"}
    - utter_filler_ans1
* filler_sentence1_heating{"verb": "Decrease", "splitpoint": "the"}
    - utter_filler_ans1
* filler_sentence1_heating{"verb": "decrease", "splitpoint": "the"}
    - utter_filler_ans1
* filler_sentence1_heating{"verb": "Decrease", "filler": "mmmm"}
    - utter_filler_ans1
* filler_sentence1_heating{"filler": "mmmm"}
    - utter_filler_ans1
* filler_sentence1_heating{"filler": "mmmm"}
    - utter_filler_ans1
* filler_sentence1_heating{"verb": "Increase", "splitpoint": "the"}

## interactive_story_1
* filler_sentence3_lights{"verb": "Switch on", "splitpoint": "the"}
    - utter_filler_ans3
* filler_sentence3_lights{"splitpoint": "the", "location": "living room"}
    - utter_filler_ans3
* filler_sentence3_lights{"splitpoint": "the", "filler": "mmmm"}
    - utter_filler_ans3
* filler_sentence3_lights{"splitpoint": "the", "filler": "mmmm"}
    - utter_filler_ans3
* filler_sentence2_music{"verb": "Start", "splitpoint": "the"}
    - utter_filler_ans2
