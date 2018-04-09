################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

init python:

    # Multi-game persitence data
    mp = MultiPersistent("barkpack.mp")

init:
    if not mp.journal:
        $ mp.journal = []

init -1 python:

    def addToJournal(item):
        if item not in mp.journal:
            mp.journal.append(item)

    ## Returns random dialog on each new game run.
    ## Though, technically it can be anything.
    ## Example: $ lalala = random_dialogue(["blablabla", "tatata", "lalala"])
    ## Based on https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=47341
    def random_dialogue(dialog_list):
        dialogue = renpy.random.choice(dialog_list)
        return dialogue

    ## Pauses the game for brief second.
    ## By defualt this is 1.0, although it can be changed.
    def delay(dur = 1.0):
        renpy.pause(dur)
