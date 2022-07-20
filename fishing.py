from datetime import datetime, timedelta
import random
import json

class FishingGame:
    def __init__(self):
        MAX_RARITY = 10
        f = open("fishes.json")
        fishes = json.load(f)
        f.close()
        self.ocean = []
        f = open("players.json")
        self.players = json.load(f)
        f.close()
        for fish in fishes:
            count = MAX_RARITY + 1
            for i in range(count - fish['rarity']):
                self.ocean.append(fish)
        

    def generate_fish(self):
        fish = random.choice(self.ocean)
        return fish

    def get_player(self, user):
        if not user in self.players.keys():
            self.players[user] = {"fish": [], "money": 0, "CD": "new"}
        return self.players[user]

    def catch(self, user):
        datetime_format = "%d/%m/%Y %H:%M:%S"
        player = self.get_player(user)
        now = datetime.now()
        if (player["CD"]!= "new"):
            stored_time = datetime.strptime(player["CD"], datetime_format)
            if (stored_time > now):
                min_remaining = (stored_time - now).total_seconds()/60
                return f"{user} can fish again in {int(min_remaining)} minutes"

        catch_number = random.randint(0, 5)
        player["CD"] = datetime.strftime(now + timedelta(minutes=30), datetime_format)
        if catch_number == 0:
            return "You caught no fish"
        fish = self.generate_fish()
        name = fish["name"]
        weight = random.uniform(fish["min_size"], fish["max_size"])
        photo = fish["picture"]
        player["fish"].append({"name": name, "weight": weight})
        with open('players.json', 'w') as f:
            json.dump(self.players, f, indent = 4)
        f.close()
        return f"{photo}\nYou caught a {name} it weighs {weight}Kg"

    def players_fish(self, user):
        player = self.get_player(user)
        fishes = player["fish"]
        if not fishes:
            return f"{user} has no fish, lol"
        message = f"{user} has:\n"
        for fish in fishes:
            name = fish["name"]
            weight = fish["weight"]
            message += f"{name}, {weight}Kg\n"
        return message
