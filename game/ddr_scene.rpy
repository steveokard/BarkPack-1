################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

## The bases behind the DDR scenes is to provide some level of interactivity
## during the course of the story while also getting a peek into their musical
## interests. The songs they're good at echos their musical tastes.

define zack_ddr_win = ["Haha, I won!"]
define anthony_ddr_win = ["Booya!"]
define zack_ddr_loss = [""]
define anthony_ddr_loss = [""]

init python:

    zack_win_dialog = random_dialogue(zack_ddr_win)
    anthony_win_dialog = random_dialogue(anthony_ddr_win)
    zack_loss_dialog = random_dialogue(zack_ddr_loss)
    anthony_loss_dialog = random_dialogue(anthony_ddr_loss)

label ddr_scene1:

    zack "[zack_win_dialog]"
    anthony "[anthony_loss_dialog]"

    jump scene3

label ddr_scene2:

    anthony "[anthony_win_dialog]"
    zack "[zack_loss_dialog]"

    jump scene3

label ddr_scene3:

    zack "[zack_win_dialog]"
    anthony "[anthony_loss_dialog]"

    jump scene3
