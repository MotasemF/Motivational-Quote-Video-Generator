import random
import json

class RandomQuote:
    def __init__(self) -> None:
        pass

    def get(self) -> None:
        json_file = json.load(open("quotes.json", encoding="utf8"))
        rand_index = random.randint(0, len(json_file))
        return json_file[rand_index]["text"]