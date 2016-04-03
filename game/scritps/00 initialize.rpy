﻿######################### 
# Character Declaration #
#########################
define n = Character(None, kind=nvl)
define wan = Character('Wayfarer', color="#c8ffc8")
define ten = Character('Bartender', color="#d5567f")
define gir = Character('Girl', color="#c7ffc7")
define nvlgir = Character('Girl', color="#c7ffc7", kind=nvl)
define emm = Character('Emmeline', color="#c7ffc7")
define can = Character('Candace', color="#c7ffc7")
define ros = Character('Rosa', color="#c7ffc7")
define mic = Character('Michael', color="#c7ffc7")

######################
# Sprite Declaration #
######################
image bartender_young = "sprites/Young Bartender/young bartender.png"
image emmeline_young_happy = "sprites/Young Emmeline/young emmeline happy.png"
image emmeline_young_surprise = "sprites/Young Emmeline/young emmeline surprise.png"
image emmeline_young_sad = "sprites/Young Emmeline/young emmeline sad.png"
image emmeline_young_angry = "sprites/Young Emmeline/young emmeline angry.png"
image emmeline_young_disgust = "sprites/Young Emmeline/young emmeline disgust.png"
image candace_std_happy = "sprites/Candace/candace standard happy.png"
image candace_std_sad = "sprites/Candace/candace standard sad.png"
image michael_older_happy = "sprites/Older Micheal/older micheal happy.png"
image rosa_happy = "sprites/Rosa/rosa happy.png"

##################
# BG Declaration #
##################
image black = "#000"
image white = "#FFF"
image winterwoods = "bg/winter_path_filter_final.png"
image cedar_night = "bg/town_filter_final.png"
image bar_night = "bg/bar_filter_night_final.png"
image stage = "bg/stage_filter_final.png"
image snow_bench = "bg/snow_bench.png"


###################
# CGs #
###################


#######
# VFX #
#######
image watercress = "vfx/splashscreen.png"


# Splash Screen
label splashscreen:
    scene black 
    with Pause(1)

    show watercress with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return

# Game starts here
label start:
    
    jump scene1