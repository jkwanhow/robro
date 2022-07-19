import random

class Choice:
    def __init__(self):
        self.choices = []

    def show_current(self):
        if not self.choices:
            return f"Choices list is empty []"
        return f"choices are currently: {','.join(self.choices)}"

    def add(self, option):
        self.choices.append(option)
        return f"{option} added to list, current list is {','.join(self.choices)}"
        

    def remove(self, option):
        if not self.choices:
            return f"cannot remove from empty lists"
        if option not in self.choices:
            return f"{option} was not found in the current list, you can add it with: \"-chooser add {option}\""
        self.choices.remove(option)
        return f"Removed {option} current list is now {','.join(self.choices)}"

    def pick(self):
        if not self.choices:
            return "No items to choose from please add items."

        outcome = random.choice(self.choices)
        return f"I Chungi pick {outcome}"

    def about(self, o):
        if o == "add":
            return f"Please don't use empty strings\nto add choices to the list simply type: `-chooser add *item_name*` "
        elif o == "remove":
            return f"Please don't use empty strings\nto remove choices from list simply type: `-chooser remove *item_name*` "