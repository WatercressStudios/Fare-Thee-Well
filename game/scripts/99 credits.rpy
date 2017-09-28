label credits:
    
    scene black

    stop music

    $ renpy.movie_cutscene("vfx/credits.mpg") # Loads the credit video

    scene black 
    with Pause(1)

    show watercress with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return