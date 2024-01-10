import json
import MetaTrader5 as mt5

class Bot:
    def __init__(self):
        self.settings = json.load(open("./settings/bot.json", "r"))
    


if __name__ == "__main__":
    bot = Bot()
    print(bot.settings["version"])
