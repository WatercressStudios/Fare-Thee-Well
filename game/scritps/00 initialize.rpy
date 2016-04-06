######################### 
# Character Declaration #
#########################
define n = Character(None, kind=nvl)
define wan = Character('Wayfarer', color="#c8ffc8")
define ten = Character('Bartender', color="#d5567f")
define gir = Character('Girl', color="#c7ffc7")
define nvlgir = Character('Girl', color="#c7ffc7", kind=nvl)
define emm = Character('Emmeline', color="#c7ffc7")
define tru = Character('Trucker', color="#C75df7")

######################
# Sprite Declaration #
######################
image bartender_young = "sprites/Young Bartender/young bartender.png"
image emmeline_young_happy = "sprites/Young Emmeline/young emmeline happy.png"
image emmeline_young_surprise = "sprites/Young Emmeline/young emmeline surprise.png"
image emmeline_young_sad = "sprites/Young Emmeline/young emmeline sad.png"
image emmeline_young_angry = "sprites/Young Emmeline/young emmeline angry.png"
image emmeline_young_disgust = "sprites/Young Emmeline/young emmeline disgust.png"
image old_bartender_standard = "sprites/Old Bartender/Old Bartender - Standard Pose - Standard.png"
image old_bartender_sad = "sprites/Old Bartender/Old Bartender - Standard Pose - Sad.png"
image old_bartender_surprised = "sprites/Old Bartender/Old Bartender - Standard Pose - Surprised.png"

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
image highway = "bg/mainehighway_1.png"


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