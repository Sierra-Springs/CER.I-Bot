from msg_string_base import *
import re
import os
import sys
from pathlib import Path


source_root = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if source_root not in sys.path:
    sys.path.append(source_root)


keys_handled = []
with open(source_root / "LANG" / "msg_string_autogen_func.py", "w") as msg_string_autogen_func:
    msg_string_autogen_func.write("from msg_string_base import *\n\n")

    accolades_regex = re.compile(r'{(?:.*)}')
    mo = accolades_regex.search('hello {pomme} patate {frite}')
    print(mo.groups())

    for key in STRINGS_MSG:
        msg_string_autogen_func.write(f"def {key}():")
        msg_string_autogen_func.write("\treturn construct_string(locals())\n\n")

        keys_handled.append(key)




def MSG_TEST(salle):
    return construct_string(locals())


def MSG_THE_TIME_IS(heure, minute):
    return construct_string(locals())


def MSG_THE_WEATHER_IS(weather, temperature_integer, temperature_decimal):
    return construct_string(locals())


def MSG_INDICATE_ROOM_FOR_CLASS(salle):
    return construct_string(locals())


if __name__ == "__main__":
    print(MSG_THE_TIME_IS(heure="12", minute="30"))
    print(MSG_TEST("C104"))
    print(MSG_THE_WEATHER_IS("Clear", 4, 52))

    accolades_regex = re.compile(r'{(?:.*)}')
    mo = accolades_regex.search('hello {pomme} patate {frite}')
    print(mo.groups())
