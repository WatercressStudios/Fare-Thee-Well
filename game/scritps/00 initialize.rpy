######################### 
# Character Declaration #
#########################
define n = Character(None, kind=nvl)
define wan = Character('Wayfarer', color="#c8ffc8")
define ten = Character('Bartender', color="#d5567f")

######################
# Sprite Declaration #
######################
image bartender_young = "sprites/Young Bartender/young bartender.png"
image emmeline_young_happy = "sprites/Young Emmeline/young emmeline happy.png"

##################
# BG Declaration #
##################
image black = "#000"
image white = "#FFF"
image winterwoods = "bg/winter_path_filter_final.png"
image cedar_night = "bg/town_filter_final.png"
image bar_night = "bg/bar_filter_night_final.png"

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