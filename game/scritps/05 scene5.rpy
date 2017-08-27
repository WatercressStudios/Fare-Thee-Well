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
    
    ten "Holy hell, you two have been sitting here and talking the whole night long. The bar's closing now. You're going to have to head on out."

    emm "I'm sorry sir, I hope we weren't a bother."

    ten "You're fine, young lady. But you should have this young man escort you home. You've had a long night."

    emm "But I'm not drunk. I can speak perfectly fine, see?"

    ten "Yes, and it's unnerving considering how much you've had to drink."

    "The bartender turns to me and gives me a wise, slow nod."

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
    
    emm "My knight in shining armor. Are you going to escort me home and protect me from all the evil monsters?"

    "I refuse to play into her game."

    wan "Yes, I swear to always safeguard you from the evils that plague the town of Cedar, Maine: subzero temperatures, and poorly paved roads."

    hide emmeline_young_happy

    show emmeline_young_disgust

    emm "They really are so poorly paved."

    wan "Yes, I've noticed. Your motel is across the bridge, right?"

    emm "My castle is, yes."

    wan "Right. Let's go on ahead."
    
    hide emmeline_young_disgust
    with Pause(.5)

    scene black with fade

    "And so we were off."

    "Together we strolled in the cold, huddling close to each other for warmth. Thankfully the walk wasn't too long."

    "We talk all the way to Emmeline's motel, despite having done nothing but for hours already at the bar."

    scene cedar_night with fade

    wan "By the way, Emmeline..."

    show emmeline_young_happy

    emm "Yeah, what is it?"

    wan "I was wondering if you knew what the meaning of that song you sang tonight was. The first one, that is."

    emm "What, Loch Lomond?"

    wan "That's the one."
    
    emm "It's Scottish, that's all I know. My mother taught it to me, just like her mother taught it to her. She taught me a lot of the folk music I know, really."
    
    emm "I was never as big into the heritage as she was."

    emm "But to answer your question, no. I guess I don't know what it's about. I just sing the words."

    wan "A folk singer who doesn't know what her songs are about?"

    emm "I like the songs. I love how they sound. I just don't know the traditional meanings behind each and every one of them."

    wan "I suppose that's fair."

    emm "But Loch Lomond, right? Isn't that about... two people traveling down different roads?"

    wan "At surface value, yes. It all comes back to Scottish tradition."
    
    wan "It is believed that when a Scot dies while abroad, their soul will walk the earth to return to the mother country, so that the deceased may rest in their homeland."

    hide emmeline_young_happy
    
    show emmeline_young_sad

    wan "The road that these wandering spirits use to return to Scotland is called the low road — as mentioned in the song."
         
    wan "The regular, corporeal roads that living people like you and I use are the high roads."

    wan "The high road belongs to the living; the low road, to the dead. That belief is what the song centers around."

    emm "That's... a bit depressing, don't you think?"

    wan "Quite the contrary. Think about what the lyrics are saying. You sing from the perspective of a Scot who has died while traveling in a foreign land."

    wan "You lament that, although the passage of time has taken your friends and your lover away from you, you will finally be able to end your journey and return to your home."
    
    wan "Where you can finally rest in peace."

    hide emmeline_young_sad

    show emmeline_young_angry

    emm "..."

    emm "I don't know, that's still very depressing to me."

    wan "I don't think so. I think it's bittersweet. The journey of the singer has come to an end, but now that it's over, they can return to where they belong."

    wan "...I don't know. Personally, I love the song."

    wan "Sometimes I feel like I take solace in it."

    emm "You find comfort in a song that tells you you're going to die?"

    wan "I do. We all die, and every death is an ending, but what the song tells me is this: when my time comes, it will be when I have done all I can in my life."
    
    wan "I will have found what I was searching for, and I will have brought it home with me."

    wan "It tells me that it will be my end. Not that I'll be stuck like I am, unchanging, constantly moving, always searching."
    
    wan "This person I am right now is in constant flux, and the days of my life are numbered with a clear beginning and a fateful end."

    wan "I don't see any problem in that."

    wan "In fact, considering neither of us have slept all night..."

    wan "...some rest sounds like exactly what we need right now."

    "Emmeline goes quiet, and she takes in everything I say."

    emm "..."
    
    hide emmeline_young_angry

    show emmeline_young_happy

    emm "Yeah, I suppose you're right."
    
    hide emmeline_young_happy
    with Pause(.5)

    scene black with fade

    emm "We could both use some rest."

    emm "..."
    
    emm "..."

    emm "..."

    emm "You know, maybe not."

    scene cedar_night with fade
    
    "Just before we reach the motel, Emmeline stops me in my tracks. She points off to the side of the path, where a small park lies unlit in the snow."

    hide emmeline_young_happy
    
    show emmeline_young_sad

    emm "...Hey."

    wan "Hm? Is something wrong?"

    emm "No..."

    "She's acting incredibly meek. Did I say something I shouldn't have?"

    emm "..."

    emm "There's a cute little park here where I come to sit sometimes. It's on top of a big hill and if you're seated on the benches, you can watch the sunrise and sunset from here."

    emm "It's beautiful."

    emm "...I'd like to sit and watch the sunrise here. With you."

    emm "...If you'd want to do that."

    "She... wants to watch the sunrise with me?"

    wan "Emmeline, it's late. We should really get you to your room."

    "Emmeline points to the sky. It does look like the sun is about to rise. Violet and pink hues are starting to show in the sky, shining in faint ripples in between the clouds."

    hide emmeline_young_sad
    
    show emmeline_young_happy

    emm "See, we might as well just stay outside the whole night."
    
    "She laughs softly."

    emm "It looks like we just did, anyway."
    
    stop music fadeout 1.0
    
    "She's right. It had completely gone unnoticed, but we really have spent the whole night together. A new day was about to dawn."

    "I had forgotten how quickly time could pass when you're with a certain kind of person."

    "When you're with someone like Emmeline."

    wan "You're right. Looks like we stayed up the whole night together."

    "I chuckle."

    wan "...We are horribly irresponsible."

    "Emmeline laughs more."

    emm "Just a little bit."
    
    hide emmeline_young_happy
    
    jump scene6
