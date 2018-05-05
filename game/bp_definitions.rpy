################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

## Characters ##################################################################
# Bark Pack
define aw = Character(_("Anthony Wilcox"))
define zc = Character(_("Zack Casey"))
define kw = Character(_("Kit Welsh"))
# Recurring
define sc = Character(_("Saveli Cornell"))
define ry = Character(_("Rolan Yamamoto")) # Saveli's robot
# Channel 45
define zt = Character(_("Zenon Tigerpaw"))
define ea = Character(_("Evan Aries"))
define dn = Character(_("Deanna Nash"))
# Universe
define ds = Character(_("DMV Sloth")) # Filler name
define ec =  Character(_("Ed Colton"))
define ms =  Character(_("Melody Swan"))
define wg = Character(_("Winter Green"))
define jk = Character(_("Jinkins")) # Reusable character, think Nurse Joy
define kc = Character(_("Kevin Clover")) # G3TV, Screen Savers
define sl = Character(_("Samantha Lane")) # G3TV, Screen Savers
define rc = Character(_("Ronald Chump")) # Trump paraody, not president

## Constants ###################################################################
default image_dir = "images"
default music_dir = "music"
default bp_license = _("The binaries and source code of this program have been made available to you under the Mozilla Public License 2.0 (MPL).")

## Variables ###################################################################
define awpack = False
define barkings = False
define triedall = False

## Images ######################################################################
# Characters
image zack = "[image_dir]/zack.png"
image anthony = "[image_dir]/anthony.png"
image zenon = "[image_dir]/zenon.png"
image winter = "[image_dir]/winter.png"
image kit = "[image_dir]/kit.png"
image sloth = "[image_dir]/sloth.png"
# Backgrounds
image bg sixam = "[image_dir]/sixam_splash.png"
image bg outside fairviewdmv = "[image_dir]/outsidefairviewdmv.png"

## Soundtrack ##################################################################
define theme_song = "[music_dir]/theme.ogg"
