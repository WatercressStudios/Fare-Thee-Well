# Fare Thee Well
# Act Three — Fare Thee Well
# Written by OptionalSauce and DarkEndless
    
label scene9:
    
    scene black 
    
    stop music
    
    nvl clear
    
    n "December — 2002"
    
    nvl clear
    
    scene black 
    
    scene stage 
    
    with Pause(.5)
    
    show rosa_happy at center 

    "A lone vocalist in a violet dress takes the stage at The Hearth and Home."

    "She appears to be close to Michael's age, who is now twenty-four."
    
    "The girl gazes with at the expectant faces all around her."
    
    "A hush falls over the crowd as she leans into the microphone. Her face betrays not a single emotion but pure wonder."
    
    "Like she's somewhere else, remembering better times, preparing to sing to herself in a world that stood still to hang off her every word."
    
    "The young woman starts to sing, and the the meager audience is immediately captivated."
    
    "She begins softly, her voice barely above a whisper."
    
    play music "music/Emmeline's Ballad - Intro.ogg" fadein 1.0
    queue music "music/Emmeline's Ballad - Loop.ogg"
        
    ros "Come over the hills, my bonnie Irish lass..."
    ros "Come over the hills to your darling..."
    ros "You choose the road, love, and I'll make the vow..."
    ros "And I'll be your true love forever."
    
    "Her voice is beautiful and wraps around the dark air of the old bar."
    "I knew this song. I knew it well."
    "Though I've heard it sung better before, I admit."
    
    ros "Red is the rose that in yonder garden grows.."
    ros "Fair is the lily of the valley..."
    ros "Clear is the water that flows from the Boyne..."
    ros "But my love is fairer than any."
    
    "She has one of the best voices I've heard in all my life."
    "I've only been this absorbed in song once before."
    "The voice of the girl in the blue dress grows, and grows, and grows, only to fill the air with complete emotion, feelings seething with energy."
    "Like her voice is an endless flowing spring, and to listen to it is to drink, and drink, and drink again."
    "It's nice to feel this way one more time... even if it's not as strongly."
    "The girl in the blue dress continues to sing."
    "While she finishes Red is the Rose and prepares for her next song, she takes a fateful step back from the microphone."
    "Her skin beads with sweat. Her chest heaves up and down to the rhythmic beat of her exhausted heart."
    "Her posture is tired, but proud. Her breath short, but steady. Her eyes somber, but bright, vibrant with fire."
    "She steps back up to the mic and keeps on singing."

    hide rosa_happy
    
    stop music fadeout 1.0
    
    with Pause(.5)
    
    scene bar_night with fade
    
    # Sprites - Candace, Michael
    
    show candace_std_happy at right
    
    show michael_older_happy at left

    "Across the bar stand the current employees of The Hearth and Home, Candace and Michael, who has taken the job his mother once held to help pay for his education."

    "Candace and I are having a lovely conversation, but Michael's unwavering attention is set on the young performer."

    can "Hey, Michael?"

    "Candace tries to grab her employee's attention, but has little success."

    can "Mike? Hello in there?"

    hide candace_std_happy
    
    show candace_std_sad
    
    play music "music/Written to Memory - Intro.ogg" fadein 1.0
    queue music "music/Written to Memory - Loop.ogg"
    
    "Candace gives a defeated sigh, and waves a hand in front of Michael's face, jolting him back to reality."

    mic "Oh, uh, sorry Candace. What did you need?"

    hide candace_std_sad

    show candace_std_happy

    "Candace laughs at the young man. She's clearly embarrassed him, so it's no surprise that his face has become several shades redder than some of the wines behind the bar."

    can "Table four was waving you down for refills. Get out there, bud."

    mic "Oh, right. I'm on it."

    "Michael prepares several mugs of draft beer, loads them onto a tray, and heads out to the floor. All the while, he pays only minimal attention to his task, still smitten by the young singer."

    # Michael Leaves

    hide michael_older_happy

    can "He reminds me of a story my father would tell me."

    wan "I know the story you mean. All too well."

    can "I'm sorry, I didn't mean to-"

    wan "No, it's alright."

    # Michael Returns
    show michael_older_happy at left
    
    hide candace_std_happy
    
    show candace_std_happy at right

    "Michael returns from his waiting duties. Candace gives him a good long stare, and he blushes again."

    can "I know she's pretty, but please do try to pay attention to our patrons, okay?"

    mic "Yes, ma'am. I mean, uh, no - uh…"

    "Candace laughs the way her father used to sometimes laugh - with her entire body, hands on her stomach and leaning back."

    "Michael turns away from his boss, and back to the singer."
    
    hide michael_older_happy    
    
    hide candace_std_happy
    with Pause(.5)

    # BG - Bar Stage
    # Sprite - Rosa
    scene stage 
    show rosa_happy

    "The young performer begins the last verse of her song."

    ros "I remember one night, in the drizzling rain, around my heart I felt an aching pain, fare thee well, my honey, fare thee well."

    "The song's end is met with a quiet, yet suitable applause."
    
    hide rosa_happy
    
    with Pause(.5)

    # BG - Bar Proper
    
    # Sprites - Candace, Michael
    
    scene bar_night 
    
    show candace_std_happy at right
    
    show michael_older_happy at left

    "I feel reminiscent about my similar experience in the very same bar thirty-five years prior, and smile in spite of myself. I propose an idea to the young man across the bar."

    wan "Why don't you buy her a drink after she finishes her set?"

    mic "That's ridiculous. I can't do that! I don't even know her."

    can "And how could asking possibly hurt? Besides, you don't need to know her to become friends."

    mic "I'm nothing more than a stranger to her though…"

    can "Ha! Now {i}that{/i} is ridiculous. As my father would say, strangers are just friends you haven't met yet."

    mic "But what if-"

    wan "Mike, you can make excuses till the sun comes up and you're blue in the face. Or you can ask the lady to have a drink with you."

    "Michael stops his protesting and considers the words his companions have shared with him."

    "For a moment, he looks as though he plans to ignore the advice he has received; however, one quick glance at Candace and I confirm that no is not an option."

    mic "I guess you guys aren't giving me a choice, huh?"

    can "Absolutely not! Now then-"

    can "Let's talk strategy!"

    "Candace and I share a laugh while Michael looks on, terrified at the prospect of whatever scheme Candace has in store."
    
    stop music fadeout 1.0
    
    hide candace_std_happy
    
    hide michael_older_happy
    
    with Pause(.5)
    
    jump scene10
