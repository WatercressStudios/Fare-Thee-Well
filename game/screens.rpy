﻿# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who:
                    id "who" xpos -436 ypos 24

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu():
    
   tag menu
   # Tells Ren'Py what images to display on screen.
   add "ui/main/background.png"
   add "ui/main/photo.png" at from_bottom2
   add "ui/main/base_left.png" at from_left
   add "ui/main/base_right.png" xanchor 1.0 at from_right
   add "ui/main/lines_left.png" at from_top
   add "ui/main/lines_right.png" xanchor 1.0 yanchor 1.0 xpos 1920 at from_bottom
   # Imagebuttons, 'Auto' tells it to use both idle and hover states. Focus masks is something to do with the alpha properties but IDK off the top of my head.
   imagebutton auto "ui/main/start_%s.png" xpos 0 ypos 306 focus_mask None action Start() at from_left
   imagebutton auto "ui/main/load_%s.png" xpos 0 ypos 415 focus_mask None action ShowMenu('load') at from_left
   imagebutton auto "ui/main/gallery_%s.png" xpos 0 ypos 529 focus_mask None action ShowMenu('gallery_bg1') at from_left
   imagebutton auto "ui/main/jukebox_%s.png" xpos 0 ypos 638 focus_mask None action ShowMenu('music_room') at from_left
   imagebutton auto "ui/main/prefs_%s.png" xpos 0 ypos 747 focus_mask None action ShowMenu('preferences') at from_left
   imagebutton auto "ui/main/credits_%s.png" xpos 0 ypos 856 focus_mask None action Start("credits") at from_left
   imagebutton auto "ui/main/quit_%s.png" xpos 0 ypos 970 focus_mask None action Quit(confirm=False) at from_left
   # Adds the image as the final thing on the screen.
   add "ui/main/overlay.png"

init -2:
    # Defines transform properties to make images move.
    transform fade_in:
        alpha 0.0
        linear 1 alpha 1.0
    transform from_left:
        alpha 0.0 xpos -500
        linear 1 alpha 1.0 xpos 0
    transform from_right:
        alpha 0.0 xpos 2420
        linear 1 alpha 1.0 xpos 1920
    transform from_top:
        alpha 0.0 ypos -1100
        pause 1.5
        linear 1 alpha 1.0 ypos 0
    transform from_bottom:
        alpha 0.0 ypos 2200
        pause 1.5
        linear 1 alpha 1.0 ypos 1080
    transform from_bottom2:
        alpha 0.0 ypos 1080
        easein 1 alpha 1.0 ypos 0
    transform from_left2:
        alpha 0.0 xpos -500
        pause 1.5
        linear 1 alpha 1.0 xpos 0
    transform from_right2:
        alpha 0.0 xpos 2420
        pause 1.5
        linear 1 alpha 1.0 xpos 1920
    transform effect1:
        alpha 0.0
        linear 1 alpha 1.0
    transform from_top2:
        alpha 0.0 ypos -300
        linear 1 alpha 1.0 ypos 0
    transform from_bottom3:
        alpha 0.0 ypos 1300
        linear 1 alpha 1.0 ypos 1080
    transform gallery_slide:
        alpha 0.0 xpos -1920
        pause 1.5
        linear 1 alpha 1.0 ypos 945
    transform rotate_pic:
        alpha 0.0 rotate -10.0
        linear 4 alpha 1.0
    # alpha 0 > 1 is just a fadein, linear & easein are just the time taken for the effect to occur. First line of each transform defines the starting state and then the second is the final state.

##############################################################################
# Gallery Menu
#
# Screens that are used to display the gallery menu
# https://www.renpy.org/doc/html/rooms.html
init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.
    # A button that contains an image that automatically unlocks.
    g.button("bg1")
    g.display("bg/bar_filter_day_final.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg2")
    g.display("bg/bar_filter_night_final.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg3")
    g.display("bg/mainehighway_1.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg4")
    g.display("bg/snow_bench.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg5")
    g.display("bg/stage_filter_final.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg6")
    g.display("bg/summer forest.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg7")
    g.display("bg/town_filter_final.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg8")
    g.display("bg/wine_closet.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg9")
    g.display("bg/winter forest night revised.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg10")
    g.display("bg/winter park night.png")
    
    # A button that contains an image that automatically unlocks.
    g.button("bg11")
    g.display("bg/winter_path_filter_final.png")

    # This button has a condition associated with it, allowing the game
    # to choose which images unlock.
    g.button("art1")
    # g.condition("persistent.gallery_unlock_1")
    g.display("cg/InstantRiot1.png")
    
    # This button has a condition associated with it, allowing the game
    # to choose which images unlock.
    g.button("art2")
    # g.condition("persistent.gallery_unlock_2")
    g.display("cg/mm.jpg")
    
    # A button that contains an image that automatically unlocks.
    g.button("empty")
    # g.display("cg/grey.jpg")

    # The transition used when switching images.
    g.transition = dissolve
    
    gallery_rows = 3
    gallery_columns = 3
    
    #Thumbnail size
    thumbnail_x_size = 540
    thumbnail_y_size = 302

# Step 3. The gallery screen we use.
screen gallery_bg1:

    tag menu
    add "white"
    use navigation

    frame background None xpos 100 at fade_in:
        grid gallery_rows gallery_columns:

            # Call make_button to show a particular button.
            add g.make_button("bg1", im.Scale("bg/bar_filter_day_final.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("bg2", im.Scale("bg/bar_filter_night_final.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("bg3", im.Scale("bg/mainehighway_1.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)

            add g.make_button("bg4", im.Scale("bg/snow_bench.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("bg5", im.Scale("bg/stage_filter_final.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("bg6", im.Scale("bg/summer forest.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)

            add g.make_button("bg7", im.Scale("bg/town_filter_final.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("bg8", im.Scale("bg/wine_closet.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("bg9", im.Scale("bg/winter forest night revised.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
    
    add "ui/gallery/grid_divider.png" xpos 670 ypos 0 at effect1
    add "ui/gallery/grid_divider.png" xpos 1236 ypos 0 at effect1
    add "ui/gallery/divider.png" xpos 0 ypos 945 at effect1
    imagebutton auto "ui/gallery/next_%s.png" xpos 20 ypos 972 focus_mask None action ShowMenu("gallery_bg2") at effect1
            
screen gallery_bg2:

    tag menu
    add "white"
    use navigation

    frame background None xpos 100 at fade_in:
        grid gallery_rows gallery_columns:

            # Call make_button to show a particular button.
            add g.make_button("bg10", im.Scale("bg/winter park night.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("bg11", im.Scale("bg/winter_path_filter_final.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("art1", im.Scale("cg/InstantRiot1.png", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)

            add g.make_button("art2", im.Scale("cg/mm.jpg", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("empty", im.Scale("cg/grey.jpg", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("empty", im.Scale("cg/grey.jpg", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            
            add g.make_button("empty", im.Scale("cg/grey.jpg", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("empty", im.Scale("cg/grey.jpg", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            add g.make_button("empty", im.Scale("cg/grey.jpg", thumbnail_x_size, thumbnail_y_size), xalign=0.5, yalign=0.5, idle_border=None, background=None)
            
    add "ui/gallery/grid_divider.png" xpos 670 ypos 0 at effect1
    add "ui/gallery/grid_divider.png" xpos 1236 ypos 0 at effect1
    add "ui/gallery/divider.png" xpos 0 ypos 945 at effect1
    imagebutton auto "ui/gallery/previous_%s.png" xpos 20 ypos 972 focus_mask None action ShowMenu("gallery_bg1") at effect1

##############################################################################
# Music Menu
#
# Screen that's used to display the music menu
# https://www.renpy.org/doc/html/rooms.html
init python:

    # Step 1. Create a MusicRoom instance.
    jukebox = MusicRoom(channel=u'music')

    # Step 2. Add music files.
    jukebox.add("music/AgeOfTransition.ogg", always_unlocked=True)
    jukebox.add("music/Departure.ogg", always_unlocked=True)
    jukebox.add("music/BalladOfEmeline.ogg", always_unlocked=True)
    jukebox.add("music/Friends Old and New Loop.ogg", always_unlocked=True)
    jukebox.add("music/Lullaby for Cedar, Maine - Intro.ogg", always_unlocked=True)
    jukebox.add("music/Snowy Night - Intro.ogg", always_unlocked=True)
    jukebox.add("music/ThemeForAWanderer.ogg", always_unlocked=True)
    jukebox.add("music/Written to Memory - Intro.ogg", always_unlocked=True)

# Step 3. Create the music room screen.
screen music_room:

    tag menu
    add "white"
    use navigation

    # The buttons that play each track.
    add "ui/jukebox/tracklist.png" xpos 40 ypos 20 at effect1
    imagebutton auto "ui/jukebox/age_%s.png" xpos 40 ypos 120 focus_mask None action jukebox.Play("music/AgeOfTransition.ogg")
    imagebutton auto "ui/jukebox/departure_%s.png" xpos 40 ypos 220 focus_mask None action jukebox.Play("music/Departure.ogg")
    imagebutton auto "ui/jukebox/emmeline_%s.png" xpos 40 ypos 320 focus_mask None action jukebox.Play("music/BalladOfEmeline.ogg")
    imagebutton auto "ui/jukebox/friends_%s.png" xpos 40 ypos 420 focus_mask None action jukebox.Play("music/Friends Old and New Loop.ogg")
    imagebutton auto "ui/jukebox/lullaby_%s.png" xpos 40 ypos 520 focus_mask None action jukebox.Play("music/Lullaby for Cedar, Maine - Intro.ogg")
    imagebutton auto "ui/jukebox/snowy_%s.png" xpos 40 ypos 620 focus_mask None action jukebox.Play("music/Snowy Night - Intro.ogg")
    imagebutton auto "ui/jukebox/theme_%s.png" xpos 40 ypos 720 focus_mask None action jukebox.Play("music/ThemeForAWanderer.ogg")
    imagebutton auto "ui/jukebox/written_%s.png" xpos 40 ypos 820 focus_mask None action jukebox.Play("music/Written to Memory - Intro.ogg")
    
    # Buttons that let us advance tracks.
    add "ui/jukebox/options.png" xpos 1459 ypos 20 at effect1
    imagebutton auto "ui/jukebox/next_%s.png" xpos 1541 ypos 120 focus_mask None action jukebox.Next()
    imagebutton auto "ui/jukebox/previous_%s.png" xpos 1541 ypos 220 focus_mask None action jukebox.Previous()
    imagebutton auto "ui/jukebox/stop_%s.png" xpos 1541 ypos 320 focus_mask None action jukebox.Stop()
    imagebutton auto "ui/jukebox/shuffle_%s.png" xpos 1541 ypos 420 focus_mask None action jukebox.RandomPlay()
    
    add "ui/jukebox/volume_header.png" xpos 1400 ypos 740 at effect1
    frame xpos 1209 ypos 820:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
        at effect1
        
    add "ui/jukebox/left_divider.png" xpos 0 ypos 88 at effect1
    add "ui/jukebox/right_divider.png" xpos 1170 ypos 88 at effect1
    add "ui/jukebox/vertical_divider.png" xpos 20 ypos 0 at effect1
    add "ui/jukebox/vertical_divider.png" xpos 1900 ypos 0 at effect1
    add "ui/gallery/divider.png" xpos 0 ypos 945 at effect1
    
    add "ui/jukebox/pic.png" xpos 545 ypos 0 at rotate_pic
    
    # Start the music playing on entry to the music room.
    # on "replace" action jukebox.Play()

    # Restore the main menu music upon leaving.
    # on "replaced" action Play("music", "music/Departure.ogg")

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():
    imagebutton auto "ui/navigation/return_%s.png" xpos 552 ypos 972 focus_mask None action Return() at effect1
    imagebutton auto "ui/navigation/save_%s.png" xpos 772 ypos 972 focus_mask None action ShowMenu('save') at effect1
    imagebutton auto "ui/navigation/load_%s.png" xpos 962 ypos 972 focus_mask None action ShowMenu('load') at effect1
    imagebutton auto "ui/navigation/prefs_%s.png" xpos 1152 ypos 972 focus_mask None action ShowMenu('preferences') at effect1
    imagebutton auto "ui/navigation/title_%s.png" xpos 1462 ypos 972 focus_mask None action MainMenu() at effect1
    imagebutton auto "ui/navigation/quit_%s.png" xpos 1652 ypos 972 focus_mask None action Quit() at effect1
    
##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen save:
    tag menu
    add "ui/main/background.png" 
    add "ui/prefs/screens_top.png" at from_top2
    add "ui/prefs/screens_bottom.png" yanchor 1.0 ypos 1080 at from_bottom3
    add "ui/prefs/lines_top.png" at from_left2
    add "ui/prefs/lines_bottom.png" xanchor 1.0 yanchor 1.0 ypos 1080 at from_right2
    add "ui/prefs/base.png" at effect1
    add "ui/saveload/save_title.png" at effect1
    use navigation
    use file_picker
    add "ui/main/overlay.png"
    
screen load:
    tag menu
    add "ui/main/background.png" 
    add "ui/prefs/screens_top.png" at from_top2
    add "ui/prefs/screens_bottom.png" yanchor 1.0 ypos 1080 at from_bottom3
    add "ui/prefs/lines_top.png" at from_left2
    add "ui/prefs/lines_bottom.png" xanchor 1.0 yanchor 1.0 ypos 1080 at from_right2
    add "ui/prefs/base.png" at effect1
    add "ui/saveload/load_title.png" at effect1
    use navigation
    use file_picker
    add "ui/main/overlay.png"
    
screen file_picker:
    imagebutton auto "ui/saveload/quick_%s.png" xpos 378 ypos 823 focus_mask None action FilePage("quick") at effect1
    imagebutton auto "ui/saveload/auto_%s.png" xpos 563 ypos 823 focus_mask None action FilePage("auto") at effect1
    imagebutton auto "ui/saveload/1_%s.png" xpos 725 ypos 823 focus_mask None action FilePage(1) at effect1
    imagebutton auto "ui/saveload/2_%s.png" xpos 818 ypos 823 focus_mask None action FilePage(2) at effect1
    imagebutton auto "ui/saveload/3_%s.png" xpos 912 ypos 823 focus_mask None action FilePage(3) at effect1
    imagebutton auto "ui/saveload/4_%s.png" xpos 1010 ypos 823 focus_mask None action FilePage(4) at effect1
    imagebutton auto "ui/saveload/5_%s.png" xpos 1104 ypos 823 focus_mask None action FilePage(5) at effect1
    imagebutton auto "ui/saveload/6_%s.png" xpos 1196 ypos 823 focus_mask None action FilePage(6) at effect1
    imagebutton auto "ui/saveload/7_%s.png" xpos 1291 ypos 823 focus_mask None action FilePage(7) at effect1
    imagebutton auto "ui/saveload/8_%s.png" xpos 1384 ypos 823 focus_mask None action FilePage(8) at effect1
    imagebutton auto "ui/saveload/9_%s.png" xpos 1478 ypos 823 focus_mask None action FilePage(9) at effect1
    
    imagebutton auto "ui/saveload/slot_%s.png" xpos 236 ypos 195 focus_mask True action FileAction(1) at effect1
    add "ui/saveload/empty.png" xpos 255 ypos 214 at effect1
    use load_save_slot(number=1, x=236, y=195) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 236 ypos 406 focus_mask True action FileAction(2) at effect1
    add "ui/saveload/empty.png" xpos 255 ypos 425 at effect1
    use load_save_slot(number=2, x=236, y=406) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 236 ypos 617 focus_mask True action FileAction(3) at effect1
    add "ui/saveload/empty.png" xpos 255 ypos 636 at effect1
    use load_save_slot(number=3, x=236, y=617) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 1023 ypos 195 focus_mask True action FileAction(4) at effect1
    add "ui/saveload/empty.png" xpos 1042 ypos 214 at effect1
    use load_save_slot(number=4, x=1023, y=195) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 1023 ypos 406 focus_mask True action FileAction(5) at effect1
    add "ui/saveload/empty.png" xpos 1042 ypos 425 at effect1
    use load_save_slot(number=5, x=1023, y=406) 
    imagebutton auto "ui/saveload/slot_%s.png" xpos 1023 ypos 617 focus_mask True action FileAction(6) at effect1
    add "ui/saveload/empty.png" xpos 1042 ypos 636 at effect1
    use load_save_slot(number=6, x=1023, y=617) 
    
screen load_save_slot:
    hbox:
        style_group "watercress"
        textbutton _("Delete") xpos x+530 ypos y+125  action FileDelete(number) at effect1

    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty."), FileSaveName(number))

    text file_text xpos x+295 ypos y+18 style_group "watercress" at effect1

    add FileScreenshot(number) xpos x+19 ypos y+19 at effect1
    
init -2 python:
    config.thumbnail_width = 260
    config.thumbnail_height = 146

init -2:
    style watercress_button:
        is default
        background None
    style watercress_button_text:
        is default
        size 38
        idle_color "#FFE2BC"
        hover_color "#5B3D28"
        insensitive_color "#808080"
        drop_shadow [(2, 2,)]
        drop_shadow_color (0, 0, 0, 100)
    style watercress_text:
         is default
         size 42
         color "#FFE2BC"
         idle_color "#FFE2BC"
         drop_shadow [(2, 2,)]
         drop_shadow_color (0, 0, 0, 100)


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    add "ui/main/background.png" 
    add "ui/prefs/screens_top.png" at from_top2
    add "ui/prefs/screens_bottom.png" yanchor 1.0 ypos 1080 at from_bottom3
    add "ui/prefs/lines_top.png" at from_left2
    add "ui/prefs/lines_bottom.png" xanchor 1.0 yanchor 1.0 ypos 1080 at from_right2
    add "ui/prefs/base.png" at effect1
    add "ui/prefs/prefs_title.png" at effect1
    add "ui/prefs/prefs_titles.png" at effect1
    use navigation
    imagebutton auto "ui/prefs/fullscreen_%s.png" xpos 183 ypos 274 focus_mask None action Preference('display','fullscreen') at effect1
    imagebutton auto "ui/prefs/windowed_%s.png" xpos 505 ypos 273 focus_mask None action Preference('display', 'window')  at effect1
    
    imagebutton auto "ui/prefs/enabled_%s.png" xpos 183 ypos 432 focus_mask None action Preference('transitions', 'all') at effect1
    imagebutton auto "ui/prefs/disabled_%s.png" xpos 505 ypos 432 focus_mask None action Preference('transitions', 'none') at effect1
    
    imagebutton auto "ui/prefs/skipall_%s.png" xpos 183 ypos 604 focus_mask None action Preference('skip', 'all') at effect1
    imagebutton auto "ui/prefs/skipread_%s.png" xpos 505 ypos 603 focus_mask None action Preference('skip', 'seen') at effect1
    
    imagebutton auto "ui/prefs/stopskip_%s.png" xpos 183 ypos 768 focus_mask None action Preference('after choices', 'stop') at effect1 
    imagebutton auto "ui/prefs/keepskip_%s.png" xpos 505 ypos 768 focus_mask None action Preference('after choices', 'skip') at effect1
    
    frame xpos 1170 ypos 456:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
        at effect1
    frame xpos 1170 ypos 701:
        style_group "pref"
        has vbox
        bar value Preference("voice volume")
        at effect1
    frame xpos 1171 ypos 212:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
        at effect1
    frame xpos 1172 ypos 332:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")
        at effect1
    frame xpos 1171 ypos 572:
        style_group "pref"
        has vbox
        bar value Preference("sound volume") 
        at effect1
        
    add "ui/main/overlay.png"

        
init -2 python: 
    style.pref_frame.background = None
    style.pref_slider.left_bar = "ui/prefs/bar_full.png"
    style.pref_slider.right_bar = "ui/prefs/bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.thumb_offset = 0
    style.pref_slider.xmaximum = 580
    style.pref_slider.ymaximum = 51
    style.pref_slider.xminimum = 580


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    add "ui/yn/background.png" 
    add "ui/yn/base_left.png" at from_left
    add "ui/yn/base_right.png" xanchor 1.0 at from_right
    add "ui/yn/lines_left.png" at from_top
    add "ui/yn/lines_right.png" xanchor 1.0 yanchor 1.0 xpos 1920 at from_bottom
    imagebutton auto "ui/yn/yes_%s.png" xpos 1393 ypos 574 xanchor 1.0 focus_mask None action yes_action at from_right
    imagebutton auto "ui/yn/no_%s.png" xpos 1394 ypos 735 xanchor 1.0 focus_mask None action no_action at from_right
    add "ui/main/overlay.png"
    
    if message == layout.ARE_YOU_SURE:
        add "ui/yn/message_quit.png" xanchor 1.0 at from_right
    elif message == layout.DELETE_SAVE:
        add "ui/yn/message_delete.png" xanchor 1.0 at from_right
    elif message == layout.OVERWRITE_SAVE:
        add "ui/yn/message_overwrite.png" xanchor 1.0 at from_right
    elif message == layout.LOADING:
        add "ui/yn/message_load.png" xanchor 1.0 at from_right
    elif message == layout.QUIT:
        add "ui/yn/message_quit.png" xanchor 1.0 at from_right
    elif message == layout.MAIN_MENU:
        add "ui/yn/message_title.png" xanchor 1.0 at from_right


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.99
        yalign 0.99

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 24
        idle_color "#888888"
        hover_color "#5B3D28"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

