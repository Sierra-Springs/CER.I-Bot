import importlib
import inspect

module_base = "LANG.MSG."

LANG_MSG_SOURCE = 'LANG_MSG_FRA'
LANG_MSG_SOURCE_ROLLBACK = 'LANG_MSG_ANG'

# Charge Les string pour les messages dans la langue choisie.
# Si la langue choisie n'est pas du tout disponible, charge la langue par défaut
try:
    STRINGS_MSG = importlib.import_module(module_base + LANG_MSG_SOURCE).STRINGS_MSG
except:
    STRINGS_MSG = importlib.import_module(module_base + LANG_MSG_SOURCE_ROLLBACK).STRINGS_MSG


# Charge la langue par défaut pour les strings qui n'existent pas dans la langue choisie.
STRING_MSG_ROLLBACK = importlib.import_module(module_base + LANG_MSG_SOURCE_ROLLBACK).STRINGS_MSG


def launch_msg_lang(lang_source):
    """
    Permet de changer la langue
    :param lang_source: Nom de la langue source. exemple: 'LANG_MSG_FRA'
    """
    global LANG_MSG_SOURCE, STRINGS_MSG
    LANG_MSG_SOURCE = lang_source
    STRINGS_MSG = importlib.import_module(module_base + lang_source).STRINGS_MSG


def get_lang_msg_source():
    """
    :return: nom de la langue source sélectionnée
    """
    return LANG_MSG_SOURCE


def construct_string(*kwargs):
    """
    Récupère la string du dictionnaire correspondant au nom de la méthode appelante.
    Complète les placeholder avec les paramètres passés à la fonction et retourne la string construite.
    """
    try:
        # Si la string requise est disponible dans la langue choisie
        return STRINGS_MSG[inspect.stack()[1][3]].format(*kwargs)
    except:
        # Si la string requise n'est pas disponible dans la langue choisie
        return STRING_MSG_ROLLBACK[inspect.stack()[1][3]].format(*kwargs)


def MSG_THE_TIME_IS(time):
    return construct_string(time)


if __name__ == "__main__":
    print(MSG_THE_TIME_IS("12:30"))