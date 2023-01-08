import requests


def i_weather(city):
    API_KEY = "30b769c3babdac103e4dfef554b32115"
    API_URL = "http://api.openweathermap.org/data/2.5/weather?"

    URL = API_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric" + "&lang=fr"

    def query():
        # response = requests.post(API_URL, headers=headers, json=payload)
        response = requests.get(URL)
        return response.json()
    output = query()
    #print(output)

    return output


def get_cours(societe, pays):
    pass


def get_ville(couleur: str):
    ville = {"rouge": "Avignon", "bleu": "Paris"}
    return ville[couleur.lower()]


