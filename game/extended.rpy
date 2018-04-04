############################################################
## Extends the functionality of Ren'Py
## or provides wrappers around existing
## Ren'Py functions
############################################################

init 1 python:
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
