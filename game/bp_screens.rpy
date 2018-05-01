################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

## Scenes screen ##########################################################
##
## A scene selection screen for jumping between varies parts of the visual novel
## This will be "Extra Life" later on for newer Anthony & Zack stories
screen scenes():

    tag menu

    use game_menu(_("Extra Life"), scroll="viewport"):

        style_prefix "extralife"

        vbox:

            text _("More stories from Anthony & Zack.")

            # Tutorial("tutorial_playing", _("Player Experience"))
            textbutton _("#666") action Start()
            textbutton _("Kit meets Winter") action Start("scene2")
            textbutton _("Channel 45") action Start("scene3")
