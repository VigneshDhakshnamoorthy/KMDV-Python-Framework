import json
import os


class JsonUtil:

    def __init__(self, file_name):
        try:
            with open(f"../Repository/DataRepository/{file_name}.json", 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            with open(f"{os.getcwd()}/Repository/DataRepository/{file_name}.json", 'r') as f:
                self.data = json.load(f)

    def get_test_data(self, text):
        arr = []
        for k, v in self.data.items():
            if text.lower() in k.lower():
                if v['RunMode'].lower() == "y":
                    for li in v['Test Cases']:
                        if list(li.values())[0].lower() == 'y':
                            arr.append(list(li.values()))
        return arr
