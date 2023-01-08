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



if __name__ == '__main__':
    input("prompt: ")
    print("Pour répondre à votre question, j'ai besoin de savoir")
    print("dans quelle ville vous souhaitez connaître la météo.")
    print("Pourriez-vous me fournir cette information s'il vous")
    print("plaît ?")

    input("prompt: ")
    print("Il fait nuageux avec un peu de soleil à Avignon.")
    print("La température actuelle est de 14.01°C, mais elle")
    print(" peut varier entre 13.57°C et 14.66°C aujourd'hui.")
    print(" Le taux d'humidité est de 78% et la vitesse du vent")
    print(" est de 4.12 km/h.")

