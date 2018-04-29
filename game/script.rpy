################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

label start:

    # show bg fairviewdmv
    zc "So why are we here?"
    aw "License renewal."
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

    # show bg woodviewloop
    kw "Hey, Winter Green, where's Zack and Anthony?"
    wg "I think they were going to the DMV today."
    kw "What!?"
    wg "You're welcome to spend sometime here."
    kw "Sure."

    # show bg wglivingroom
    kw "..."
    wg "..."
    kw "So what have you been doing lately?"
    wg "Working on a new program."
    kw "For the two love birds at the DMV?"
    wh "You really think they're in love?"
    kw "Just a hunch."
    kw "So what's the program?"
    wg "Come. I'll show you."

    # show bg wgbedroom
    wg "It's a little calculator I've been making in my spare time."
    kw "Seems a litte basic, don't ya' think?"
    wg "I'm studying a new programming language, called Spark."
    kw "Zack did tell me you were a programmer."
    wg "Interested in learning?"
    kw "Nah. That stuff is way beyond my realm of understanding."
    wg "Speaking of, I don't think we've formally met."
    kw "I'm more of a loner, to be honest."
    wg "How did you come to know Zack?"
    kw "Anthony."

    # show pic kitanthonymeet1
    "We see each other everyday in the morning and evenings."

    # show pic kitanthonymeet2
    "Then we bumped into each other at the supermarket one day."

    # show bg wgbedroom
    wg "Cool."
    kw "Yeah. Rest is history, of course."

    jump scene3

label scene3:

    # show bg fairviewdmv
    ds "Now serving 356"

    # show bg dmvwaitingroom
    aw "What are you doing?"
    zc "Giving an application one star."
    aw "Why?"
    zc "So I can give it a good review."
    aw "What!? That makes no sense."

    # show bg ketotvunit
    zc "Anthony."
    aw "What?"
    zc "Channel 45 is here."
    zc "Is that Zenon?"
    aw "Yes it is."

    # show bg dmvwaitingroom
    zn "What are you two doing here?"
    zc "License renewal."
    zn "Well, I've been looking for Anthony everywhere."
    aw "I thought I had the day off."
    zn "You do."
    aw "So what are you are?"
    zn "News story going on around this area."
    zc "You go on. I'll be watching G3TV in the meantime."

    # show bg ketotvunit
    zn "We're doing a news story on the bank that got robbed on the otherside here."
    aw "I know this is my break but it's not like we're doing anything back at the DMV."
    zn "You'd be willing to help?"
    aw "As long as I'm not in the front of the camera this time."

    # show bg fairviewbank
    aw "And 3... 2... 1..."
    dn "We now return to Zenon Tigerpaw with an update to the robbery."
    zn "Thanks, Deanna. The cops were able to take down the crimial before he could hurt any hostages."
    dn "Any word on the motives?"
    zn "No, Deanna. He did go on about \"new world order\" after he was arrested."
    dn "Thanks, Zenon."
    "This is KETO-TV, Channel 45."

    # show bg ketotvunit
    aw "And, that's a wrap."
    zn "Not bad director work, little fen."
    aw "Thanks. Zack and I made a lot of home movies in the past."
    zn "Really? Should me now."
    aw "I'll have to check to see if I have any saved."

    return

# Save Trump paraody for last
label scene100:

    # show bg dmvwaitingroom
    ds "Now serving 245."
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

    return
