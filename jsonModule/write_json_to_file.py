"""
 Задание № 1
 Записать словарь в json-файл lib/payload.json
"""
from utils import definitions
import json

dictData = {"user": "churashevsa",
            "pan": 3214538756238,
            "is_employee": True,
            "phone": None,
            "groups_id": [234, 365, 987]}

with open(definitions.TMP_DIR / 'payload.json', 'w+') as f:
    json.dump(dictData, f, indent=4, sort_keys=True)

