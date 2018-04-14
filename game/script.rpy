################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

label start:

    # show bg fairviewfield

    zc "Have you ever been to Icy Blaze Park?"
    aw "Icy Blaze Park? No."
    zc "Netheir have I."
    aw "Why do you ask?"
    zc "I always wanted to go there."
    aw "I'll put it on my bucket list."

    # $ journal_entry("Anthony Wilcox adds Icy Blaze Park to his bucket list.")

    "I was watching a live feed of G3. The Screen Savers was on right now with Attack of the Show up next. I was waiting for X-Play."

    # show bg g3screensavers

    kc "Stay tuned. The Screen Savers will be right back!"

    $ delay()

    # show bg fairviewfield

    zc "Is that G3?"
    aw "Yup."
    zc "I thought they went under."
    aw "Nope someone brought them for a lot of money."
    zc "Huh..."

    "I wasn't that interested in traditional sports, like Baseball."
    "I preferred eSports. Rocket Leauge, an vehicular soccer game, was more of my cup of tea. G3 would simulcast various eSports tourments on weekdays."

    # show bg baseballflyover

    aw "Zack! Zack!"
    zc "I see it! I see it!"

    $ delay()

    zc "..."
    aw "..."
    zc "And there it goes."

    jump scene2

label scene2:

    # show bg zackhouse

    "Later, we went back to zc's house after the game."

    # show bg zackroom

    zc "Check out all these baseball cards I have."
    aw "Wow! You're quite a collector."
    zc "It's just a hobby."

    "Zack and I checked out all the cool cards he had collected over the years."

    zc "So what's on G3 right now?"
    aw "Cinematech. Then a Counter Strike tourment from UCCleague tonight."
    zc "Isn't Cinematech your favorite show?"
    aw "Yeah. However, I can let it pass for you."

    "Zack paused with a blush."

    $ delay()

    zc "Hey, aw?"
    aw "Yeah?"
    zc "I know you like to listen to music. And I was thinking..."
    aw "Hm?"

    # show bg cassetteneckplace

    "Zack got out a necklace with a cassette around it."

    zc "I made this."
    aw "I like it."
    zc "Do you want?"
    aw "Really?"
    zc "Yeah. I know how much you like music."
    aw "Thank you!"

    $ journal_entry("Zack Casey hands aw his cassette necklace.")

    # show bg wrapnecklace

    $ delay()

    aw "You know what?"
    zc "What?"
    aw "Have my hat."
    zc "..."

    $ delay()

    zc "But, I."
    aw "You like hats. No? Keep it."

    # $ journal_entry("Anthony Wilcox hands zc his blue on black hat.")

    # show bg sleepoverhug

    jump scene3

label scene3:

    # show bg andrewshouse

    aw "Up for some DDR?"

    menu:
        "Play DDR song 1":
            jump ddr_scene1

        "Play DDR song 2":
            jump ddr_scene2

        "Play DDR song 3":
            jump ddr_scene3

        "Play DDR song 4":
            jump ddr_scene4
        "Skip":
            $ ddr_skip = True
            zc "Maybe next time."
            aw "Okay."

    if ddr_skip is False:
        zc "Good game."
        aw "Maybe we can play another time?"
        zc "Yeah!"

    jump scene4

label scene4:

    # show bg anthonysroom

    zc "Is it possible for you to get pregnant?"
    aw "Wait, wha!?"
    aw "... Uh."

    $ delay()

    aw "I don't know. Never tried to do {b}it{/b} before."
    zc "You're a-?"
    aw "Yes."

    # $ journal_entry("Zack Casey discovered aw is a virgin.")

    zc "Why not?"
    aw ""

    return
