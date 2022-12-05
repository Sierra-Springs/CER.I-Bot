import importlib
import inspect

module_base = "LANG."

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


def MSG_MISSING_KEY(key_name, example):
    return construct_string(key_name, inspect.stack()[1][3], example)


def MSG_MODEL_LOADED_SUCCESSFULLY(model_name):
    return construct_string(model_name)


def MSG_MODEL_LOAD_ERROR(model_name):
    return construct_string(model_name)


def MSG_PREDICTION_ATTEMPT_ON_NONE_MODEL():
    return construct_string()


def MSG_LOG_LANG_CHANGED_SUCCESSFULLY(lang_name):
    return construct_string(lang_name)


def MSG_LOG_LANG_CHANGE_ERROR(lang_name):
    return construct_string(lang_name)


def MSG_MSG_LANG_CHANGED_SUCCESSFULLY(lang_name):
    return construct_string(lang_name)


def MSG_MSG_LANG_CHANGE_ERROR(lang_name):
    return construct_string(lang_name)


def MSG_MSG_LOCAL_LANG_CHANGE_ERROR(lang_name):
    return construct_string(lang_name)


def MSG_NO_NEW_DATA_AVAILABLE():
    return construct_string()


def MSG_NEW_DATA_DOWNLOADED(last_game_time):
    return construct_string(last_game_time)


def MSG_PREDICTION_RECEIVED():
    return construct_string()


def MSG_PREDICTION_IMPOSSIBLE(model_name):
    return construct_string(model_name)


def MSG_GAME_TIME_RESET():
    return construct_string()


def MSG_NO_NEW_PREDICTION():
    return construct_string()


def MSG_LAST_GAME_TIME_IS(last_game_time):
    return construct_string(last_game_time)


def MSG_WAIT_FOR_THE_DOWNLOAD(wait_time_with_unit):
    return construct_string(wait_time_with_unit)

def W_MODEL_IS():
    return construct_string()

def W_WORKSPACE_IS():
    return construct_string()

def W_VALUES_ARE():
    return construct_string()

def W_CLICK_ME():
    return construct_string()

def W_LANG():
    return construct_string()

def W_DOWNLOAD_MODEL():
    return construct_string()

def W_PREDICT():
    return construct_string()

def W_LOAD_DATA():
    return construct_string()

def W_RESET():
    return construct_string()

def W_CHANGE_LANG():
    return construct_string()

def MSG_THE_TIME_IS(time):
    return construct_string()


if __name__ == "__main__":
    print(MSG_MISSING_KEY("hello", "hi"))