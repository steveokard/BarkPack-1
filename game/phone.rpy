################################################################################
## Mobile phone framework
## https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=40245&p=427567#p427567

image phone = "images/phone.png"

## Phone #######################################################################
init 5:
    style phone_message_vbox:

        xalign 0.5
        yalign 0
        ypos 480
        xsize 240
        xoffset -10

    style phone_message_frame:

        background Solid("#71c837")
        ypadding 10
        xpadding 10

    style phone_message_frame2:

        background Solid("#78E8A0")
        ypadding 10
        xpadding 10

    style phone_message_contents:

        spacing 10

    style phone_message is say_dialogue:

        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style phone_message2 is say_dialogue:

        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style phone_message_who is phone_message:

        color "#ffffff"
        size 18

    style phone_message_what is phone_message:

        color "#ffffff"
        size 18

    style phone_message_who2 is phone_message:

        color "#000000"
        size 18

    style phone_message_what2 is phone_message:

        color "#000000"
        size 18

    style phone_reply is default:

        size 18
        xalign 0.5
        xsize 200
        background Solid("#666")
        hover_background Solid("#78E8A0")
        ypadding 10
        xpadding 10

## Phone messages ##############################################################
screen phone_message(who, what):

    vbox at incoming_message:

        style_group "phone_message"

        add "images/bubble-tip.png" at phone_message_bubble_tip
        frame:
            style_group "phone_message"


            vbox:
                style "phone_message_contents"
                text who style "phone_message_who"
                text what style "phone_message_what"

screen phone_message2(who, what):

    vbox at incoming_message:

        style_group "phone_message"
        xoffset -480

        xalign 1.0

        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid("#ffffff")
            xsize 200

            vbox:
                style "phone_message_contents"

                text who style "phone_message_who2"
                text what style "phone_message_what2"

screen phone_reply(reply1, label1, reply2, label2):

    modal True

    vbox:
        xalign 0.5
        yalign 0.96
        spacing 5
        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"

## Picking up the phone ########################################################
transform phone_pickup:

    yalign 1.0 xalign 0.5
    yoffset 600
    easein 0.3 yoffset 200

    on hide:
        easeout 0.2 yoffset 600

transform phone_message_bubble_tip:

    xoffset 10
    yoffset 1

transform phone_message_bubble_tip2:

    xoffset 165
    yoffset 1

transform scrolling_out_message:

    easeout 0.1 yoffset -30 alpha 0

transform incoming_message:

    yoffset 100
    alpha 0

    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message
