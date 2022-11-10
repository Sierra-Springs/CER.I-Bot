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

## schedule
* greet
  - utter_greet
* ask_schedule
  - utter_ask_section
* give_section
  - utter_ask_group
* give_major
  - utter_ask_major
* give_group
  - utter_resume
  - action_schedule
  - utter_goodbye

## Ask Time
* ask_time
  - action_time
