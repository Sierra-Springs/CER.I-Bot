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
    msg_string_autogen_func.write("from msg_string_base import *\n\n\n")

    for key in STRINGS_MSG:
        print("_" * 30)
        print(key)
        strings = STRINGS_MSG[key]
        placeholders = []

        if isinstance(strings, list):
            for string in strings:
                for placeholder in re.findall('\{(.*?)\}', string):
                    if not placeholder in placeholders:
                        placeholders.append(placeholder)
        else:
            for placeholder in re.findall('\{(.*?)\}', strings):
                if not placeholder in placeholders:
                    placeholders.append(placeholder)

        print(placeholders)
        arguments = ", ".join(placeholders)

        msg_string_autogen_func.write(f"def {key}({arguments}):\n")
        msg_string_autogen_func.write("    return construct_string(locals())\n\n\n")

        keys_handled.append(key)


from msg_string_autogen_func import *


if __name__ == "__main__":
    print(MSG_THE_TIME_IS(heure="12", minute="30"))
    print(MSG_TEST("C104"))
    print(MSG_THE_WEATHER_IS("Clear", 4, 52))
    print(MSG_TA_MERE(couleur="blue", forme="square"))
