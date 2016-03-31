######################### 
# Character Declaration #
#########################
define e = Character('Eileen', color="#c8ffc8")

######################
# Sprite Declaration #
######################


##################
# BG Declaration #
##################
image black                = "#000"
image white                = "#FFF"

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