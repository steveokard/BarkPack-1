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

    rc "Chump likes this town. Think a golf course would be good here, Jinksins?"
    jk "I'm just a butler."
    rc "Yes it does."
    rc "Maybe near the station by those active tracks?"
    aw "No!"
    zc "Wait!"
    aw "Huh?"
    zc "Why not over at the edge of town?"
    aw "What are you doing?"
    zc "You owe me a week of coffee."

    rc "Chump is listening."
    aw "Talking in third person won't get old at all..."
    zc "Yes! So much land for a wonderful golf course. Away from the loud noises."
    rc "Deal!"
    zc "What!?"
    jk "You get use to it."
    aw "Do I still owe that coffee?"
    zc "Only for the weekend."
    aw "Yes!"

    jk "A second has passed, sir."
    rc "What did I tell you kids? Just a second."
    aw "That was more like an half hour."
    rc "Billion dollars?"
    jk "Limo is outside, sir."
    rc "Goodbye, kids."

    & delay()
    zc "..."
    & delay()
    aw "..."
    & delay()
    zc "If he calls me \"kid\" one more ti-"
    aw "Goodbye!"

    & delay()
    ds "Now serving 100."

    jump scene3

label scene3:

    # show bg fairviewdmv

    "Two hours later"
    ds "Now serving 185"

    # show bg dmvwaitingroom

    aw "What are you doing?"
    zc "Giving an application one star."
    aw "Why?"
    zc "So I can give it a good review."
    aw "I- wha!?"

    # Anthony gets a beeping from his phone

    aw "..."
    zc "Is that Channel 45?"
    aw "Yup."
    zc "What do they need from you now?"
    aw "Gotta finish a story for them."
    zc "But what about the DMV?"
    ds "Now serving 189."
    zc "..."
    aw "I'm sure you'll manage."

    # show bg newsvan

    aw "Hey, Zen."
    zn "Hey, Anthony."
    zn "You're not normally here this quickly."
    aw "DMV."
    zn "Oh."
    aw "Shouldn't you be waiting?"

    # show bg dmvwaitingroom

    ds "Now calling 199."
    zc "I hate the DMV."

    # show bg newsvan

    zn "Oh."
    $ delay()
    zn "Wait, you did what!?"
    zn "Nevermind."
    aw "So what's up?"
    zn "We gotta finish our story on the generation gap."
    aw "Oh. That."
    aw "How long did Channel 45 give us?"

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
