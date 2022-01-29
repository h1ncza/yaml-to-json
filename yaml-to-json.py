#!/usr/bin/env python
#Simple python script to convert yaml to json

import sys, yaml, json
from emoji import emojize as em
from colorama import Fore, Style

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('usage: yaml-to-json.py <yaml> <output.json>')
    sys.exit()

targetYaml = sys.argv[1]

if (len(sys.argv) == 2):
    with open(targetYaml, "r") as stream:
        try:
            json.dump(yaml.load(stream, Loader=yaml.SafeLoader), sys.stdout, indent=4)
        except yaml.YAMLError as exc:
            print(exc)
elif (len(sys.argv) == 3):
    outputJson = sys.argv[2]
    if outputJson.endswith(".json"):
            outputJson = outputJson
    else:
            outputJson = outputJson + ".json"
    with open(targetYaml, "r") as stream, open(outputJson, "w") as toFile:
        try:
            json.dump(yaml.load(stream, Loader=yaml.FullLoader), toFile, indent=4)
        except yaml.YAMLError as exc:
            print(exc)

    print(Fore.BLUE, em(":outbox_tray: :page_with_curl:"), targetYaml, Fore.MAGENTA, em(":inbox_tray: :scroll:"), outputJson, em(":floppy_disk:"), Style.RESET_ALL)
