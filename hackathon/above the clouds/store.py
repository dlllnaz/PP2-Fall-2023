import pygame
from characters import *

class Store:
    def __init__(self):
        self.characters = {
            "character0": Character("Character Main", "./characters/ch0.png", 50),
            "character1": Character("Character 1", "./characters/ch1.png", 100),
            "character2": Character("Character 2", "./characters/ch2.png", 150),
            "character3": Character("Character 3", "./characters/ch3.png", 200),
            "character4": Character("Character 4", "./characters/ch4.png", 250),
            "character5": Character("Character 5", "./characters/ch5.png", 300),
            "character6": Character("Character 6", "./characters/ch6.png", 350),
            "character7": Character("Character 7", "./characters/ch7.png", 400),
            "character8": Character("Character 8", "./characters/ch8.png", 450),
            "character9": Character("Character 9", "./characters/ch9.png", 500),
            "character10": Character("Character 10", "./characters/ch10.png", 550),
            "character11": Character("Character 11", "./characters/ch11.png", 600),
            # Add more characters as needed
        }
        with open('./characters/purchased_ch.txt', 'r') as file:
            text = file.read().split("\n")
            self.purchased_characters = text[0].split(",")
            self.active_character = f"character{text[1]}" 
            self.active_characted_id = int(text[1])
        with open('./coins.txt', 'r') as f:                     
                self.collected_coins = int(f.read())
        for x in self.purchased_characters:
            self.characters.get(f"character{x.strip()}").is_unlocked = True

    def purchase_character(self, character_name):
        character = self.characters.get(character_name)
        if character and not character.is_unlocked and self.collected_coins >= character.price:
            character.is_unlocked = True
            self.collected_coins -= character.price
            text = ""
            with open('./characters/purchased_ch.txt', 'r') as file:
                text = file.read().split("\n")
            text[0]+=f", {character_name[9:]}"
            with open('./characters/purchased_ch.txt', 'w') as file:
                file.write("\n".join(text))
            with open('./coins.txt', 'w') as f:                     
                f.write(str(self.collected_coins))
            return True
        return False

    def set_active_character(self, character_name):
        if character_name in self.characters and self.characters[character_name].is_unlocked:
            self.active_character = character_name
            with open('./characters/purchased_ch.txt', 'r') as file:
                text = file.read().split("\n")
            text[1] = str(character_name[9:])
            with open('./characters/purchased_ch.txt', 'w') as file:
                file.write("\n".join(text))
            return True
        return False
