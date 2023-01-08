from pyChatGPT import ChatGPT
from implementations import *
from functions import *
import time

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..LtlctUtTtjG5mlYA.8QZK-0WzoVHSthRPyxJgldLYfa31bYnsNxVaIoiltEZ_LnQbvfTOj9zifK28OKvMEOtAdk0HDV-HshWfDyIIPyH3vAul4u-dF16H83eJPTN_QrEPqjv6fg_E95zcYKT1o36gufDn1K09i_80AbUVGhksCCx9hpPX903nVTlXbmsuBGgkxYz60BYKRTXDczzSfG9Gc9r9PclbxsPDAZNNp1fDTgae-a45tpSxPTZT-tBxWyacR27KbEbMUdeeJYcL-LPkGaYNJ44xvKVcOk2XvMVNPiuV4-a_tQB0Bj1DeA_D6f9Rqvg5FkMRqtfeOUSBIG2pluhxCHbnGY-4b0yYLll6PzslXm4zfsaLzzo2m7aftwUpEcXa1JXWq6BvcdNxRDUOqlip6vhyUdupxK8ue_tPWbY3GuHRtZj15iF4d2pvoDVaybMF9bqxudMypi-OvPyvRufVJJ-bRr1YaJCuDbhXg6oAV0sQa9-rw8ZI6EEzZ8EDalQOW8tIAPdcKhYzAC9wls2-EcM52cGPhvdSuc5O_rwFTcP2H3fYaV-gZavK8vrpHsg_posEDVZQxQjjth0oI_02s-oJ17_ztn-7QdCSOLTQBiPERXt0CMT6ks--LlOgj7IQ958JC6T-Wxxriu2pCnN1rlyRYL8NFccUv_vEVlqPdlLGL6DdPu9ENiS40whZnYwFpCoILYGKP2eVBnG2XBBiIg2BITDOj6VWDrZFSjkBu_U2v3HZ-3O76xSQc0gCWwFxR0i2T8Ugqs4kosPffzRMAj5V2T_KLeNoF88clZcoUOiaFqKkjmsFSfVtsvY0yvS5IYJbrKv783yvwAnZ-6JKV9WhUPPXBZSudXWn4govpzhN5fkmDP0Jnd-Jth29zQW-7NmfSQU-tdgaqZYgONV9_bPqwNPZPt4iBbksmocoMkf7u3VwR-0YQ5XHrVY3g0XXCavyc_a8_d9Myo7sMeW8x5cOUvxdRN-T6Wpi6MrmkemSBSFngqLX6FEjQobCnGj-NvRPFkr0WyZKJyuZsi-LSj-rlsRKuryq86_UcXnJVMRTz2agI_lqxV1pFM0CR99hX37BYMzp4a-J49UdUW_MfDzHM99jrITCbAT_R2ltfcs20HI2EmNWv7_ZCC8EYD8fnj5tDni3Q8O1QtGJuKccnLiSXBBDBHH0WtXAyHDdCyYXVJ6gydjRSQg7F5goNf-izTQn5_FVWF8168Z3UkbyfKfKCL_V8bzxyPw_UJYUIJ-lwEIG_1mfB5lQEIph0k4Yji5C_sDDvI9jQAjtQZ3hpRukVUvj1KXyQEfzp9qaWy5AoixiA5p1O-asFmyie4snskxg6qHh1zzvjksF8JNvPiaXh5VM3831z6PqvAWHvC3-Y0do_wY4deuG29KH4tqHw_5GC2rS-Pi1ZIBhp7qK1il5nmg81i9oEiuLQFl0pjtBPxYZGYe1_d1tSVChwCi3UpKe2Nnsc3Hl5vAKtd68BtazFpsav1d_PAjKtPrsicbPGuulsTmxxxoPk1loMf12yTVo5T31gZwQosORWyYYQPtVwnS65dio6p-3nP3D985lqvvyj0dGRTPmxB8s1neW_71TDMRjKqIcGA_slYTK7XMXoTvmZci-IbQ8_z4HF4bfn50XKytFY-I3GaiGn4D1rh-rK6MeICkzRrayjSgEbi9yG71Odaw-CM4laOeigyty-UHmT1s1po5O1b4CFN05FukdbQV4YUNi3IiGiRwG-aLZAMbvKe2nURnVBqLvdo3-_zTmjmiTqtqGSaEj8G1nnS0Mwfy_6R0_leX_hb0J43UESL2VCofMfKLyG4nTlVxNqIJYLQq2AOe1FZs8-c5G6snrgDmPQDkQEbg3T11j4ThpMWUxwSB_cX24oC_fC_0V8igfuKT_WqWp06qSZCnkq1kVOEc78ZCgLZHq6C9ads-jqYaQYbk4alPewY2QPOrEIzc-bx6paORStHj5c1S8_EvZSYd6BqvnXYXKIw5XlUi1YGZAkpiUUUXXf0EO3O1SPPahLuadk7jahzu7c50R1YLMm1B9iR1wgUWKSQDr7o9OwAvW81HW1aDroBaW0Oz6AtHhiYu343w4IMODb2gWnYjTnrmWckOja71fIO_h6lzUu5LrLlbsJADj1gXJTPAN6e5qBNBsO7eQ2w8O3bX_DkNgUzHjahrGJOg4JJ31jN0XvucpdLxPnCYR2pChaDkwPA25Tdh2cLydozmqzVsqjr-TbyFr1cPndPciRiftwRE5R1E-Ffd_3gvkRo2OTvXA2SjAmJYKIljEPacTJuqYr7tIYJGZBotkMM73QTCpBA.d2TXIJUIPbNSafF95WFTZg'
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
    #string += "\n Comporte toi comme un assistant virtuel et n'explique pas comment tu procède. réponds de façon naturelle."
    string += "\n Si il manque des informations, poses les questions nécessaires pour les récupérer. Tu peux aussi te servir des autres fonctions pour les trouver. Comporte toi comme un assistant virtuel. Une fois toutes les informations fournies, si besoin, produit un code python en un seul bloc qui réponds à la question au format JSON en utilisant les fonctions données. la fonction main() fini par return json.dumps(answer). Fait des réponses courtes. Ne donne pas de code tant que tu n'as pas toute les informations nécessaires"

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