from pyChatGPT import ChatGPT
from implementations import *
from functions import *
import time

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..VTk7jzQGAMyrFWZm.lTKPlmKHkxybx2OhFr5eIJY_dowbu0h0Ow9619evs-srdD6RnzrSSifuRZsWVqnBHKiQ1Ao5dYZgrEHskxKd9EvFd-xTmL7bvdk5IMtNKBLtmYRaN8xMGkSFmqVMUXv6fQnByYPf2IhiPj4-yT08_t5zI2UIteYlKm2wF_5aKxSxRP_K6YVFO5PinnpvIRAQNaZ4KG2FL0S4zGjW7VR8WUzLf6Gs-jNHQaOcb3V-IIr5mV05cwPXEreeOnTNTTyYdhIgaGxcTWEd6Y3VyUbWz0KPzBXqSMayHB1B_BtYFzJESwzyoeDIgtmuP_9JH2th5V83NNKUDhMOJiAMCytOJYTDFgwSaMzhL0qrHBzkQ48rmwb9qotyeTbmEtBxVwJjLR7k23qBG11XSPCfoCGNRI911xX1355cUORY0RfjHFUvY6u6iTz6IlH9aWBM253mc90sBMMpKf0ZYtw7rS1Lzpj0DalgC9Fcsu90Mg96yCVXerKIkyy6pbGrhZmCjGvo7oK0d29yPYNrC0sjsvv9I17RvrSIF7POa8hVUEb_1hh1YRPk_cS_ND4oyQ3X689ZGnd00bN6TlSLBeLV-zTGZmEkGnnxJblaD5hyUD7H4QM719Na_AvxikYcZIk0hRBUOsXYfM2RhY0_8aek0XxMrQ41ybR8gEm3lowvffbq-Xz_evarxMnOJxOmnoDdvBaHCb87jGT0gePiQ5oMe52D3JFJy-9S2xlKGjgTpQPKD9EA8-3P1OodKY_PgBaDlHnDxX-J-QoWwLYPt9tODNSqgMXrdGaYWrjGylT1zLgiIdb_IVvy0EOeV6toYvLY4Sp2t-F0uFiLrvAfWIQfUwmCuqlmPc08hZEjEH9ise_W-duajpW8iWUMsPLjxVfWhZohxfV5f1j2sIdC8dpcDi7Zdh6ahxoAZLPavPZ-l4HROY-d5ZG6VJ07YEStBQceTFdaDQLYNQpyrUJRd9oYRIbiS17LCXVRQk9AtOusEWxH16P1uLMGoS75pODrRiOVrsnhLkEufyNZF8H0rDBX3eGBuKtXcOdoNftEKrQuR9YhR6nIfYwpPLwqiLTsZz66_fpz7BdqWLRfjIt_3SEoNDnOV6ZwqwvopxzTsQIYLOR9WWOqO0HN_pAwIsdh1QmxbqTLS8_O5gxsgCuw_d5qnpqR4ZGC2W4f_dsiiSPs4bBo-GIBwZp5W-P3ElifVq3Tp835kNOnzYqi4x_9thwFhLSMzdYZAGl0xhuj_k8DqqCxsgOZgAs8aXayvjGUVQUdENib21JHm8pTw4lhMhZ58azi9KELZ7LQMtW9Nm4k6wRJ6Ar-zAqOrOOrchK1JsiIExz1JcxgAg_hoGkp5BegioYZi6bbEeiXGa5StUZvDfmgOI1X6mrpmAo-i-RiUd6O88_RZWo7tvuM2WhRslZDYtzjDIgosQXag9Sf_HfElyUC0YEpsgYamLkQZF6GHoP3Z8C1O0XewOdHaXax1ZRA2ru1ma3iccdvpcjYZ3J_O-aG5auTbkPDHKahcddyKcRrjeDCxflRNjPrQ2kcsBpp5oOPieC-XPhdDSAfWoQC1ma6v1kG1wCN_A0XFaZJRjm8CDWr4amaVy-R0sRLR8k33ln5sxARH1PCdK6IrxJgsfKV1DrNurAX0C3UMWwNxbV1uq-gyJi-8m3AzXOit3uhWJRrRW2jXIYObXcHvLtRmztYZKBd2IHgi6Q0oM7ENY6WTrb6yKQ7j3q-E86WBAVMS_f5hIs-97AVxHHaC7lyFelXgI7z7f7e-w07nF4w4b-PJV2H5rW8n_2Q-pLyLWkYAyqLASsDDuZsqO9gLQGJWjRCqxJHArpTCW7t6zH0dg2SjXrY8-kiJl6FuwBt2sW8xTzPkVytJ6d7tzo6OHn0XKgihnslI7HiClzG3opUcz0TaglUWnemio-LRBGhrd6UBeJ8N-W2p3I8EX-Cb3wrUiDrR9A5XNtya--VZVIAnhna-XLkxEGFCk8CowAMo8cM8VkSN7x60vkBxfxRrWENw-BBUtE6ZPHhvQFiiDyDGxT7ECt2r31_QU6h8TawStb6_ksscWUs8YeGzQ_pklSklROCDkvXtU32tEZTtNvBegHq1GtEThll3grTAWqwibxEGYlFU6j7dj5vhRgLZn2fdAZNiX4IW51LWeCE86U6iEEaCITeH27NDZRJ0bwjIyn1bbvbSPi_7HQQRvynbAcwEBI1u1BTXkHtwKckRQ8-KxanFNUHn9CzFzuTmL4ISfgTs1Yoyl3GbpWb32hrZs96ljPL3wvlyvQHvdJwcsbQoG9AKncFBQEvzUSqSg.lATATRnTC7iHPOQIu9sMzA'
api = ChatGPT(session_token)  # auth with session token

import re

def get_code_blocks(text):
    # Utilise l'expression régulière "```.*?```" pour trouver tous les blocs de code
    # La partie ".*?" signifie "n'importe quel caractère, zéro ou plusieurs fois, de manière non greedy"
    # Cela signifie que l'expression régulière s'arrêtera au premier ``` trouvé, plutôt que d'aller jusqu'au dernier
    code_blocks = re.findall("```.*?```", text, re.DOTALL)
    # Supprime les marqueurs de code du début et de la fin de chaque bloc de code
    return [block[4:-4] for block in code_blocks]

def gen_first_prompt(question):
    with open("functions.py", "r") as func_file:
        funcs = func_file.readlines()
        funcs = "\n".join(funcs)

    string = "Imagine que tu as accès à ces fonctions:\n"
    string += funcs
    string += "\n"
    string += question
    string += "\n Ne parles pas de ce que je viens de te dire. Ne parles pas des fonctions. Réponds comme d'habitude mais si besoin tu peux procéder ainsi:"
    string += "\nSi il manque des informations, poses les questions nécessaires pour les récupérer. Tu peux aussi te servir des autres fonctions pour les trouver. Comporte toi comme un assistant virtuel. Une fois toutes les informations fournies, si besoin, produit un code python en un seul bloc qui réponds à la question au format JSON en utilisant les fonctions données. la fonction main() fini par return json.dumps(answer). Fait des réponses courtes. Ne donne pas de code tant que tu n'as pas toute les informations nécessaires"

    return string


from bs4 import BeautifulSoup
import requests


# Fonction qui récupère le code Python dans le code HTML
def get_python_code(html):
    # Utilise BeautifulSoup pour parser le code HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Recherche la balise "pre" qui contient le code Python
    pre_tag = soup.find('pre')

    # Récupère le contenu de la balise "pre"
    code = pre_tag.text
    code = code.replace("Copy code", "")

    return code


def main():
    print("La fonction main n'as pas été override")

if __name__ == '__main__':
    first_prompt = True

    while 1:
        prompt = input("prompt: ")
        if first_prompt:
            prompt = gen_first_prompt(prompt)
            first_prompt = False
        resp = api.send_message(prompt)
        if re.search("```", resp['message']):
            code = get_python_code(resp["html"])
            """print(resp["html"])
            print("_" * 10, code)
            print(get_python_code(resp["html"]))
            print("_" * 10, code)"""

            exec(code)
            reponse = main()

            answer_prompt = "Voici la réponse de l'API:\n"
            answer_prompt += reponse.__str__()
            answer_prompt += "\n Réponds à la question avec ces informations."

            time.sleep(0.1)
            resp = api.send_message(answer_prompt)
            print(resp['message'])
        else:
            print(resp['message'])



    api.reset_conversation()  # reset the conversation
    api.clear_conversations()  # clear all conversations
    api.refresh_chat_page()  # refresh the chat page