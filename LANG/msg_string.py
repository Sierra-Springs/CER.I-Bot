import re
import os
import sys
from pathlib import Path


source_root = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if source_root not in sys.path:
    sys.path.append(source_root)

from LANG.msg_string_base import *

keys_handled = []
with open(source_root / "LANG" / "msg_string_autogen_func.py", "w") as msg_string_autogen_func:
    msg_string_autogen_func.write("from LANG.msg_string_base import *\n\n\n")

    for key in STRINGS_MSG:
        for strings_lang in [STRINGS_MSG, STRING_MSG_ROLLBACK]:
            if key in strings_lang.keys():
                strings = strings_lang[key]
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

        arguments = ", ".join(placeholders)

        msg_string_autogen_func.write(f"def {key}({arguments}):\n")
        msg_string_autogen_func.write("    return construct_string(locals())\n\n\n")

        keys_handled.append(key)


from LANG.msg_string_autogen_func import *


if __name__ == "__main__":
    pass  # Do nothing anyway just to autogenerate the msg_string_autogen_func.py file when launching this module alone
    print(MSG_THE_TIME_IS(heure="12", minute="30"))
    print(MSG_TEST("C104"))
    print(MSG_THE_WEATHER_IS("Clear", 4, 52))