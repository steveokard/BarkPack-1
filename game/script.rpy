################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

label start:

    show bg sixam
    $ delay()
    hide bg sixam
    # show bg fairviewdmv
    show zack
    zc "So why are we here?"
    hide zack
    show anthony
    aw "License renewal. Expires soon."
    show zack at right
    zc "Think it'll take long?"
    aw "It shouldn't take but a few-"
    $ delay()
    hide anthony
    hide zack

    # show bg dmvslothes
    show anthony
    aw "minutes."
    show zack at left
    zc "..."
    $ delay()
    zc "Anthony?"
    hide anthony
    hide zack

    # show bg dmvcheckin
    show sloth
    ds "Now serving 12."
    hide sloth
    show anthony
    aw "We're number 666."
    hide anthony
    show zack
    zc "Why do I get the feeling this will be a long day?"
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
    kw "Oh? What is it?"
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

    # show bg kitawfb1
    "We saw each other everyday in the morning and evenings."

    # show bg kitawfb2
    "Then we bumped into each other at the supermarket one day."

    # show bg kitzackfb
    "He introduced me to Zack shortly after that."

    # show bg wgbedroom
    hide kit
    show winter at left
    wg "Sounds like you guys really hit it off."
    show kit
    kw "Yup. Rest is history, of course."
    hide kit
    hide winter

    jump scene3

label scene3:

    # show bg fairviewdmv
    show sloth
    ds "Now serving 753."
    hide sloth
    show anthony
    aw "I'm so glad that's ove-"
    aw "What are you doing?"
    hide anthony
    show zack
    zc "Giving an application one star."
    show anthony at left
    aw "Why?"
    zc "So I can give it a good review."
    hide zack
    show anthony
    aw "What!? That makes no sense."
    hide anthony

    show zack
    zc "... Anthony"
    show anthony at right
    aw "What?"
    show zack at right
    zc "Is that channel 45?"
    aw "Yes. Yes it is."
    hide anthony
    hide zack
    show zenon
    zn "What are you two doing here?"
    hide zenon
    show anthony
    aw "Needed to get my license renewed. "
    extend "Why is the crew here?"
    hide anthony
    show zenon
    zn "There was a robbery over at Nation Holdings yesterday."
    show zack at left
    zc "Don't you have the day off, Anthony?"
    zn "Yes he does."
    show anthony
    hide zack
    hide zenon
    aw "And I'm standing behind that camera!"

    jump scene4

label scene4:

    # show bg wgbedroom
    kw "I noticed you have a lot of electronics lying around."
    wg "Oh yeah. I've been tinkering in it lately."
    kw "Is there anything you don't do?"
    wg "I can't drive."
    hide winter
    show kit
    kw "..."
    hide kit

    # show bg wggarage
    kw "What do all of these do?"
    ## The design is based on the radio transmitter from Sims 3: University life
    wg "This is a radio transmitter."
    wg "Anthony wanted to see if I could make one just for the heck of it."
    # show bg wgradio
    wg "It transmits to AM and FM."
    kw "And it works?"
    wg "Haven't tested it yet."
    kw "I wonder what the range of it is."
    wg "Wanna try it out?"
    kw "Sure!"

    # show bg wgoutsidegarage
    wg "Tuning in."
    $ kfbroad = "This is Kit broadcasting live from Fairview!"
    kw "[kfbroad]"
    "Radio" "[kfbroad]"
    wg "It works!"
    kw "This is so exciting!"
    wg "I know, right?"

    kw "Maybe Zack can help start a small radio station."
    wg "Think he'd be up for it?"
    kw "Why not? He really enjoys mixing music."

    jump scene5

label scene5:

    zn "The cops were able to take down the crimial before he could hurt any hostages."
    dn "Any word on the motives?"
    zn "No, Deanna. He did go on about \"new world order\" after he was arrested."
    dn "Thanks, Zenon."
    "This is KETO-TV, Channel 45."
    ea "And that's a wrap."

    zc "\"New world order\"?"
    aw "Don't ask."
    zn "So where are you two headed?"
    aw "Uh... "
    extemd "Hmm... "
    extend "Zack?"
    zc "Up for some sushi?"
    aw "SUSHI!"
    zn "I won't keep you. DMV is one hell of a wait."

    # show bg fvshuhidiner
    aw "Mmm... So good."
    zc "Try not to inhale it all."
    "Anthony burps."
    aw "Sorry."

    return
