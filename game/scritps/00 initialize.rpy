######################### 
# Character Declaration #
#########################
define n = Character(None, what_color="#FFFFFF", kind=nvl)
define wan = Character('Wayfarer', color="#800000", show_two_window=True)
define ten = Character('Bartender', color="#993399", show_two_window=True)
define gir = Character('Girl', color="#333399", show_two_window=True)
define nvlgir = Character(None, what_color="#FFFFFF", kind=nvl)
define emm = Character('Emmeline', color="#333399", show_two_window=True)
define tru = Character('Trucker', color="#666666", show_two_window=True)
define mic = Character('Micheal', color="#006600", show_two_window=True)
define can = Character('Candace', color="#663300", show_two_window=True)
define ros = Character('Rosa', color="#6600cc", show_two_window=True)
define mic = Character('Michael', color="#336699", show_two_window=True)

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
image old_bartender_happy = "sprites/Old Bartender/Old Bartender - Standard Pose - Happy.png"
image old_bartender_standard_cleaning_glass = "sprites/Old Bartender/Old Bartender - Cleaning Glass - Standard.png"
image old_bartender_sad_cleaning_glass = "sprites/Old Bartender/Old Bartender - Cleaning Glass - Sad.png"
image old_bartender_happy_cleaning_glass = "sprites/Old Bartender/Old Bartender - Cleaning Glass - Happy.png"
image middle_aged_emmeline_sad = "sprites/Middle Aged Emmeline/middle aged emmeline sad.png"
image middle_aged_emmeline_happy = "sprites/Middle Aged Emmeline/middle aged emmeline happy.png"
image young_micheal_happy = "sprites/Young Micheal/young micheal happy.png"
image young_micheal_fear = "sprites/Young Micheal/young micheal fear.png"
image young_micheal_surprised = "sprites/Young Micheal/young micheal surprise.png"
image candace_std_happy = "sprites/Candace/candace standard happy.png"
image candace_std_sad = "sprites/Candace/candace standard sad.png"
image michael_older_happy = "sprites/Older Micheal/older micheal happy.png"
image michael_older_surprise = "sprites/Older Micheal/older micheal surprise.png"
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
image highway = "bg/mainehighway_1.png"
image bar_day = "bg/bar_filter_day_final.png"

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

init python:
    def callback_transition(event, interact=True, **kwargs):
        if event == "begin":
            renpy.transition(dissolve, layer="master")
        
    config.all_character_callbacks = [callback_transition] 

# Game starts here
label start:
    
    jump scene1