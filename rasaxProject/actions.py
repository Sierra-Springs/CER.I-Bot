# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from db_sqlite import select_data
import datetime
import requests
import os
import sys


source_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if source_root not in sys.path:
    sys.path.append(source_root)

from LANG.msg_string import *


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionSchedule(Action):

     def name(self) -> Text:
         return "action_schedule"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#           dispatcher.utter_message(text="Your next schedule is Math in room S2")

           print(select_data(tracker.get_slot("section"),tracker.get_slot("group")))
           text="Your next schedule is {}".format(select_data(tracker.get_slot("section"), tracker.get_slot("group")))
           dispatcher.utter_message(text)
	
           return []

class ActionTime(Action):

     def name(self) -> Text:
         return "action_time"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
           now = datetime.datetime.now()
           heure = now.strftime("%H")
           minute = now.strftime("%M")
           dispatcher.utter_message(text=MSG_THE_TIME_IS(heure=heure, minute=minute))

           return []


class ActionPresentation(Action):

    def name(self) -> Text:
        return "action_presentation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Bonjour, je suis le robot Pepper" )
        return []

class ActionFonctionnalite(Action):

    def name(self) -> Text:
        return "action_fonctionnalite"

    def run(self, dispatcher: CollectingDispatcher,
      tracker: Tracker,
      domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        fonctionnalities = ["je peux me présenter",
                            "Je donne La Méteo",
                            "l'heure",
                            " et Je raconte une Histoire"]
        answer = "Voici la liste de mes fonctionnalitées, "
        for funct in fonctionnalities :
            answer += funct + ", "
        dispatcher.utter_message(answer)
        return []


class GPT3Client:
    def __init__(self, ip: str = "10.126.4.216", port: int = 8080):
        self.base_url = f"http://{ip}:{port}"

    def request_text(self, prompt):
        res = requests.post(url=self.base_url + "/generate",
                            json={'prompt': prompt})
        print(res.json()["text"])


class ActionGPT(Action):

    def name(self) -> Text:
        return "action_gpt3"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sc = GPT3Client()
        answer = sc.request_text(prompt="Raconte moi une blague")

        dispatcher.utter_message(answer)
        return []


class ActionBloom(Action):

    def name(self) -> Text:
        return "action_bloom"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        API_TOKEN = os.environ["BLOOM_API_KEY"]

        API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        print("--------------------------------------------")
        print(tracker.get_slot("start_of_sentence_entity"))
        print("--------------------------------------------")
        output = query({
            "inputs": tracker.get_slot("start_of_sentence_entity"),
        })

        print(output)
        try:
            dispatcher.utter_message(text=output[0]['generated_text'])
        except:
            dispatcher.utter_message(text=output['error'])

        return []


class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # city = tracker.get_slot('city')
        city = "Avignon"

        API_KEY = "30b769c3babdac103e4dfef554b32115"
        API_URL = "http://api.openweathermap.org/data/2.5/weather?"

        # API_GGL = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=fr&dt=t&q="

        URL = API_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric" + "&lang=fr"
        print(URL)

        def query():
            # response = requests.post(API_URL, headers=headers, json=payload)
            response = requests.get(URL)
            return response.json()

        output = query()
        print(output)

        # def translate(weather):
        #     trad = requests.get(API_GGL + weather)
        #     return trad.json()

        temp_integer_decimal = str(output['main']['temp']).split(".")
        try:
            response = MSG_THE_WEATHER_IS(weather=output['weather'][0]['description'],
                                          temperature_integer=temp_integer_decimal[0],
                                          temperature_decimal=temp_integer_decimal[1])
            # trad = translate("The weather is " + "Rain")
            # print(trad)
        except:
            response = "Error code : {} -> {}".format(output['cod'], output['message'])

        dispatcher.utter_message(text=response)

        return []

#################################utils
from typing import Any, Text, Dict, List, cast
import wikipedia
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def to_html(text):
    html = '<div>{0}</div>'
    html = html.format( text.replace("\n", "<br/>").replace("\\n", "<br/>") )
    return html
def custom_response_message(text, html):

    try:
        f = open("../projet_monrobotparlant/NaoRasaASRProject/html/index.html", "w")
        f.write(html)
        f.close()
    except:
        print("Warning ---> Pas pu créer la page web")

    return "{0}".format(text)
    # return "{0}$$$$${1}".format(text,html)


class ActionWiki(Action):
    def name(self) -> Text:
        return "action_wiki"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        terme_cle = tracker.get_slot("demande_wiki")
        print(terme_cle)
        try:
            current_state = tracker.current_state()
            latest_message = current_state["latest_message"]["text"]
            wikipedia.set_lang("fr")
            data = wikipedia.summary(terme_cle, sentences=2)
            # pageWeb = wikipedia.page(terme_cle).url
            # print(pageWeb)


        except wikipedia.exceptions.PageError:
            data = "Aucune correspondace n'a été trouvé. Veillez réessayer!"

        html = to_html("<div class='joke'>{0}</div>".format(data))
        print(custom_response_message(data, html))
        dispatcher.utter_message(custom_response_message(data, html))

        return []


if __name__ == '__main__':
    now = datetime.datetime.now()
    print(MSG_THE_TIME_IS(heure=now.strftime("%H"),
                          minute=now.strftime("%M")))
    #print(os.environ["BLOOM_API_KEY"])





