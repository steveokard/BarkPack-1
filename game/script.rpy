################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

label start:

    # show bg fairviewdmv
    show zack
    zc "So why are we here?"
    hide zack
    show anthony
    aw "License renewal."
    show zack at right
    zc "Think it'll will take long?"
    aw "It shouldn't take but a fe-"
    $ delay()
    hide anthony
    hide zack

    # show bg dmvslothes
    show anthony
    aw "-w minutes."
    show zack at left
    zc "..."
    zc "Anthony?"
    hide anthony
    hide zack

    # show bg dmvcheckin
    show zack
    zc "So?"
    hide zack
    show sloth
    ds "Now serving 12."
    hide sloth
    show anthony
    aw "We're number 666."
    hide anthony
    show zack
    zc "Why do I get the feeling it'll be a long day?"
    hide zack

    jump scene2

label scene2:

    # show bg woodviewloop
    show kit
    kw "Hey, Winter Green, where's Zack and Anthony?"
    hide kit
    show winter
    wg "I think they were going to the DMV today."
    $ delay()
    show kit
    kw "What!?"
    hide kit
    show winter
    wg "You're welcome to spend sometime here."
    hide winter
    show kit
    kw "Sure."
    hide kit

    # show bg wglivingroom
    show kit
    kw "..."
    hide kit
    show winter
    wg "..."
    hide kit
    show kit
    kw "So what have you been doing lately?"
    hide kit
    show winter
    wg "Working on a new program."
    show kit at left
    kw "For the two love birds at the DMV?"
    hide kit
    show winter
    wg "You really think they're in love?"
    show kit
    kw "Just a hunch."
    kw "So what's the program?"
    show winter at right
    wg "Come. I'll show you."
    hide kit
    hide winter

    # show bg wgbedroom
    wg "I'm working on a vector graphics editor. I've been making in my spare time."
    kw "You made that in your spare time?"
    wg "Yeah. I'm studying a new programming language, called Spark."
    kw "Zack did tell me you were a programmer."
    wg "Interested in learning?"
    kw "Nah. That stuff is way beyond my realm of understanding."
    wg "Speaking of, I don't think we've formally met."
    kw "I'm more of a loner, to be honest."
    wg "How did you come to know Zack?"
    kw "Anthony."
    hide kit
    hide winter

    # show pic kitanthonymeet1
    "We see each other everyday in the morning and evenings."

    # show pic kitanthonymeet2
    "Then we bumped into each other at the supermarket one day."

    # show bg wgbedroom
    show winter at right
    wg "Cool."
    show kit
    kw "Yeah. Rest is history, of course."
    hide kit
    hide winter

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
    aw "And,"
    extend " 3..."
    extend " 2..."
    extend " 1..."
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
    zn "Really? Should show me now."
    aw "I'll have to check to see if I have anything saved."

    jump scene4

label scene4:

    # show bg wgbedroom
    kw "I noticed you have a lot of electronics lying around."
    wg "Oh yeah. I've been tinkering in it lately."
    kw "Is there anything you don't do?"
    wg "I can't drive."
    hide winter
    hide kit

    # show bg wggarage
    kw "What do all of these do?"
    ## The design of the transmitter is based on the one from Sims 3: University life
    wg "Anthony wanted to see if I could make a radio transmitter."
    # show bg wgradio
    wg "It transmits to AM and FM."
    kw "And it works?"
    wg "Haven't tested it yet."
    kw "I wonder what it's range is."
    wg "Wanna try it out?"
    kw "Sure!"

    # show bg wgoutsidegarage
    wg "Tuning in."
    $ kfbroad = "This is Kit broadcasting live from Fairview."
    kw "[kfbroad]"
    "Radio" "[kfbroad]"
    wg "It works!"
    kw "Sweet!"

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

    $ delay()
    zc "..."
    $ delay()
    aw "..."
    $ delay()
    zc "If he calls me \"kid\" one more ti-"
    aw "Goodbye!"

    return
