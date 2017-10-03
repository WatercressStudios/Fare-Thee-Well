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
    
    "The girl gazes at the expectant faces all around her."
    
    "A hush falls over the crowd as she leans into the microphone, and her face betrays not a single emotion but pure wonder."
    
    "It's almost as if she's somewhere else, remembering better times, preparing to sing to herself in a world that stood still, hanging off her every word."
    
    "The young woman starts to sing, and the the meager audience is immediately captivated."
    
    "She begins softly, her voice barely above a whisper."
    
    play music "music/Emmeline's Ballad Rework.mp3" fadein 1.0
    #queue music "music/Emmeline's Ballad - Loop.ogg"
        
    voice "C-9-1.mp3" #Rosa (Tiana Camacho)
    ros "Come over the hills, my bonnie Irish lass..."
    voice "C-9-2.mp3" #Rosa (Tiana Camacho)
    ros "Come over the hills to your darling..."
    voice "C-9-3.mp3" #Rosa (Tiana Camacho)
    ros "You choose the road, love, and I'll make the vow..."
    voice "C-9-4.mp3" #Rosa (Tiana Camacho)
    ros "And I'll be your true love forever."
    
    "Her voice is beautiful and wraps around the dark air of the old bar."
    "I knew this song. I knew it well."
    "Though I've heard it sung better before, I admit."
    
    voice "C-9-5.mp3" #Rosa (Tiana Camacho)
    ros "Red is the rose that in yonder garden grows.."
    voice "C-9-6.mp3" #Rosa (Tiana Camacho)
    ros "Fair is the lily of the valley..."
    voice "C-9-7.mp3" #Rosa (Tiana Camacho)
    ros "Clear is the water that flows from the Boyne..."
    voice "C-9-8.mp3" #Rosa (Tiana Camacho)
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

    "Across the bar stand the current employees of The Hearth and Home, Candace and Michael, the latter having taken the job his mother once held to help pay for his education."

    "Candace and I are having a lovely conversation, but Michael's unwavering attention is set on the young performer."

    voice "C-9-9.mp3" #Candace (Victoria Wong)
    can "Hey, Michael?"

    "Candace tries to grab her employee's attention, but has little success."

    voice "C-9-10.mp3" #Candace (Victoria Wong)
    can "Mike? Hello in there?"

    hide candace_std_happy
    
    show candace_std_sad
    
    play music "music/Written to Memory - Intro.ogg" fadein 1.0
    queue music "music/Written to Memory - Loop.ogg"
    
    "Candace gives a defeated sigh, and waves a hand in front of Michael's face, jolting him back to reality."

    voice "C-9-11.mp3" #Michael (Reece Bridger)
    mic "Oh, uh, sorry Candace. What did you need?"

    hide candace_std_sad

    show candace_std_happy

    "Candace laughs at the young man. She's clearly embarrassed him, so it's no surprise that his face has become several shades redder than some of the wines behind the bar."

    voice "C-9-12.mp3" #Candace (Victoria Wong)
    can "Table four was waving you down for refills. Get out there, bud."

    voice "C-9-13.mp3" #Michael (Reece Bridger)
    mic "Oh, right. I'm on it."

    "Michael prepares several mugs of draft beer, loads them onto a tray, and heads out to the floor. All the while, he pays only minimal attention to his task, still smitten by the young singer."

    # Michael Leaves

    hide michael_older_happy

    voice "C-9-14.mp3" #Candace (Victoria Wong)
    can "He reminds me of a story my father would tell me."

    voice "C-9-15.mp3" #Wayfarer (Terrance Drye)
    wan "I know the story you mean. All too well."

    voice "C-9-16.mp3" #Candace (Victoria Wong)
    can "I'm sorry, I didn't mean to-"

    voice "C-9-17.mp3" #Wayfarer (Terrance Drye)
    wan "No, it's alright."

    # Michael Returns
    show michael_older_happy at left
    
    hide candace_std_happy
    
    show candace_std_happy at right

    "Michael returns from his waiting duties. Candace gives him a good long stare, and he blushes again."

    voice "C-9-18.mp3" #Candace (Victoria Wong)
    can "I know she's pretty, but please do try to pay attention to our patrons, okay?"

    voice "C-9-19.mp3" #Michael (Reece Bridger)
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

    voice "C-9-20.mp3" #Rosa (Tiana Camacho)
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

    voice "C-9-21.mp3" #Wayfarer (Terrance Drye)
    wan "Why don't you buy her a drink after she finishes her set?"

    voice "C-9-22.mp3" #Michael (Reece Bridger)
    mic "That's ridiculous. I can't do that! I don't even know her."

    voice "C-9-23.mp3" #Candace (Victoria Wong)
    can "And how could asking possibly hurt? Besides, you don't need to know her to become friends."

    voice "C-9-24.mp3" #Michael (Reece Bridger)
    mic "I'm nothing more than a stranger to her though…"

    voice "C-9-25.mp3" #Candace (Victoria Wong)
    can "Ha! Now {i}that{/i} is ridiculous. As my father would say, strangers are just friends you haven't met yet."

    voice "C-9-26.mp3" #Michael (Reece Bridger)
    mic "But what if-"

    voice "C-9-27.mp3" #Wayfarer (Terrance Drye)
    wan "Mike, you can make excuses till the sun comes up and you're blue in the face. Or you can ask the lady to have a drink with you."

    "Michael stops his protesting and considers the words his companions have shared with him."

    "For a moment, he looks as though he plans to ignore the advice he has received; however, one quick glance at Candace and I confirm that no is not an option."

    voice "C-9-28.mp3" #Michael (Reece Bridger)
    mic "I guess you guys aren't giving me a choice, huh?"

    voice "C-9-29.mp3" #Candace (Victoria Wong)
    can "Absolutely not! Now then-"

    voice "C-9-30.mp3" #Candace (Victoria Wong)
    can "Let's talk strategy!"

    "Candace and I share a laugh while Michael looks on, terrified at the prospect of whatever scheme Candace has in store."
    
    stop music fadeout 1.0
    
    hide candace_std_happy
    
    hide michael_older_happy
    
    with Pause(.5)
    
    jump scene10
