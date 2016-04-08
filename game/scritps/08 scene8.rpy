# Fare Thee Well

# Act Three — Scene Two? - Fare Thee Well

# Written by DarkEndless

# BG - Bar Background
# Sprite - Old Man/Bartender

label scene8:
    
    play music "music/Friends Old and New Loop.ogg" fadein 1.0
    
    scene bar_day with fade

    "The next morning, I arrive early enough to help the bartender with the tables, stools, and chairs. The worn wood seems to embody the place as a whole - well worn with time and filled with warmth."

    show old_bartender_standard_cleaning_glass

    "I take a seat in front of the bar as the old man organizes the rainbow of colored glass bottles behind it."

    ten "Calm down, son. You’d think someone with as much experience as you would’ve learned to deal with these situations."

    wan "Saying goodbye is easy. But the returns, and the greetings..."

    "The old man met my eyes and inclined his head toward the door. Making my best effort to keep my door, I notice Emmeline and her son - probably around seven years old. An inquisitive blue-eyed boy with brown hair."

    #Sound - door opens?
    
    stop music fadeout 1.0
    
    #Emmeline (Middle Aged) and Young Michael enter
    
    play music "music/Snowy Night - Loop.ogg" fadein 1.0
    
    hide old_bartender_standard_cleaning_glass

    show middle_aged_emmeline_sad at right

    show young_micheal_happy at left

    "Emmeline glances around the bar and seems mildly disappointed. Her gaze flits over me as it would one of the tables. She approaches the old man."

    emm "You set up without me?"

    show old_bartender_sad_cleaning_glass

    ten "Sorry, Em. I should’ve mentioned earlier that I have a new employee in training - he helped me this morning. We still have the stage to set up, though. I’ll get you some work yet."

    "She looks at me directly for the first time, but there is no spark of memory in her eyes - only the casual friendliness of someone greeting a new acquaintance."

    hide middle_aged_emmeline_sad
   
    show middle_aged_emmeline_happy at right
    
    show old_bartender_happy_cleaning_glass

    emm "Oh. Nice to meet you! I’m Emmeline, and this is my son Michael."

    hide young_micheal_happy

    show young_micheal_fear at left

    "Michael plays with the collar of his shirt and averts his eyes."

    mic "Hi…"

    "I give him a smile and a wave, and then extend my hand to Emmeline. She shakes it. I take a page out of Michael’s book - I’m too nervous to meet her gaze directly for too long."

    wan "It’s nice to meet you both."
    
    hide young_micheal_fear

    show young_micheal_happy at left
    
    stop music fadeout 1.0

    ten "Right, well. That stage isn’t going to set up itself. Em, why don’t you and Michael teach this greenie here the ropes. I’ve got a few more glasses to clean."

    show old_bartender_standard_cleaning_glass

    "Emmeline nods and gestures for Michael to follow her to the stage."

    hide young_micheal_happy
    
    hide middle_aged_emmeline_happy
    
    hide old_bartender_happy_cleaning_glass
    
    hide old_bartender_standard_cleaning_glass
    
    hide old_bartender_sad_cleaning_glass
    
    with Pause(.5)

    #BG - Bar stage

    #Sprites - Michael (Young), Emmeline (Middle Aged)
    
    play music "music/Written to Memory - Intro.ogg" fadein 1.0
    queue music "music/Written to Memory - Loop.ogg"
    
    scene stage with fade

    show middle_aged_emmeline_happy 

    emm "Have you ever worked in a bar before?"

    wan "I know my way around one."

    hide middle_aged_emmeline_happy
    
    show middle_aged_emmeline_happy at right
    
    emm "Don't we all."

    show young_micheal_happy at left
 
    "Michael climbs up the front of the stage and seemed to be opening a bin that contained the cables."

    emm "How old are you? Twenty five?"

    wan "I’m a little older than I look. I’m assuming he’s done this before?"

    "Emmeline walks beside the stage to retrieve a broom and a dustpan before starting to sweep behind the speakers, amps, and other sound equipment."

    emm "Yeah. He loves to listen to music, so this is right up his alley. It’s Karaoke night tonight, so the setup will be a little different."

    "I set about putting the microphone center stage, and I feel something nudge my leg. I see Michael holding a cable toward me."

    mic "That one goes with this one."

    wan "Oh. Thanks. What kind of music do you enjoy, Michael?"

    hide young_micheal_happy

    show young_micheal_surprised at left

    "I take the cable he offered me and hook it up. Surely enough, the audio jack and ports are the correct sizes, and the cable is long enough to walk around the stage with if necessary."

    mic "The Stray Cats, and, uh…"

    "He looks at his Mother for answers, looking anxious."

    emm "You remember. Depeche Mode, sometimes you listen to Michael Jackson. I’m more of a Simon and Garfunkel gal myself. The new stuff isn’t bad, but there’s something about the acoustic guitars…"

    hide young_micheal_surprised

    show young_micheal_happy at left

    wan "It brings to mind the open road, and people singing in new bars. Soft atmospheres and a good crowd."

    "Emmeline looks back at me and gives me a genuine smile - not the practiced friendliness of polite greeting, but something with altogether more substance. Michael and I finish setting up all of the relevant cords."

    emm "Yeah. You took the words right out of my mouth. Well, it’s about time - I have to get Michael to school."

    #BG - Bar Proper

    #Sprites - Young Michael, Middle aged Emmeline, Old man
    
    hide young_micheal_happy
    
    hide middle_aged_emmeline_happy
    with Pause(.5)
    
    scene bar_day with fade

    show young_micheal_happy at left

    show middle_aged_emmeline_happy at right

    show old_bartender_happy

    "Emmeline waves goodbye to the bartender and takes Michael’s hand, walking toward the door."

    ten "Same time tomorrow. Have a good day."
    
    stop music fadeout 1.0

    "Emmeline pauses before she reaches the door and freezes in place. At first I wonder if she had forgotten something, but then she turns, and I see it."

    "That spark of remembrance, the warmth in her eyes that signifies memory. Now she knows who I am. She remembers that night, two decades past. She brings a hand to her cheek as Michael tugs at her shirt."
    
    mic "Mommy, are you okay?"

    emm "I’m alright. Let’s get you to school."

    #Michael and Emmeline leave

    hide middle_aged_emmeline_happy

    hide young_micheal_happy

    "I sigh and lean against the worn mahogany of the bar, and I can hear the bartender pouring a glass of something. I didn’t bother to turn around - my eyes were fixed on the road, watching them drive away."

    ten "Well, you couldn’t have been expecting anything else, could you?"
    
    play music "music/Departure.ogg" fadein 1.0
    
    wan "No, I couldn’t have. Do you want to hear the story of that winter night?"

    ten "Yeah, why not. This is for you, by the way. Looks like you could use it. On the house."

    "I turn enough to pick it up, and take a sip, but my gaze remains on the road. Emmeline is long gone by now, but I can’t bring myself to look inside again. Not just yet."

    wan "I don’t know how much you remember. Em and I left after talking. Really bonding, you know. At one of these tables, by that window."

    "I gesture in the general direction with a finger extended from my hand that held my drink. The brownish fluid sloshed around behind the intricate lines in the glass, and I realized that it was the same kind I had used that night so many years ago."

    wan "We walked out of this place together and explored the town after dark. Playing in the snow, laughing together… But at the end of the night, we sat close and just talked. I brought up the legend of the wanderer. I didn’t think she’d take it seriously."

    wan "But she did. She listened, and in the end she identified with it. Of course, you know Emmeline’s story - how she got here. She has every bit as much wanderlust as I did."

    "I take a sip from my glass and turn around before looking into the cup."

    wan "Or… had. I guess everyone else like me eventually grows out of that phase. I suppose a part of me realized it then. I didn’t want to break her heart, so I just left. Ultimately, I shouldn’t be surprised that she didn’t remember me at first."

    wan "I’m sure she’s had to deal with her share of people walking out of her life. It was only one night."

    show old_bartender_sad

    ten "It was a long night."

    "The old man puts a comforting hand on my shoulder."

    ten "You know, I didn’t think Emmeline would ever settle down. But her husband… well, you’d like him. He runs the tri-county newspaper. Takes the family camping often in the summer and autumn. You couldn’t ask for a better life for her or her son in this town."

    "I nod and hand the bartender back his glass."

    wan "Thanks for the drink. And thanks for the cover earlier. Do you really need some help around here?"

    show old_bartender_standard

    ten "That I do. If you want to settle in for a few years, I’d love to have you around. But you know what happens if you stay, wanderer. You sure you want to deal with that?"

    hide old_bartender_standard

    show old_bartender_sad

    "I ran a hand through my hair and looked outside, wondering what it would be like to stay in this town for a few years."

    wan "I think I’m going to get some fresh air. If I return, you’ll know my answer. If I don’t - well, you’ll know just the same."

    #Wolf's part of scene 2

    ten "Actually, if you wouldn't mind, I think I need a break for today. If it's okay with you…"

    wan "Yeah, I'll close up shop. I'll keep everything straight, don't worry."
    
    hide old_bartender_sad

    show old_bartender_happy

    "The bartender nods, wipes a few more surfaces, and heads out. He gives me one last fleeting smile before the door closes with an odd sense of finality."

    #Wolf's scene 3
    
    hide old_bartender_happy
    with Pause(.5)

    scene bar_day with fade
    
    stop music fadeout 1.0

    "With that, I am left alone. The emptiness of the bar fills the air, silence keeping me company as it has the past hundred years." 

    "The familiar smells of drafts, the familiar atmosphere of the community, made of vagabonds and travelers, friends and families, of those with homes and of those who have yet to find theirs... the familiar sense of loneliness."
    
    play music "music/Age of Transition - Intro.ogg" fadein 1.0
    queue music "music/Age of Transition - Loop.ogg"
    
    "Have I found my home? Is this my final resting place? Is this where I will eak out the rest of my existence, however long into infinity that it may take me?"

    "I honestly don't know."

    "The heat of the bar begins to constrict my breathing, the weight of it all crushing me, claustrophobically, the warm lights a blazing fire."

    "Tugging at my collar, I grab my belongings and walk out of the door. It closes ever so softly behind me, the entrance framing me, engulfing me."

    scene highway with fade

    "I turn and make my way down the street. Buildings, both new and old, guide me, gradually giving way to more and more nature, as I continue my journey."

    "I find myself in front of a large, somewhat young tree. It's appearance does little to betray the true age of the form, being perhaps only a hundred years old or so."
    
    "This is as good a place as any, and I sit against it, allowing the trunk to support my back."

    "I ache."

    "I ache like an old man would, despite having no reason to. My body is fine; my body is young, despite my mind not being so."

    "Cool air fills me, embracing me as the winds dance upon my skin. The tree responds in kind, swaying this way and that, lively, almost youthful and energetic, life only just beginning for the poor soul."

    "I sit motionless, knowing what must come. I need not distract myself - I have a very important decision to make."

    "It's a simple decision, really."

    "Something a normal person wouldn't even hesitate to answer."

    "Do I stay, or do I go?"

    "The wind quiets down, all things listening intently to my every word, my every thought."

    "I guess, in reality, the more important question is whether or not she would care."

    "Does she remember me? That moment, earlier, gave me the feeling… But how could she forget, that magical night? Out of my many years of existence, that is the one memory that I am certain to never lose."

    "Maybe she just… did what I never could."

    "The air turns frigid, humid. Someone shakes me out of my lull, my trance, my thoughts and memories."
    
    stop music fadeout 1.0

    play music "music/Rain_Background-Mike_Koenig-1681389445.mp3"
    
    "Rain."
    
    "It's raining."

    "The rain continues to shake me, spreading through my clothes, across my cold skin."

    "I know what I have to do. It isn't about me, it's about everyone else, isn't it?"

    "I can't keep hurting people like this. It's for the better that I don't stay. They'd have to keep secrets, hide me away, or worse still, they'd have to die, seeing my eternal youth, seeing what they once were and what they could never be."

    "They'd all die, and I'd still be there, forever burying them, the job of a father at war or a son in peace."

    "I am not like them. I am not one of them. It is not my place to be here, to serve as a constant reminder of what they must have, and what I am fated to never feel."

    "Shivering now, I try to stand up, to walk away from everything."

    "I can't."

    "My muscles refuse to respond, screaming at me, aching through and through. My heart gives out, telling me what my brain never would, never should."

    "Don't run from this."

    "Stay here."

    "Don't leave her again."

    "No, no. I can't. I can't stay here, and yet I can't leave her again. The rain penetrates the canopy, pouring over me, as though lending a few short moments of quiet clarity were too much for the youngling, overcome by the weight of the world.."

    "I'm sorry that you have to go through this again."

    "I force myself through the pain, standing on my youth, with it, regaining my stature. I leave the now corrupted embrace of the tree, out into the chilled weather."

    "Looking up from my sodden boots, my vision is blocked by the one thing I had planned to never see again."

    "It reads, simply, CEDAR, MAINE."

    "A simple representation of the place, the family that I had grown to love."

    "The aching becomes unbearable, and I am forced to lean against the sign, my full weight causing the sign to waver, temporarily, until it catches itself, accepting me."

    "I cannot see the world beyond the sign, my vision entirely blocked."

    "I've made my decision. Please, please, get out of my way."
 
    "The sign remains, quiet as it always was."

    "I beg, I plead. I can't watch them die! I can't be here! Only pain will come from this. Once again, I will be alone. Once again, I will be held down by my regrets."

    "It remains."
    
    stop music fadeout 1.0

    "The clouds begin to dissipate, the cold rain gone, the warm air flooding down, back into me."
    
    "The crickets begin to chirp, frogs ever so loud, life filling the air."
    
    "So. The decision has been made for me."

    "I turn back from the sign, the town of Cedar, Maine staring right back at me, expecting me to return as if it never had a second thought."

    "The humid air clings to my skin, as I make my way back to the Bar. I pass the tree once again, waving its leaves in the wind, welcoming me back."

    "I pass that, as the buildings become less sparse and the nature recedes, the Bar enters my vision."

    scene bar_day with fade

    "I enter my home, the heat helping warm my clothes and my skin. I look at the things around me in appreciation, wiping the bar, cleaning it as if it were my own."

    jump scene9
