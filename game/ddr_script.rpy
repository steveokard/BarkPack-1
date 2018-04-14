################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

## The bases behind the DDR scenes is to provide some level of interactivity
## during the course of the story while also getting a peek into their musical
## interests. The songs they're good at echos their musical tastes.

define zc_ddr_win = ["Haha, I won!", "I just love this song."]
define aw_ddr_win = ["Booya!", "It's my favorite song."]
define zc_ddr_loss = ["Almost had it."]
define aw_ddr_loss = ["Next time I'll get it."]

init python:

    zc_win_dialog = random_dialogue(zc_ddr_win)
    aw_win_dialog = random_dialogue(aw_ddr_win)
    zc_loss_dialog = random_dialogue(zc_ddr_loss)
    aw_loss_dialog = random_dialogue(aw_ddr_loss)

label ddr_scene1:

    aw "[aw_loss_dialog]"
    zc "[zc_win_dialog]"

    # $ journal_entry("Zack found out Anthony liked .")

    jump scene3

label ddr_scene2:

    zc "[zc_loss_dialog]"
    aw "[aw_win_dialog]"

    # $ journal_entry("Anthony found out Zack liked .")

    jump scene3

label ddr_scene3:

    aw "[aw_loss_dialog]"
    zc "[zc_win_dialog]"

    # $ journal_entry("Zack found out Anthony liked .")

    jump scene3

label ddr_scene4:

    zc "[zc_loss_dialog]"
    aw "[aw_win_dialog]"

    # $ journal_entry("Anthony found out Zack liked .")

    jump scene3
