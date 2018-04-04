# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define plyr_name = ""
define anthony = Character('[plyr_name]') # Defualt: Anthony Wilcox
define zack = Character("Zack Casey")

label start:

    # Parse in the bracket in the next that the game will display to promt
    # The player to enter the name they've choosen
    $ plyr_name = renpy.input("What's your name? Leave blank for defualt.")
    $ plyr_name = plyr_name.strip()

    python:
        if plyr_name == "":
            plyr_name = "Anthony Wilcox"

    "Zack and I have been freinds since we were children."
    "Our parents use to send us to baseball games together."
    "I wasn't into baseball but I didn't mind joining my"
    "family as long as they let me play my tablet games."

    anthony "I forgot my hat."

    "But it wasn't always ideal."

    zack "Have you ever been to Poke Cola Stadium?"
    anthony "Poke. Cola. Stadium?"
    zack "..."
    zack "Long story."
    anthony "No."
    zack "Netheir have I."
    anthony "Why do you ask?"
    zack "I always wanted to go there."
    anthony "I'll put it on my bucket list."

    "I was watching a live feed of G4TechTV. The Screen Savers"
    "was on right now with Attack of the Show up next."

    zack "Is that G4?"
    anthony "Yup."
    zack "I thought they ceased operations."
    anthony "Someone brought the rights for an untold amounts."
    zack "Huh..."

    "I wasn't that interested in traditional sports, like Baseball."
    "I preferred eSports. Rocket Leauge, an vehicular soccer video game, was more of my cup of tea."

    return
