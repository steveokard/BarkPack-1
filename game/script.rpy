################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

label start:

    # show pic fairviewfield

    zack "Have you ever been to Icy Blaze Park?"
    anthony "Icy Blaze Park? No."
    zack "Netheir have I."
    anthony "Why do you ask?"
    zack "I always wanted to go there."
    anthony "I'll put it on my bucket list."

    $ addToJournal("Anthony adds Icy Blaze Park to his bucket list.")

    "I was watching a live feed of G3. The Screen Savers was on right now with Attack of the Show up next. I was waiting for X-Play."

    zack "Is that G3?"
    anthony "Yup."

    "I wasn't that interested in traditional sports, like Baseball."
    "I preferred eSports. Rocket Leauge, an vehicular soccer game, was more of my cup of tea. G3 would simulcast various eSports tourments on weekdays."

    # show pic baseballflyover

    anthony "Zack! Zack!"
    zack "I see it! I see it!"

    $ delay()

    zack "..."
    anthony "..."
    zack "And there it goes."

    jump scene2

label scene2:

    # show pic zackhouse

    "Later, we went back to Zack's house after the game."

    # show pic zackbedroom

    anthony "Hey, Mom can I sleep over at Zack's tonight?"
    mom "If it's fine with his mother. I see no reason why not to."
    zack "Yay!"

    "After our parents agreed to let us stay over Zack and I began to settle down."

    zack "Check out all these baseball cards I have."
    anthony "Wow! You're quite a collector."
    zack "It's just a hobby."

    "Zack and I checked out all the cool cards he had collected over the years."

    zack "So what's on G3 right now?"
    anthony "Cinematech. Then a Counter Strike tourment from UCCleague tonight."
    zack "Isn't Cinematech your favorite show?"
    anthony "Yeah. However, I can let it pass for you."

    "Zack paused with a blush."

    $ delay()

    zack "Hey, Anthony?"
    anthony "Yeah?"
    zack "I know you like to listen to music. And I was thinking..."
    anthony "Hm?"

    # show pic cassetteneckplace

    "Zack got out a necklace with a cassette around it."

    zack "I made this."
    anthony "I like it."
    zack "Do you want?"
    anthony "Really?"
    zack "Yeah. I know how much you like music."
    anthony "Thank you!"

    $ addToJournal("Zack hands Anthony his cassette necklace.")

    # show pic wrapnecklace

    $ delay()

    anthony "You know what?"
    zack "What?"
    anthony "Have my hat."
    zack "..."

    $ delay()

    zack "But, I."
    anthony "You like hats. No? Keep it."

    $ addToJournal("Anthony hands Zack his blue on black hat.")

    # show pic sleepoverhug

    jump scene3

label scene3:

    anthony "Up for some DDR?"
    zack "Sure!"

    menu:
        "Play DDR song 1":
            jump ddr_scene1

        "Play DDR song 2":
            jump ddr_scene2

        "Play DDR song 3":
            jump ddr_scene3

        "Play DDR song 4":
            jump ddr_scene4

    zack "Good game."
    anthony "Maybe we can play another time?"
    zack "Yeah!"

    jump scene4

label scene4:

    # show pic downtownfairview

    zack "Is it possible for you to get pregnant?"
    anthony "Wait, wha!?"

    menu:
        "I don't know.":
            anthony "I don't know. Kinda difficult to find out."

    # $ addToJournal("Zack discovered out ")

    return
