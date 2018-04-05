# Prologue.
################################################################################
label start:

    if yes_no == "n":
        $ plyr_name = renpy.input("Okay, we can try again. Leave blank for defualt.")
    else:
        plyr_dad "Hooray!"
        $ delay()
        plyr_dad "It's a she!?"
        plyr_dad "Or is it a he?"
        $ delay()
        plyr_mom "I don't know."
        doc "They're a male everywhere but their genitals."
        $ delay()
        plyr_dad "... Interesting."
        plyr_mom "Should we give them a male name?"
        doc "It's up to you, but I'd stick with male."
        $ plyr_name = renpy.input("Type in a name, or leave it blank for \"[plyr_name]\".")

    $ plyr_name = plyr_name.strip()

    python: # Fallback
        if plyr_name == "" or yes_no == "":
            plyr_name = default_name

    $ yes_no = renpy.input("Do you wish to stay with \"[plyr_name]\"? Type in \"y\", \"n\" or leave blank to continue.")
    $ yes_no = yes_no.strip()

    if yes_no == "y":
        plyr_mom "We'll call you [plyr_name]."
        jump chap1
    elif yes_no == "n":
        jump start
    else:
        plyr_mom "We'll call you [plyr_name]."
        jump chap1

# Story begins here.
################################################################################
label chap1:

    $ delay()
    "15 years later."

    # At a baseball game

    $ delay()
    "My name is [plyr_name]. And this is my friend Zack."
    "We've known each other since kindergarten."
    "Our parents like to send us to baseball games together."
    "I wasn't into baseball but I didn't mind joining my"
    "family as long as they let me play my tablet games."

    player "Mom, I forgot my hat."

    "But it wasn't always ideal."

    zack "Have you ever been to Poke Cola Stadium?"
    player "Poke. Cola. Stadium?"
    zack "..."
    zack "Long story."
    player "No."
    zack "Netheir have I."
    player "Why do you ask?"
    zack "I always wanted to go there."
    player "I'll put it on my bucket list."

    "I was watching a live feed of G4. The Screen Savers was on right now with Attack of the Show up next. I was waiting for X-Play."

    zack "Is that G4?"
    player "Yup."
    zack "I thought they shutdown."
    player "Someone brought the rights for an untold amount before it went off the air. I'm so excited!"
    zack "Huh..."

    "I wasn't that interested in traditional sports, like Baseball."
    "I preferred eSports. Rocket Leauge, an vehicular soccer game, was more of my cup of tea. G4 would simulcast various eSports tourments on weekdays."

    zack "Have they ever figured what \"G4\" stands for?"
    player "I always thought it meant \"Group of 4\"?"
    zack "Like a four player game?"
    player "I think so."

    jump chap2

label chap2:

    "Later, we went back to Zack's house after the game."

    player "Hey, Mom can I sleep over at Zack's tonight?"
    plyr_mom "If it's fine with his mother. I see no reason why not to."
    zack "Yay!"

    "After our parents agreed to let us stay over Zack and I began to settle down."

    zack "Check out all these baseball cards I have."
    player "Wow! You're quite a collector."
    zack "It's just a hobby."

    "Zack and I checked out all the cool cards he had collected over the years."

    zack "So what's on G4 right now?"
    player "Cinematech. Then a Counter Strike tourment from UCCleague tonight."
    zack "Isn't Cinematech your favorite show?"
    player "Yeah. However, I spend sometime with you for once."

    "Zack paused with a blush."

    $ delay()
    zack "Hey, [plyr_name]?"
    player "Yeah?"
    zack "I know you like to listen to music. And I was thinking..."
    player "Hm?"

    "Zack got out a nackle with a cassette around it."

    player "For me?"
    zack "Yeah!"
    player "Thank you so much."

    "I decided to wrap the necklace around me immediately. In return, I gave him my blue on black hat."

    zack "Really?"
    player "Yeah!"
    zack "Thank you so much!"

    "Zack wore the hat immediately as I did."
    "Afterwards, we hugged each other really tight."

    "5 years later."
    $ delay()
    "Present day."

    return
