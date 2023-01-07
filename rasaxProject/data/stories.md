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

## Bloom generation
* ask_bloom_generation
  - utter_ask_start_of_sentence
* start_of_sentence
  - action_bloom

## Weather
* ask_weather
  - action_weather

## Ask presentation
* presentation
    - action_presentation
    - utter_ask_ifNeedHelp

## fonctionnalities
* fonctionnalities
  - action_fonctionnalite

## Presentation_deny
* presentation
  - action_presentation
  - action_fonctionnalite
  - utter_ask_ifNeedHelp
* deny
  - utter_goodbye

## happy path 1
* greet
  - utter_greet
  - action_presentation

## demande wiki
 * demande_wikipedia 
   - action_wiki

## demande gpt
 * ask_gpt
   - action_gpt3