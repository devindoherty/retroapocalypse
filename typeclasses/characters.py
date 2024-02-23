"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import utils
from evennia.objects.objects import DefaultCharacter
from .objects import ObjectParent
import random

class Character(ObjectParent, DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_post_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the prelogout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    prelogout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """

    def at_object_creation(self):
        self.db.mind = random.randint(3, 20)
        self.db.body = random.randint(3, 20)
        self.db.soul = random.randint(3, 20)

        self.db.health = (self.db.body + random.randint(1, 10)) * 5
        self.db.stamina = (self.db.body + self.db.soul) * 5
        self.db.willpower = (self.db.mind + self.db.soul) * 5
    
    def get_stats(self):
        return self.db.mind, self.db.body, self.db.soul

    def increase_stat(self, stat, amount):
        self.stat += amount

class NPC(Character):
    """
    Class that extends Character to nonplayer characters.
    """
    def at_object_creation(self):
        self.db.dialogues = {
            "greeting": "Shade and water, friend.",
            "name": f"My name is {self.name}.",
        }
    
    def at_heard_say(self, message, from_obj):
        message = message.split('says, ')[1].strip(' "')
        if message in self.db.dialogues:
            return f"{self.db.dialogues[message]}"

        return f"{from_obj} said: '{message}'"
    
    def msg(self, text=None, from_obj=None, **kwargs):
        if from_obj != self:
            try:
                say_text, is_say = text[0], text[1]['type'] == 'say'
            except Exception:
                is_say = False
            if is_say:
                response = self.at_heard_say(say_text, from_obj)
                if response != None:
                   utils.delay(2, self.execute_cmd, f"say {response}")
        super().msg(text=text, from_obj=from_obj, **kwargs)