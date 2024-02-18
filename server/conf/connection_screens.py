# -*- coding: utf-8 -*-
import random

"""
Connection screen

This is the text to show the user when they first connect to the game (before
they log in).

To change the login screen in this module, do one of the following:

- Define a function `connection_screen()`, taking no arguments. This will be
  called first and must return the full string to act as the connection screen.
  This can be used to produce more dynamic screens.
- Alternatively, define a string variable in the outermost scope of this module
  with the connection string that should be displayed. If more than one such
  variable is given, Evennia will pick one of them at random.

The commands available to the user when the connection screen is shown
are defined in evennia.default_cmds.UnloggedinCmdSet. The parsing and display
of the screen is done by the unlogged-in "look" command.

"""

from django.conf import settings

from evennia import utils

CONNECTION_SCREEN = """
|b==============================================================|n
 Welcome to |g{}|n, version {}!

 If you have an existing account, connect to it by typing:
      |wconnect <username> <password>|n
 If you need to create an account, type (without the <>'s):
      |wcreate <username> <password>|n

 If you have spaces in your username, enclose it in quotes.
 Enter |whelp|n for more info. |wlook|n will re-show this screen.
|b==============================================================|n""".format(
    settings.SERVERNAME, utils.get_evennia_version("short")
)

def connection_screen():
    quotes = [
        """
        \"The water, like our souls, is spent.\"
                                - Brother Gilak
        """,
        """
        "We have little room for error. Even the slightest 
        mistake could lead to thermonuclear winter."
                                                 - Cogworth
        """,
        """
        "They who run on two legs shall outrun they who run on one.
        They who run on four legs shall outrun those on two.
        They who have nitro boosted treads outrun all."
                                                  - Tanker Timm
        """,
        """
        "Foolishly, I have pursued vengeance when I should have sought
        death."
                                                             - Nergull    
        """,
        """
        "Blue skies have turned black, the rivers red. The earth is 
        dust and the air is poison. Hope hangs ever so loosely."
                                                      - Vizier Rabin
"""
    ]


    screen = """    


              _.-^^---....,,--       
          _--                  --_  
          <                        >)
          |                         | 
          \._                   _./  
              ```--. . , ; .--'''       
                    | |   |             
                .-=||  | |=-.   
                `-=#$%&%$#=-'   
                    | ;  :|     
          _____.,-#%&$@%#&#~,._____
        ###############################
        #   RETRO MUTANT APOCALYPSE   #
        ###############################

{}

        Connect to an existing: 
          |wconnect <username> <password>|n
        Create a new account:
          |wcreate <username> <password>|n
""".format(random.choice(quotes))
    return screen
