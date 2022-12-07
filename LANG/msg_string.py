import importlib
import inspect
import random

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
    Récupère les strings du dictionnaire correspondant au nom de la méthode appelante.
    Selectionne aléatoirement une string si plusieurs sont disponibles dans une liste
    Complète les placeholder avec les paramètres passés à la fonction et retourne la string construite.
    """
    try:
        # Si la string requise est disponible dans la langue choisie
        strings = STRINGS_MSG[inspect.stack()[1][3]]  # strings disponibles pour le message
        if isinstance(strings, list.__class__):
            string_index = random.randint(0, len(strings) - 1)  # index de la string choisie
            selected_string = strings[string_index]
        else:
            selected_string = strings
        return selected_string.format(*kwargs)
    except:
        # Si la string requise n'est pas disponible dans la langue choisie
        strings = STRING_MSG_ROLLBACK[inspect.stack()[1][3]]  # strings disponibles pour le message
        if isinstance(strings, list.__class__):
            string_index = random.randint(0, len(strings) - 1)  # index de la string choisie
            selected_string = strings[string_index]
        else:
            selected_string = strings
        return selected_string.format(*kwargs)


def MSG_THE_TIME_IS(time):
    return construct_string(time)


def MSG_TEST():
    return construct_string()

if __name__ == "__main__":
    print(MSG_THE_TIME_IS("12:30"))
    print(MSG_TEST())