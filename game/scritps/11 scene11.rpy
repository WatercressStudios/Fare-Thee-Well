label scene11:
    
    # BG ­ Bar Proper

    # Sprites ­ Michael, Rosa, Candace
 
    scene bar_night

    show candace_std_happy at right
    
    show rosa_happy
    
    show michael_older_happy at left
    
    play music "music/Departure.ogg" fadein 1.0
       
    "Hours pass, and it's clear that we've all reached our limit. The clock behind the bar reads three-thirty­six."

    ros "My goodness, I hadn't realized how late — well, early — it's gotten. I really should be going."

    "Rosa stands and puts on her coat."

    ros "Thank you all for a wonderful evening. I'm truly grateful."

    mic "Rosa, would you mind if I walked you back to your motel?"

    "Candace sneaks a wink and a thumbs­up in my direction. I can't help but grin."

    ros "Well, okay. That's very nice of you to offer."

    "As the two prepare to leave, Candace begins to clean up while I lean back in my chair and stretch my tired bones."

    # Candace Leaves
    
    hide candace_std_happy

    mic "Hey Rosa, could you just wait by the door? I'll be there in just a minute."

    ros "Sure."

    # Rosa Leaves
    
    hide rosa_happy
    
    hide michael_older_happy
    
    show michael_older_happy

    "Michael, now standing in front of me alone, turns to me."

    mic "I just wanted to thank you. Tonight has been one of the most memorable nights of my life, and it's all thanks to your encouragement."
    
    wan "There's no need to thank me. We all had a good time."

    "I think it's time I left Cedar. I've spent more time in this little town than I'd intended to. It's the first time I ever came back somewhere."

    "But now, it's time I move on. Life will go on here, just as it always has. My journey is far from finished. This place has taught me a lot, and I'd like to think I've given something back."

    "Though no other place will ever quite fill the gap Cedar will doubtlessly leave in my life, I chose to make Cedar a part of me, and I wouldn't trade that for anything."

    mic "Maybe I don't need to thank you, but let me anyway. You've always been a good friend to me; let me do the same for you."

    "Michael extends his hand to me, and I take it in mine. We exchange a handshake, meaningful to each of us in different ways."

    mic "Thank you."

    "Goodbye, Michael."

    #Michael Leaves

    hide michael_older_happy

    "I take a long look around the cozy bar I've become so familiar with."

    "I see the tables and the booths where Candace's loyal patrons gather after a long day's work."

    "I see the bar, where I first met Candace, and her father before her."

    # BG ­ Bar Stage
    
    scene stage

    "I see the stage, where I first saw Emmeline all those years ago ­ the same stage that Rosa just performed on a few hours ago."

    # BG ­ Bar Proper
    
    scene bar_night

    "I close my eyes and breath in the familiar scents of pine, fire, and alcohol."

    "I will surely miss Cedar. I'll miss The Hearth and Home. I'll miss Candace, Michael, and now Rosa. I'll miss Emmeline."

    "I will miss them all, but I will never forget them."

    "I stand and walk over to the coat rack, which sits beside the door. My coat is now hanging alone."

    "After putting my coat on, I start out the door, but am quickly halted by the length of a broomstick being thrust in front of me."

    # Candace Enters
    
    show candace_std_happy

    hide candace_std_happy
    
    show candace_std_sad

    can "I know what you're about to do. I never expected you'd stay forever."

    can "About two hours ago, I figured this would be your last night in Cedar."

    "Candace looks very serious when compared to her normal, more gleeful, demeanor."
    
    can "Now, after seeing you just a moment ago, I'm certain."

    wan "It's just... time I moved on, Candace."

    can "I'm not going to argue that, I'm not going to stop you."

    wan "What is it then?"

    hide candace_std_sad
    
    show candace_std_happy

    "She cracks a slight smile, but gives nothing away."

    can "Before you go, there's something you need to see."

    wan "Well, what is it?"
    
    stop music fadeout 1.0
    
    can "Come with me."

    "Candace takes me by the arm and leads me behind the bar, through a door, and down a flight of stairs into the wine cellar."

    "She reaches to an empty section of the wine rack, and produces a large sealed envelope."

    can "There's a chair over there. Take as much time as you need."

    "She hands me the envelope and walks over to the door."

    "Candace turns back to me. She looks sad for a brief moment, but then smiles again."

    can "It's been fun. Thank you."

    "Without another word, she turns once more, closing the door behind her."

    hide candace_std_happy

    "I sit down in Candace's chair and look at the envelope in my hands."

    "I run my hand across its smooth surface, wondering what this is."

    "Carefully, I tear open the envelope at its seal."

    "Inside are three smaller envelopes, each marked with a date, 1967, 1987, and 2002."

    "I start with the envelope labeled 1967. Inside is a letter, handwritten."

    "The handwriting is excellent and unmistakably feminine."

    # Letter 1967
    
    nvl clear
    
    play music "music/Lullaby for Cedar, Maine - Intro.ogg" fadein 1.0
    queue music "music/Lullaby for Cedar, Maine - Loop.ogg"
    
    n "Hello, stranger,"

    n "Two nights ago, you swooped into my life. You shared with me the best night of my life, and then you were gone, with more mystery than your arrival."

    n "For the few hours we spent together, all seemed to be right in the world. All my cares had gone away. It was truly blissful. And then you left so suddenly, so abruptly. You never even said goodbye. The magic dissipated instantly. My bliss shattered, leaving only pain and confusion."

    n "That night that we shared, why did we share it? Why did you come into my life, if only to leave hours later? Please don't misunderstand me, dear stranger, I'm not angry. I hold nothing against you. I only wish I could understand why that night happened. I was sure that we were both so happy, but when you left, I began to have doubts."

    n "Had I done something wrong? Were you not happy, as I thought you to be? Of course, thinking back to it now, it all seems a bit silly. It was one night, nothing gained and nothing lost. I'm sure you had your reasons for leaving. I'm glad it happened. I will always remember it."

    n "However, dear stranger, should I ever see you again, though it seems doubtful, please help me to understand what that night meant. I have an aching desire to know."

    n "To be honest, I'm not sure that you will ever read this letter, but I take comfort in knowing that it will not matter if you read it or not. This letter doesn't really mean anything. All I have written here is just the result of one impossible yet undeniable experience. The ramblings of a young woman."

    n "My dear stranger, I wrote all of this to ask for an explanation, but it is now clear to me that I will never receive one. You don't owe it to me, so please don't feel as though you do. I'm happy enough to keep the memories of that night precious without anything more."

    n "So, my stranger, although you never said it yourself, I will say it now."

    n "Goodbye, stranger,"

    n "Emmeline"
    
    nvl clear

    # End letter 1967

    # Letter 1987
    
    nvl clear
    
    stop music fadeout 1.0
    
    "It took me a few moments, but eventually I was able to reach for the second letter, dated 1987."

    "I trace a finger over the now familiar script of Emmeline’s handwriting before reading her words."
    
    play music "music/Snowy Night - Intro.ogg" fadein 1.0
    queue music "music/Snowy Night - Loop.ogg"

    n "Dear Young Man,"
    
    n "I didn’t want to believe it was you. Why would you return, after just leaving me there? But your face was unmistakeable."

    n "I’m sure you’ve heard the expression about not having aged a day. We usually reserve this for women too vain for the truth, or people who’ve recently had plastic surgery."

    n "But in your case, you actually haven’t. You looked exactly the same as you had all those years ago. I hadn’t expected you to return at all, after you’d left me. For a while, I was left to theorize, and I let my imagination run wild. What are you?"

    n "Some kind of alien in human skin? A super advanced machine? A Vampire? And then I remembered one of the things you had talked about: The legend of an eternal wanderer. At the time, I dismissed it as drunken rambling."

    n "Then I saw you, just yesterday. It had been two decades since I’d seen you. Memories fade, but I had my first suspicions when I saw you with Michael. You were helping each other with the audio cables. You might not have even recognized it, but I saw- "

    n "-clear admiration in your eyes. Admiration and more. Envy? I guess if you really are to live forever, you could never again know childlike wonder and curiosity like Michael could. And then I saw your reflection in the window as I was leaving."

    n "I recalled that time when we frolicked around the city in the snow in that moment, and I knew it was you. And now there’s the matter of your cover. If you truly intend to work at the Hearth and Home, then I’ll see you again. Believe me, the-"

    n "- temptation is very real. To reveal you; what you are. But what exactly would that solve? No, it’s better to let bygones be bygones.I’d gain nothing by revealing you, and it would just cause you to leave again. I’m sure you’re used to that process by now."

    n "I considered asking you what occurred in your past travels. Who else did you meet? Anyone famous? How long have you been around? The things usual people would ask someone like you. But honestly, the numbers and faces of the past matter less that what you’ve felt."

    n "I’ve been on the other side of it. Your emotions. I know what you’ve felt. I’ll admit that I hated you for a while, after leaving me on that bench. But now I understand. I forgive you. I hope one day you find a place - or, more likely, a time - that you can flourish in."

    n "With as much loss as I’ve experienced, yours could only be worse. I wish you the best, stranger."

    n "Sincerely, "

    n "Emmeline"
    
    nvl clear
    
    stop music fadeout 1.0

    "She signed her name in that familiar script. I could feel the pressure of tears welling in my eyes now, wishing I could’ve spoken to her. If she knew who I was, then I could have apologized for leaving her all alone on that frosty bench decades ago."

    "Clearly, she had cared for me enough to not reveal who I was to everyone. At the very least, I had the privilege of making that kind of connection - the only kind of connection I could truly ever establish."
    
    # End Letter 1987

    # Letter 2002
    
    play music "music/Theme for a Wanderer - Intro.ogg" fadein 1.0
    queue music "music/Theme for a Wanderer - Loop.ogg"
    
    nvl clear
    
    n "To you,"

    n "I will write to you once again, and this will be my last."
 
    n "I have grown old and feeble, but alas, you are just as I remember you from all those years ago. I'm sorry that you'll never be able to grow old. My life, my son and my family, they have given me joy, just as the night we spent together so long ago did."

    n "Candace has been filling me in on all the fun I've been missing, so I'm grateful to her for that. I trust that she'll deliver these letters to you, when the time is right."

    n "We've had our suspicions for a while now, that you would probably leave Cedar soon. It always makes me sad, thinking of your inevitable departure. It's kind of strange. We've spent so little time together in our lives, but it seems like that time is so very significant."
    
    n "Over all these years, there hasn't been a day that I haven't thought back to the night we first met. I never have been able to understand why, it's just always meant a lot to me."
    
    n "I did recognize you when you came back in '87, though not right away. I'm not really sure why I didn't ever say anything to you. It just never felt like there was a good time to say anything. You had lived twenty more years. I had gotten twenty years older. I got married and had Michael. Looking back, it was for the best that I did not say anything."

    n "It's a strange thing, the connection we seem to have. I would say it is unique, but I can't say for certain whether that is true or not."

    n "The time you were a part of my life was indeed brief, but, without a doubt, that time changed my life. It changed my view of the world, and it changed how I see other people. I'm uncertain, but I think these changes were for the better, so I thank you."

    n "I also want to thank you for leaving me that night. I've enjoyed my normal life; I see now that this is all I ever could have wanted. You saw that it was what I wanted long before I ever even wanted it. You showed me something special, and you gave me the chance to live the life that was mine."

    n "My dearest Wanderer, we aren't very good at goodbyes, are we? But this will indeed be our last. But I have grandchildren that I soon hope to meet, and you have a long road ahead of you, so I'll keep it brief."

    n "I want you to remember me as who I was and, to you, will now always be."

    n "So goodbye, my dear Wanderer."

    n "Travel safe. Travel far and long and wide."

    n "And maybe, in another life ­ in a different time ­ we will meet again."

    nvl clear
    
    stop music fadeout 1.0
    
    # End Letter 2002

    scene black with fade
    
    "I am speechless."
    "I sit for a while, stirring in my emotions."
    "I feel..."
    "Empty. But in a good way."
    "At an end. But in the best way."
    "I feel.."
    "...complete."
    
    scene bar_night
    
    show candace_std_sad
    
    "After I walk out of the closet, I come across Candace, alone. She's the only one left. The bar is empty, silent and calm like some place out of a dream."
    
    can "..."
    can "Finished already?"
    
    wan "..."
    wan "Yeah."
    
    can "..."
    can "And you're leaving now?"
    
    wan "Candace..."
    
    "She begins to cry."
    
    wan "You know I have to do."
    
    "She wipes at her eyes with her dirtied hands."
    
    can "I know."
    can "...I know."
    
    "There is silence for a moment before Candace draws in for a hug."
    "She embraces me tightly, her trickling tears soaking into the shoulder of my coat."
    "She trembles, but only a little."
    
    can "I don't want you to go."
    
    wan "I have to."
    
    can "You can't leave. We're all still here."
    
    wan "I'm sorry."
    
    can "I..."
    can "..."
    
    "I pull myself away."
    
    wan "Goodbye, Candace. I'll miss you."
    wan "I'll miss you, and everyone else."
    wan "And this dark, dusty old bar..."
    wan "...and this sleepy town in the snow."
    wan "I'll miss it."
    wan "I'll miss you all."
    wan "...I will."
    
    can "..."
    can "Will you remember us?"
    
    wan "Always."
    
    can "..."
    
    show candace_std_happy
    
    can "...Thank you."
    can "..."
    can "You know, you were like family to us."
    can "To my dad, to me, to the bar, to the town."
    can "..You really were."
    can "I want you to remember that, okay?"
    
    scene black with dissolve
    
    "I give Candace one last smile before I turn for the door."
    "She goes back to sweeping, not wanting to watch me leave."
    "She takes a deep breath."
    "Tears drip from her eyes onto the floor."
    
    wan "Okay."
    
    play music "music/Wind-Mark_DiAngelo-1940285615.wav"
    
    scene cedar_night with dissolve
    
    "Once outside, I take a final stroll around the town."
    "Cedar, Maine."
    "At first glance, it all seems so..."
    "Asleep."
    "Like it's not alive but only lays there, in a state of constant rest."
    "But that couldn't be more wrong."
    "This town was more alive than any other I've seen."
    "The white snow resting on the frozen ground glowed like the stuff of dreams."
    "I've fallen in love, over the years, with this town..."
    "...with this dream."
    
    scene black with dissolve 
    
    "But it's time to wake up."
    
    scene winterwoods with dissolve
    
    "I walk away into wilderness as the sun rises over the trees."

    "I vanish like a ghost from a dream, wiping tears from my eyes."

    "All I leave behind are footprints in the snow that are soon swept away by winter wind."
    
    nvl clear
    
    n "Of all the money that ere I had, I spent it in good company."
    n "And of all the harm that ere I've done, alas was done to none but me."
    n "And all I've done for want of wit, to memory now I cannot recall."
    n "So fill me to the parting glass. Goodnight and joy be with you all."
    
    nvl clear
    
    n "So fill to me that parting glass,"
    n "And drink a health whate'er befalls."
    n "Then gently rise and softly call,"
    n "Goodnight and joy be with you all."
    
    nvl clear

    n "Of all the comrades that ere I had, they're sorry for my going away,"
    n "And of all the sweethearts that ere I had , they wish me one more day to stay,"
    n "But since it falls unto my lot that I should rise while you should not,"
    n "I will gently rise and I'll softly call, Goodnight and joy be with you all."
    
    nvl clear

    n "Fare Thee Well — The story of a lonely man."

    n "A wanderer, a wayfarer, a stranger,"

    n "And the sleepy town he left in the snow,"

    n "One winter night."
    
    nvl clear
    
    jump credits
