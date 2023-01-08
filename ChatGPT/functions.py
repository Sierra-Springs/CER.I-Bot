from implementations import *
import json

def weather(city):
    """
    city : ville dans laquelle ont veux connaitre la météo
    Exemple de retour :
    {'coord': {'lon': 4.8333, 'lat': 44.0833},
     'weather': [{'id': 804, 'main': 'Clouds', 'description': 'couvert', 'icon': '04n'}], 'base': 'stations',
     'main': {'temp': 12.48, 'feels_like': 11.77, 'temp_min': 11.29, 'temp_max': 12.73, 'pressure': 1018,
              'humidity': 76}, 'visibility': 10000, 'wind': {'speed': 5.14, 'deg': 120}, 'clouds': {'all': 100},
     'dt': 1673124523, 'sys': {'type': 1, 'id': 6516, 'country': 'FR', 'sunrise': 1673075717, 'sunset': 1673108269},
     'timezone': 3600, 'id': 3035679, 'name': 'Avignon', 'cod': 200}
     """

    return i_weather(city)

def action(societe, pays):
	"""
	retourne le cours de la bourse pour la societe indiquée dans le pays choisi
	"""
	return get_cours(societe, pays)

