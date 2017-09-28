label scene5:
    
    stop music
    
    "We talk on and on, long into the night."

    "We tell stories. Learn about each other. Come to understand everything there is to understand."

    "Still, I don't tell her my secret."

    "But the conversation brims with life anyway."

    "I've not spoken like this to someone in a long time."

    "I've not felt this way about someone in a long time."

    "The night is long and full of joy. We keep each other's company, talking until we're the only ones left in the bar."

    "Under the cover of the winter storm, under the dim bar lights, under the drowsy spell of insomnia, we talk, and talk, and talk until we can talk no more."
    
    scene bar_night with fade
    
    play music "music/Written To Memory - Intro.ogg" fadein 1.0 loop
    queue music "music/Written To Memory - Loop.ogg"
    
    show emmeline_young_happy at right
    
    show bartender_young at left
    
    voice "C-5-1.mp3" #Bartender (Andrew Boa)
    ten "Holy hell, you two have been sitting here and talking the whole night long. The bar's closing now. You're going to have to head on out."

    voice "C-5-2.mp3" #Emmeline (Hayley Nelson)
    emm "I'm sorry sir, I hope we weren't a bother."

    voice "C-5-3.mp3" #Bartender (Andrew Boa)
    ten "You're fine, young lady. But you should have this young man escort you home. You've had a long night."

    voice "C-5-4.mp3" #Emmeline (Hayley Nelson)
    emm "But I'm not drunk. I can speak perfectly fine, see?"

    voice "C-5-5.mp3" #Bartender (Andrew Boa)
    ten "Yes, and it's unnerving considering how much you've had to drink."

    "The bartender turns to me and gives me a wise, slow nod."

    voice "C-5-6.mp3" #Wayfarer (Terrance Drye)
    wan "I'll get her home safe."
    
    hide bartender_young  
    
    hide emmeline_young_happy
    with Pause(.5)

    stop music fadeout 1.0

    scene black with fade
    
    play music "music/Snowy Night - Intro.ogg" fadein 1.0 loop
    queue music "music/Snowy Night - Loop.ogg"
    
    "The snow has finally stopped, leaving behind a sleepy town draped in white. The snow is thick, cold, soft like the stuff of dreams."

    "It feels like the ground itself is sleeping, drifting in time and space and frozen in winter silence."

    "Dormant like a slumbering beast waiting to awaken in the snowmelt, its heart stilled by the seething cold."

    "Like Emmeline and I are the only two waking people on the face of the entire earth."

    show emmeline_young_happy

    "Emmeline grins at me smugly."
    
    voice "C-5-7.mp3" #Emmeline (Hayley Nelson)
    emm "My knight in shining armor. Are you going to escort me home and protect me from all the evil monsters?"

    "I refuse to play into her game."

    voice "C-5-8.mp3" #Wayfarer (Terrance Drye)
    wan "Yes, I swear to always safeguard you from the evils that plague the town of Cedar, Maine: subzero temperatures, and poorly paved roads."

    hide emmeline_young_happy

    show emmeline_young_disgust

    voice "C-5-9.mp3" #Emmeline (Hayley Nelson)
    emm "They really are so poorly paved."

    voice "C-5-10.mp3" #Wayfarer (Terrance Drye)
    wan "Yes, I've noticed. Your motel is across the bridge, right?"

    voice "C-5-11.mp3" #Emmeline (Hayley Nelson)
    emm "My castle is, yes."

    voice "C-5-12.mp3" #Wayfarer (Terrance Drye)
    wan "Right. Let's go on ahead."
    
    hide emmeline_young_disgust
    with Pause(.5)

    scene black with fade

    "And so we were off."

    "Together we strolled in the cold, huddling close to each other for warmth. Thankfully the walk wasn't too long."

    "We talk all the way to Emmeline's motel, despite having done nothing but for hours already at the bar."

    scene cedar_night with fade

    voice "C-5-13.mp3" #Wayfarer (Terrance Drye)
    wan "By the way, Emmeline..."

    show emmeline_young_happy

    voice "C-5-14.mp3" #Emmeline (Hayley Nelson)
    emm "Yeah, what is it?"

    voice "C-5-15.mp3" #Wayfarer (Terrance Drye)
    wan "I was wondering if you knew what the meaning of that song you sang tonight was. The first one, that is."

    voice "C-5-16.mp3" #Emmeline (Hayley Nelson)
    emm "What, Loch Lomond?"

    voice "C-5-17.mp3" #Wayfarer (Terrance Drye)
    wan "That's the one."
    
    voice "C-5-18.mp3" #Emmeline (Hayley Nelson)
    emm "It's Scottish, that's all I know. My mother taught it to me, just like her mother taught it to her. She taught me a lot of the folk music I know, really."
    
    voice "C-5-19.mp3" #Emmeline (Hayley Nelson)
    emm "I was never as big into the heritage as she was."

    voice "C-5-20.mp3" #Emmeline (Hayley Nelson)
    emm "But to answer your question, no. I guess I don't know what it's about. I just sing the words."

    voice "C-5-21.mp3" #Wayfarer (Terrance Drye)
    wan "A folk singer who doesn't know what her songs are about?"

    voice "C-5-22.mp3" #Emmeline (Hayley Nelson)
    emm "I like the songs. I love how they sound. I just don't know the traditional meanings behind each and every one of them."

    voice "C-5-23.mp3" #Wayfarer (Terrance Drye)
    wan "I suppose that's fair."

    voice "C-5-24.mp3" #Emmeline (Hayley Nelson)
    emm "But Loch Lomond, right? Isn't that about... two people traveling down different roads?"

    voice "C-5-25.mp3" #Wayfarer (Terrance Drye)
    wan "At surface value, yes. It all comes back to Scottish tradition."
    
    voice "C-5-26.mp3" #Wayfarer (Terrance Drye)
    wan "It is believed that when a Scot dies while abroad, their soul will walk the earth to return to the mother country, so that the deceased may rest in their homeland."

    hide emmeline_young_happy
    
    show emmeline_young_sad

    voice "C-5-27.mp3" #Wayfarer (Terrance Drye)
    wan "The road that these wandering spirits use to return to Scotland is called the low road — as mentioned in the song."
         
    voice "C-5-28.mp3" #Wayfarer (Terrance Drye)
    wan "The regular, corporeal roads that living people like you and I use are the high roads."

    voice "C-5-29.mp3" #Wayfarer (Terrance Drye)
    wan "The high road belongs to the living; the low road, to the dead. That belief is what the song centers around."

    voice "C-5-30.mp3" #Emmeline (Hayley Nelson)
    emm "That's... a bit depressing, don't you think?"

    voice "C-5-31.mp3" #Wayfarer (Terrance Drye)
    wan "Quite the contrary. Think about what the lyrics are saying. You sing from the perspective of a Scot who has died while traveling in a foreign land."

    voice "C-5-32.mp3" #Wayfarer (Terrance Drye)
    wan "You lament that, although the passage of time has taken your friends and your lover away from you, you will finally be able to end your journey and return to your home."
    
    voice "C-5-33.mp3" #Wayfarer (Terrance Drye)
    wan "Where you can finally rest in peace."

    hide emmeline_young_sad

    show emmeline_young_angry

    voice "C-5-34.mp3" #Emmeline (Hayley Nelson)
    emm "..."

    voice "C-5-35.mp3" #Emmeline (Hayley Nelson)
    emm "I don't know, that's still very depressing to me."

    voice "C-5-36.mp3" #Wayfarer (Terrance Drye)
    wan "I don't think so. I think it's bittersweet. The journey of the singer has come to an end, but now that it's over, they can return to where they belong."

    voice "C-5-37.mp3" #Wayfarer (Terrance Drye)
    wan "...I don't know. Personally, I love the song."

    voice "C-5-38.mp3" #Wayfarer (Terrance Drye)
    wan "Sometimes I feel like I take solace in it."

    voice "C-5-39.mp3" #Emmeline (Hayley Nelson)
    emm "You find comfort in a song that tells you you're going to die?"

    voice "C-5-40.mp3" #Wayfarer (Terrance Drye)
    wan "I do. We all die, and every death is an ending, but what the song tells me is this: when my time comes, it will be when I have done all I can in my life."
    
    voice "C-5-41.mp3" #Wayfarer (Terrance Drye)
    wan "I will have found what I was searching for, and I will have brought it home with me."

    voice "C-5-42.mp3" #Wayfarer (Terrance Drye)
    wan "It tells me that it will be my end. Not that I'll be stuck like I am, unchanging, constantly moving, always searching."
    
    voice "C-5-43.mp3" #Wayfarer (Terrance Drye)
    wan "This person I am right now is in constant flux, and the days of my life are numbered with a clear beginning and a fateful end."

    voice "C-5-44.mp3" #Wayfarer (Terrance Drye)
    wan "I don't see any problem in that."

    voice "C-5-45.mp3" #Wayfarer (Terrance Drye)
    wan "In fact, considering neither of us have slept all night..."

    voice "C-5-46.mp3" #Wayfarer (Terrance Drye)
    wan "...some rest sounds like exactly what we need right now."

    "Emmeline goes quiet, and she takes in everything I say."

    voice "C-5-47.mp3" #Emmeline (Hayley Nelson)
    emm "..."
    
    hide emmeline_young_angry

    show emmeline_young_happy

    voice "C-5-48.mp3" #Emmeline (Hayley Nelson)
    emm "Yeah, I suppose you're right."
    
    hide emmeline_young_happy
    with Pause(.5)

    scene black with fade

    voice "C-5-49.mp3" #Emmeline (Hayley Nelson)
    emm "We could both use some rest."

    voice "C-5-50.mp3" #Emmeline (Hayley Nelson)
    emm "..."
    
    voice "C-5-51.mp3" #Emmeline (Hayley Nelson)
    emm "..."

    voice "C-5-52.mp3" #Emmeline (Hayley Nelson)
    emm "..."

    voice "C-5-53.mp3" #Emmeline (Hayley Nelson)
    emm "You know, maybe not."

    scene cedar_night with fade
    
    "Just before we reach the motel, Emmeline stops me in my tracks. She points off to the side of the path, where a small park lies unlit in the snow."

    hide emmeline_young_happy
    
    show emmeline_young_sad

    voice "C-5-54.mp3" #Emmeline (Hayley Nelson)
    emm "...Hey."

    voice "C-5-55.mp3" #Wayfarer (Terrance Drye)
    wan "Hm? Is something wrong?"

    voice "C-5-56.mp3" #Emmeline (Hayley Nelson)
    emm "No..."

    "She's acting incredibly meek. Did I say something I shouldn't have?"

    voice "C-5-57.mp3" #Emmeline (Hayley Nelson)
    emm "..."

    voice "C-5-58.mp3" #Emmeline (Hayley Nelson)
    emm "There's a cute little park here where I come to sit sometimes. It's on top of a big hill and if you're seated on the benches, you can watch the sunrise and sunset from here."

    voice "C-5-59.mp3" #Emmeline (Hayley Nelson)
    emm "It's beautiful."

    voice "C-5-60.mp3" #Emmeline (Hayley Nelson)
    emm "...I'd like to sit and watch the sunrise here. With you."

    voice "C-5-61.mp3" #Emmeline (Hayley Nelson)
    emm "...If you'd want to do that."

    "She... wants to watch the sunrise with me?"

    voice "C-5-62.mp3" #Wayfarer (Terrance Drye)
    wan "Emmeline, it's late. We should really get you to your room."

    "Emmeline points to the sky. It does look like the sun is about to rise. Violet and pink hues are starting to show in the sky, shining in faint ripples in between the clouds."

    hide emmeline_young_sad
    
    show emmeline_young_happy

    voice "C-5-63.mp3" #Emmeline (Hayley Nelson)
    emm "See, we might as well just stay outside the whole night."
    
    "She laughs softly."

    voice "C-5-64.mp3" #Emmeline (Hayley Nelson)
    emm "It looks like we just did, anyway."
    
    stop music fadeout 1.0
    
    "She's right. It had completely gone unnoticed, but we really have spent the whole night together. A new day was about to dawn."

    "I had forgotten how quickly time could pass when you're with a certain kind of person."

    "When you're with someone like Emmeline."

    voice "C-5-65.mp3" #Wayfarer (Terrance Drye)
    wan "You're right. Looks like we stayed up the whole night together."

    "I chuckle."

    voice "C-5-66.mp3" #Wayfarer (Terrance Drye)
    wan "...We are horribly irresponsible."

    "Emmeline laughs more."

    voice "C-5-67.mp3" #Emmeline (Hayley Nelson)
    emm "Just a little bit."
    
    hide emmeline_young_happy
    
    jump scene6
