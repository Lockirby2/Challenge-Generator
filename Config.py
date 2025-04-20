import random

class Config(object):
    def __init__(self, yaml_config): # Initialize the restriction
        if yaml_config.get("ask_for_input"):
            self.game = input("What game do you want to generate a challenge for? ")
            self.max_restrictions = int(input("What is the maximum number of restrictions that you want? "))
            self.target_difficulty = int(input("What is the difficulty that you're aiming for? "))
            print("")
            
        else:
            self.game = yaml_config.get("game")
            self.max_restrictions = yaml_config.get("max_restrictions")
            self.target_difficulty = yaml_config.get("target_difficulty")
            
        self.mandate_limiting = random.random() < yaml_config.get("limiting_chance") / 100