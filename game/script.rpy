################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

label start:

    # show bg fairviewdmv

    zc "So why are we here?"
    aw "Mom wants to see something about her car."
    zc "Think it'll will take long?"
    aw "It shouldn't take but a fe-"

    $ delay()
    # show bg dmvslothes

    aw "-w minutes."
    zc "..."
    zc "Anthony?"

    # show bg dmvcheckin

    zc "So?"
    ds "Now serving 12."
    aw "We're number 666."
    zc "Why do I get the feeling it'll be a long day?"

    jump scene2

label scene2:

    # show bg dmvwaitingroom

    "An hour later"
    ds "Now serving 45."
    zc "This is gonna take forever."

    rc "Scuse me. A billion dollars walking through."
    aw "And who are you?"
    rc "Ronald Chump. Billionare."
    zc "We got the latter part already."
    rc "Myself and I are coming to renew my license."

    zc "Then get in line like the rest of us."
    rc "Of course. Jinkins, fetch my papers while I wait in line with these kids."
    jk "Yes, sir."
    aw "We're in our 20s."
    rc "Ronald will only be in line only for a second."
    zc "He only tells the truth by accident, folks."

    jk "We're done."
    rc "Now drive Chump back home."
    jk "Yes, sir."

    & delay()
    zc "..."
    & delay()
    aw "..."
    & delay()
    zc "So what's on G3TV, Anthony?"
    aw "Um, well..."

    & delay()
    ds "Now serving 100."

    jump scene3

label scene3:

    ds "Now serving 185"

    jump scene4

label ddrscene3:

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
