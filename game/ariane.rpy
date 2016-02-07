#This document and associated images Copyright 2013 by ArianeB.com 

label call_ariane1:
        $ abaseball = 0
        scene lastdate
        show story1title at centerlow
        stop music fadeout 5
        $ renpy.pause(4.0)
        hide story1title
        if not persistent.ldhotdate and not persistent.ldeverything:
            play sound "voice/Desc_Last_week_you_went_over_to_Arianes_house.mp3" fadein 0
            "Last week you went over to Ariane's house for the evening."
            stop sound fadeout 0
            play sound "voice/Desc_It_was_a_nice_pleasant_evening.mp3" fadein 0
            "It was a nice pleasant evening, she has a pool and a hot tub,\n so the two of you spent the evening having fun at her place."
            stop sound fadeout 0
            scene phone
            play sound "voice/Desc_You_call_her_up.mp3" fadein 0
            "You call her up."
            stop sound fadeout 0
            show ariphone at phonepos1 with moveinright
            $ menuplaceX = 0.1
            $ menuplaceY = 0.5
            menu:
                ap "Hello?"
                "Hey Ariane, it's me, [persistent.playername].":
                    ap "{i}Oh, hi there [persistent.playername].  Just caught me eating breakfast.{/i}"
                "Hey ya sweet cheeks. What's a fine lady doing this Saturday Morning?":
                    ap "{i}Hey Sexy Dude.  Just caught me eating breakfast.{/i}"
                "Hey Ariane, it's me, [persistent.playername], sorry for calling so early.":
                    play sound "voice/Ariane_Dont_Worry_about_it.mp3" fadein 0
                    ap "{i}Don't worry about it [persistent.playername]. I'm in my kitchen eating cereal.  Got up to go to the gym.{/i}"
                    stop sound fadeout 0
                "Hey beautiful, whatcha wearing?":
                    scene black
                    card "You a hear a click, then nothing.\n\nGuess she did not recognize you."
                    jump morning_ending
            show kitchenback at center0 with moveinleft
            scene kitchenback
            show ariphone at phonepos1 with moveinright
            play sound "voice/Player_I_thought_we_had_a_great_time.mp3" fadein 0
            y "I thought we had a great time on our date, and was wondering if you were free tonight? \nMaybe Dinner and a movie?"
            stop sound fadeout 0
            play sound "voice/Ariane_Sure_Id_love_to_see_you_again.mp3" fadein 0
            ap "{i}Sure, I'd love to see you again, and yes, I am free tonight.{/i}"
            stop sound fadeout 0
            play sound "voice/Player_Excellent.mp3" fadein 0
            y "Excellent!"
            stop sound fadeout 0
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            play sound "voice/Ariane_I_want_to_do_something_different.mp3" fadein 0
            menu:
                ap "{i}I want to do something different this time, though.{/i}"
                "Different is cool with me. What do you have in mind?":
                    play sound "voice/Ariane_I_want_to_go_out_on_a_formal_date.mp3" fadein 0
                    ap "{i}I want to go out on a formal date.{/i}"
                    stop sound fadeout 0
                "We could hang out at my place if you want.":
                    play sound "voice/Player_I_dont_have_a_pool.mp3" fadein 0
                    y "I don't have a pool or hot tub like you do, and most of my stuff is still in boxes..."
                    stop sound fadeout 0
                    ap "{i}Maybe another time, I was thinking we should go on a formal date.{/i}"
                "I was looking forward to hanging out at your place, again.": 
                    ap "{i}I know, but I'd like to go out... like really out.\nA real formal date.{/i}"
            play sound "voice/Player_How_formal_are_we_talking.mp3" fadein 0
            y "How formal are we talking?"
            stop sound fadeout 0
            show suit at suitpos with moveinleft
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            play sound "voice/Ariane_You_in_a_suit.mp3" fadein 0
            menu:
                 ap "{i}You in a suit. Me in a nice dress. Out at a really nice restaurant.\nMaybe dancing afterward. A fancy night out.{/i}"
                 "A suit in the middle of summer?":
                     hide suit with moveoutleft
                     ap "{i}Sorry, but I've made up my mind.{/i}"
                     show suit at suitpos with moveinleft
                     y "Very well a suit it is."
                 "You want a suit? You got it!":
                     play sound "voice/Ariane_Great_looking_forward_to_seeing_you.mp3" fadein 0
                     ap "Great, looking forward to seeing you all gussied up."
                     stop sound fadeout 0
                 "How about swimsuits instead? We can do the fancy night out later.":
                     ap "Not looking for a repeat of last week, I want a fancy night out for a change."    
                     y "Very well a suit it is."
            play sound "voice/Player_So_when_and_where_shall_we_meet.mp3" fadein 0
            y "So, when and where shall we meet?"
            stop sound fadeout 0
            if persistent.ldrestaurant:
                ap "{i}Remember the restaurant we went to last week?  Let's meet there at 7 o'clock.  OK?{/i}"
                show restaurantintro at center0 with moveintop
                scene restaurantintro
                show ariphone at phonepos1 with moveinbottom
                y "Sounds perfect."
                jump ariane
            else:
                play sound "voice/Ariane_How_about_the_Cafe_da_Silva.mp3" fadein 0
                ap "{i}How about the Cafe da Silva. It's next door to the Art Museum downtown.{/i}"
                stop sound fadeout 0
                show restaurantintro at center0 with moveintop
                scene restaurantintro
                show ariphone at phonepos1 with moveinbottom
                play sound "voice/Player_Sounds_easy_enough_to_find.mp3" fadein 0
                y "Sounds easy enough to find."
                stop sound fadeout 0
                play sound "voice/Ariane_Why_dont_we_meet_around_7.mp3" fadein 0
                ap "{i}Why don't we meet around 7? Is that OK?{/i}"
                stop sound fadeout 0
                play sound "voice/Player_Sounds_perfect.mp3" fadein 0
                y "Sounds perfect."
                stop sound fadeout 0
                jump ariane
        if persistent.ldhotdate and not persistent.ldeverything:
            "Last week you went over to Ariane's house for the evening."
            scene arianepast2
            "It was a hot and crazy night, she was really into you and you ended up making love."
            "You have been thinking about her all week, but didn't want to seem desperate by calling too soon."
            scene phone
            "You call her up."
            show ariphone at phonepos1 with moveinright
            y "Hey Ariane, it's me, [persistent.playername]."
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                ap "{i}It's about time you called, [persistent.playername].  I figure you were one of those guys that fucks a girl then never calls.{/i}"
                "I'm so sorry it has taken me so long to call.":
                    ap "{i}That's all you can offer is an apology?{/i}"
                    y "Why don't I make it up to you tonight? Maybe Dinner and a movie?"
                    show ariphone at phonepos2 with move
                    ap "{i}Then you should be willing to prove it. We can go out on one condition.{/i}"
                    y "OK, what do you want?"
                "No, I'm not one of those guys.  I have been thinking of you all week actually.":
                    y "Why don't I make it up to you tonight? Maybe Dinner and a movie?"
                    ap "{i}Do you think I'm one of those girls that waits around for my \"man\" to make a booty call?{/i}"
                    y "No, ... and that is not what this is."
                    show ariphone at phonepos2 with move
                    ap "{i}Then you should be willing to prove it. We can go out on one condition.{/i}"
                    y "OK, what do you want?"
                "I'll be honest. Yes, I want to come by and fuck you.":
                    ap "{i}Thanks for the honesty, but I'm not one of those girls that \nwaits around for my \"man\" to make a booty call.{/i}"
                    ap "{i}I'm not looking for anything serious right now either, \nbut I would hope we could have a relationship on more than sex.{/i}"
                    $ menuplaceX = 0.1
                    $ menuplaceY = 0.6
                    menu:
                        "You have to consider your next words carefully, or your relationship may be over."
                        "I'm sorry for the misunderstanding, I got the impression you enjoyed our night of passion.":
                            ap "{i}I did, I enjoyed sex with YOU, emphasis on the YOU.\nYou seemed to enjoy SEX with me, emphasis on the SEX.{/i}"
                            y "That's not true!, I enjoyed the YOU part too."
                            y "Give me a chance to prove it? Maybe Dinner and a movie tonight?"
                            show ariphone at phonepos2 with move
                            ap "{i}All right, you deserve another chance. We can go out on one condition.{/i}"
                            y "OK, what do you want?"
                        "You are right, we could have something special here, and it should not be about casual sex.":
                            ap "{i}I'm glad you agree.  Are you willing to prove it?{/i}"
                            y "Yes I am.  Let's go out tonight, and I will."
                            show ariphone at phonepos2 with move
                            ap "{i}All right, you deserve another chance. We can go out on one condition.{/i}"
                            y "OK, what do you want?"
            ap "{i}On our last date, I let you decide what we did on our date.\nAll I did was offer some advice.{/i}"
            ap "{i}It was my way of getting to know you better, and see what kind of guy you are.{/i}"
            ap "{i}The result was I got to know you very intimately.{/i}"
            y "We both got to know {i}each other{/i} intimately."
            ap "{i}I'll go out with you again, but I get to decide what we do this time.{/i}"
            ap "{i}If you know me intimately, then you'll have to trust me. \nTonight, you can give suggestions, but I am the decider.{/i}"
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                "Do you accept Ariane's terms?"
                "Can't we come to a mutual agreement on what to do tonight?":
                    ap "Aha! I figured as much. You're the type that doesn't like to follow."
                    ap "I'm perfectly OK with mutual agreements, I was just testing you. ... and you failed."
                    ap "Call me in another week, and we can try this again."
                    jump morning_ending
                "Fair is fair, you decide tonight.  Where are you taking me?":    
                    ap "{i}Great, well last week was a casual get together at my place.\nThis week is a fancy night on the town.{/i}"
                    y "Sounds Great, when and where shall we meet?"
                    if persistent.ldrestaurant:
                        ap "{i}Remember the restaurant we went to last week?  Let's meet there at 7 o'clock.  OK?{/i}"
                        show restaurantintro at center0 with moveintop
                        scene restaurantintro
                        show ariphone at phonepos1 with moveinbottom
                    else:
                        play sound "voice/Ariane_How_about_the_Cafe_da_Silva.mp3" fadein 0
                        ap "{i}How about the Cafe da Silva. It's next door to the Art Museum downtown.{/i}"
                        stop sound fadeout 0
                        show restaurantintro at center0 with moveintop
                        scene restaurantintro
                        show ariphone at phonepos1 with moveinbottom
                        play sound "voice/Player_Sounds_easy_enough_to_find.mp3" fadein 0
                        y "Sounds easy enough to find."
                        stop sound fadeout 0
                        play sound "voice/Ariane_Why_dont_we_meet_around_7.mp3" fadein 0
                        ap "{i}Why don't we meet around 7? Is that OK?{/i}"
                        stop sound fadeout 0
                    play sound "voice/Player_Sounds_perfect.mp3" fadein 0
                    y "Sounds perfect."
                    stop sound fadeout 0
                    $ menuplaceX = 0.2
                    $ menuplaceY = 0.7
                    menu:
                        ap "{i}And it's a fancy night out, so suit and tie ARE required.{/i}"
                        "A suit in the middle of summer?":
                            show suit at suitpos with moveinleft
                            ap "{i}Sorry, but I've made up my mind.{/i}"
                            y "Very well a suit it is."
                        "You want a suit? You got it!":
                            show suit at suitpos with moveinleft
                            ap "See you tonight then."
                        "How about birthday suits instead?":
                            ap "Not looking for a repeat of last week, I want a fancy night out for a change." 
                            show suit at suitpos with moveinleft  
                            y "You are right. Very well a suit it is."
            jump ariane
        if persistent.ldeverything:
            "You have been out on a few dates with Ariane."
            "So far, she is the only girl you have dated in this town,\nbut the two of you have had a lot of fun together."
            scene arianepast2
            "Some of these dates have turned into sleepovers,\nthough when it happens, sleep is actually rare."
            scene phone
            "You call her up."
            show ariphone at phonepos1 with moveinright
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                ap "Hello?"
                "Hey Ariane, it's me, [persistent.playername].":
                    ap "{i}Oh, hi there [persistent.playername].  Just caught me eating breakfast.{/i}"
                "Hey ya sweet cheeks. What's a fine lady doing this Saturday Morning?":
                    ap "{i}Hey Sexy Dude.  Just caught me eating breakfast.{/i}"
                "Hey Ariane, it's me, [persistent.playername], sorry for calling so early.":
                    play sound "voice/Ariane_Dont_Worry_about_it.mp3" fadein 0
                    ap "{i}Don't worry about it [persistent.playername]. I'm in my kitchen eating cereal.  Got up to go to the gym.{/i}"
                    stop sound fadeout 0
                "Hey beautiful, whatcha wearing?":
                    ap "{i}I'm naked of course. Is this a Gallup poll?{/i}"
                    hide ariphone with moveoutright
                    show ariphonewide at phonepos1 with moveinright
                    y "No, silly, it's me [persistent.playername]."
                    ap "{i}I know, it was a joke. So I'm just grabbing some breakfast, whats up?{/i}"
            show kitchenback at center0 with moveinleft
            scene kitchenback
            show ariphone at phonepos1 with moveinright
            y "I was wondering if you were free tonight? \nMaybe Dinner and a movie?"
            ap "{i}A movie?  Huh, I don't think we have done that one yet?{/i}"
            y "Well I am running out of original ideas."
            ap "{i}Let's save the movie date for when we are completely out of ideas.{/i}"
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            play sound "voice/Ariane_I_want_to_do_something_different.mp3" fadein 0
            menu:
                ap "{i}I want to go out tonight, but let's do something different.{/i}"
                "Different is cool with me. What do you have in mind?":
                    play sound "voice/Ariane_I_want_to_go_out_on_a_formal_date.mp3" fadein 0
                    ap "{i}I want to go out on a formal date.{/i}"
                    stop sound fadeout 0
                "We could hang out at my place if you want.":
                    play sound "voice/Player_I_dont_have_a_pool.mp3" fadein 0
                    y "I don't have a pool or hot tub like you do, and most of my stuff is still in boxes..."
                    stop sound fadeout 0
                    ap "{i}Sounds worse than the movie idea.\nNo, I was thinking we should go on a formal date.{/i}"
            play sound "voice/Player_How_formal_are_we_talking.mp3" fadein 0
            y "How formal are we talking?"
            stop sound fadeout 0
            show suit at suitpos with moveinleft
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            play sound "voice/Ariane_You_in_a_suit.mp3" fadein 0
            menu:
                 ap "{i}You in a suit. Me in a nice dress. Out at a really nice restaurant.\nMaybe dancing afterward. A fancy night out.{/i}"
                 "A suit in the middle of summer?":
                     hide suit with moveoutleft
                     ap "{i}Sorry, but I've made up my mind.{/i}"
                     show suit at suitpos with moveinleft
                     y "Very well a suit it is."
                 "You want a suit? You got it!":
                     play sound "voice/Ariane_Great_looking_forward_to_seeing_you.mp3" fadein 0
                     ap "Great, looking forward to seeing you all gussied up."
                     stop sound fadeout 0
                 "How about swimsuits instead? We can do the fancy night out later.":
                     ap "Not looking for a repeat of last week, I want a fancy night out for a change."    
                     y "Very well a suit it is."
            play sound "voice/Player_So_when_and_where_shall_we_meet.mp3" fadein 0
            y "So, when and where shall we meet?"
            stop sound fadeout 0
            ap "{i}Remember the restaurant we went to downtown?  Let's meet there at 7 o'clock.  OK?{/i}"
            show restaurantintro at center0 with moveintop
            scene restaurantintro
            show ariphone at phonepos1 with moveinbottom
            y "Sounds perfect."

label ariane:
        scene black
        play ambient "restaurant.ogg" fadein 1 fadeout 2
        card "A typical Saturday passes... until 7PM arrives."
        scene bar2
        $ renpy.pause(2.0)
        $ menuplaceX = 0.1
        $ menuplaceY = 0.7
        menu:
            "You arrive at the restaurant, and Ariane waves to you, she is standing by the bar."
            "Good evening Ariane, I love your dress.":
                play sound "voice/Ariane_Thank_you_very_much_You_are_so_charming.mp3" fadein 0
                ap "Thank you very much, just got it today.\nYou look very nice in a suit yourself."
                stop sound fadeout 0
                y "Well, thank you. Shall we go to dinner?"
            "Hi Ariane, is that a new hairstyle?":
                ap "Yes, I went to the salon today, do you like it?"
                y "Yes, it looks wonderful. Shall we have dinner?"
            "Hello Ariane, you look absolutely fabulous.":
                jump skiptobar    
        ap "Let's sit down and have a drink, first.  The restaurant overbooked and we have to wait a while."
        y "Yeah, but we have reservations." 
        ap "Well some big party came in around 6:30 apparently, and took all of the available seats. \nThey are just being served now."
        $ menuplaceX = 0.1
        $ menuplaceY = 0.7
        menu:
            ap "We probably won't see a table until they are done."
            "Let's sit at the bar and wait then.":
                ap "OK, order me some white wine then."
            "Maybe we should try someplace else nearby.":
                ap "Where else?  The night club has a concert tonight and it's closed except for ticket holders\nand we are too way overdressed for The Cantina. Let's just wait it out."  
            "Let's drive someplace else then.":
                ap "All the other nice restaurants are probably all booked,\nthe only place we could get a table would be the Drive-N-Dine."
                y "Fast food? Only if we are desperate. Let's just wait at the bar."
                ap "Agreed."
        y "Well you look absolutely fabulous this evening Ariane, in case I forget to mention it."
label skiptobar:        
        play sound "voice/Ariane_Thank_you_very_much_You_are_so_charming.mp3" fadein 0
        ap "Thank you very much. You are so charming.\nAnd you look dashingly handsome tonight as well."
        stop sound fadeout 0
        play sound "voice/Ariane_giggles.mp3" fadein 0
        "Ariane giggles"
        stop sound fadeout 0
        play sound "voice/Player_Whats_so_funny.mp3" fadein 0
        y "What's so funny?"
        stop sound fadeout 0
        play sound "voice/Ariane_Us_actually_fancy_and_shit.mp3" fadein 0
        ap "Us actually...\nPut us in some formal clothes and we start talking all fancy, and shit."
        stop sound fadeout 0
        scene bar3
        stop ambient fadeout 5
        play sound "voice/Desc_The_restaurant_bar_is_getting_crowded_now.mp3" fadein 0
        "The restaurant bar is getting crowded now. A guy took the last free bar stool \nsitting between Ariane and a pretty blonde two seats over."
        stop sound fadeout 0
        $ menuplaceX = 0.1
        $ menuplaceY = 0.8
        menu:
            ap "So how has your day been?"
            "{i}Talk about your day{/i}":
                $ abaseball = 1
                y "I mostly spent it at home.  It was quiet except people kept calling me."
                ap "Oh yeah, what about?"
                y "Oh just wanting me to do stuff, go to a baseball game, that kind of stuff. \nI was more interested in being with you."
                ap " You could've gone to the baseball game tonight, and came here instead?"
                y "Why do you sound so surprised?"
                scene barbb
                "Ariane points to a TV behind the bar, the game is on, \nthe score is tied 9 all in the 12th inning."
                ap "Looks like it would've been a good game to go to."
                scene bar3
                y "It does, but then I would not have made it to see you, I'd still be at the game."
                ap "Thanks, but you shouldn't have to stop doing fun stuff for my sake."
                y "Oh, it's not like that.  I just wasn't that interested. I'd rather be here with you."
                ap "Ah, that's so sweet of you to say."
                scene barbb
                $ renpy.pause(3.0)
                ap "You're watching the game now, aren't you?"
                scene bar3
                y "Huh, what?\nOh, sorry."
            "{i}Ask about her day{/i}":
                play sound "voice/Player_Nothing_special_did_you_do_anything_fun.mp3" fadein 0
                y "Nothing special, did you do anything fun?"
                stop sound fadeout 0
                if persistent.ldrebecca:
                    ap "I went to the gym this morning, and ran into Rebecca, again."
                    y "Oh yeah?"
                    ap "She asked me out too, but I told her I already had a date with you tonight."
                else:
                    play sound "voice/Ariane_I_went_to_gym_this_morning.mp3" fadein 0
                    ap "I went to the gym this morning, for a gymnastics class."
                    stop sound fadeout 0
                    play sound "voice/Player_I_rember_you_mentioning_that_you_did_gymnastics.mp3" fadein 0
                    y "I remember you mentioning that you did gymnastics in college."
                    stop sound fadeout 0
                    play sound "voice/Ariane_Yeah_no_more_competitions.mp3" fadein 0
                    ap "Yeah, no more competitions, but I still do it for fun."
                    stop sound fadeout 0
                play sound "voice/Ariane_After_that_I_went_and_got_my_hair_done.mp3" fadein 0
                ap "After that I went and got my hair done, ate lunch, did some shopping, then came here."
                stop sound fadeout 0
                y "You didn't go swimming? Seems like a good day for it."
                ap "No, no swimming. I just got my hair done, didn't want to get it wet."
                y "Oh, of course. Sounds like you spent the day preparing for our date."
                ap "Hey, it's not very often a girl gets a fancy night out."
        scene bar4
        "The blonde girl two seats down from Ariane looks upset.\nThe guy sitting between them is talking to her, trying to calm her down."
        scene bar5
        "The girl then throws her drink at the guy,\nhe manages to back away in time,\nnearly falling off his stool..."
        if not "wine" in persistent.verlist:
            $ persistent.verlist.append("wine")
        if persistent.soundtrack == True:
            play song "dancingmice3.ogg" fadein 0.1
        "... and the majority of the drink hits Ariane instead, ruining her violet top."
        scene bar6
        if not persistent.ldstrip and not persistent.ldeverything:
            ap "(to Blonde girl) WHAT THE HELL DO YOU THINK YOU ARE DOING!!"
            bg "Oh I am so sorry, I wasn't aiming for you."
            ap "Lucky for you, Wonderbra, I learned proper drink throwing as a toddler.\nHere,  let me show you."
            if not "bar" in persistent.arilist:
                $ persistent.arilist.append("bar")
            scene bar7
            "Before Ariane could grab her glass of champagne, the bartender intervened."
            bar "(to Blonde Girl) Please pay for your drinks and leave...  You too sir (to man in the middle)."
            scene bar8
            bar "I apologize, this kind of thing rarely happens. Can I get you anything?... on the house."
            ap "Soda water would be helpful."
        if persistent.ldstrip and not persistent.ldstripwon and not persistent.ldeverything:
            ap "(to Blonde girl) WHAT THE HELL DO YOU THINK YOU ARE DOING!!"
            bg "Oh I am so sorry, Betty, I wasn't aiming for you."
            ap "You shouldn't be aiming for ANYBODY, especially in a crowded bar!"
            ap "Now, my top is ruined!"
            bg "I am so sorry again, Betty, I'll pay for your drinks."
            ap "Why do you keep calling me Betty?"
            bg "That's what you told me your name was, remember?"
            "Ariane suddenly remembered."
            ap "Get the FUCK AWAY from me BITCH!"
            scene bar7
            "The bartender saw what happened, grabs a roll of paper towels and hands them to Ariane."
            bar "(to Blonde Girl) Please pay for your drinks and leave...  You too sir (to man in the middle)."
            scene bar8
            bar "I apologize, this kind of thing rarely happens. Can I get you anything?... on the house."
            ap "Soda water would be helpful."
        if persistent.ldeverything or persistent.ldstripwon:
            ap "(to Blonde girl) What the hell did you do that for, Stacy?"
            if not "ariane" in persistent.verlist:
                $ persistent.verlist.append("ariane")
            st "Oh I am so sorry, Ariane, I wasn't aiming for you."
            ap "Now, my top is ruined!"
            st "I am so sorry again, Ariane, I'll get you a new top."
            ap "Everyone says you have been acting crazy since that magazine was released. Just get over it already."
            st "And, you are right, I'm sorry I did the photos. I did them in hopes\nof gaining some respect, and I feel they have undermined my authority instead."
            ap "Stacy, the pictorial DID gain you some respect, but then YOU\nundermined that respect by acting belligerent to EVERYBODY."
            st "I know we only met recently, but I have never seen you this brutally honest before."
            ap "It's my nature, people PISS ME OFF, and I start telling the TRUTH,\nno matter how BRUTALLY HONEST it gets."
            if not "brutal" in persistent.arilist:
                $ persistent.arilist.append("brutal")
            st "Good to know."
            st "Once again, Ariane, sorry about the top.  I {i}will{/i} get you a new one."  
            st "Can you stop being mad at me now?"
            ap "Page 38 makes your butt look big."
            st "I'll take that as a no.  Here is some soda water. \nI will leave you now. I'll see you on Monday."
        scene bar9    
        "She uses the soda water to try and keep the stain from setting, but it is just making the top wetter."
        if not persistent.ldeverything and abaseball == 1:
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                ap "Let's go... back to my place so I can change."
                "It's not that big of a stain, and you still look fabulous.":
                    ap "No, I need to change.  I think I have a T-Shirt in my SUV, wait here and I'll go grab it."
                    y "OK, I'll wait here for you."
                    scene black
                    stop song fadeout 1
                    card "Ariane never comes back, you give up after a while."
                    jump evening_ending
                "All right, Let's go.":
                    scene freeway1
                    stop song fadeout 1
                    card "You get in the SUV with Ariane, and you drive back to her place.\nYou don't talk much in the car.  Let Ariane calm down.\n\nAt least there is a beautiful sunset to watch. The sun sets late in the summer."
                "Let's just sit and watch the rest of the baseball game.":
                    ap "No thanks, I'm not staying here."
                    scene black
                    stop song fadeout 1
                    card "Your team wins, 11-10 in the 14th inning, but Ariane is gone.\n\nTHE END"
                    jump evening_ending
        elif persistent.ldeverything:
            ap "Let's go... back to my place so I can change."
            y "All right, Let's go."
            scene freeway1
            card "You get in the SUV with Ariane, and you drive back to her place.\nYou don't talk much in the car.  Let Ariane calm down.\n\nAt least there is a beautiful sunset to watch. The sun sets late in the summer."
        else:    
            $ menuplaceX = 0.1
            $ menuplaceY = 0.8
            menu:
                ap "Let's go... back to my place so I can change."
                "It's not that big of a stain, and you still look fabulous.":
                    ap "No, I need to change.  I think I have a T-Shirt in my SUV, wait here and I'll go grab it."
                    y "OK, I'll wait here for you."
                    scene black
                    stop song fadeout 1
                    card "Ariane never comes back, you give up after a while."
                    jump evening_ending
                "All right, Let's go.":
                    scene freeway1
                    stop song fadeout 1
                    card "You get in the SUV with Ariane, and you drive back to her place.\nYou don't talk much in the car.  Let Ariane calm down.\n\nAt least there is a beautiful sunset to watch. The sun sets late in the summer."
        if not persistent.ldhotdate and not persistent.ldeverything:
            scene arihouse1
            ap "It'll be just a few minutes. Take  a seat on the couch"
            scene arihouse2
            "Ariane goes in to her bedroom, you remain outside, you hear her muttering to herself. {i}\"Dammit nothing\"{/i}"
            ap "(yelling from the bedroom) If it is OK with you, I'm declaring an end to our fancy date."
            y "(yelling back) Fine with me, no formal night out. I am removing my jacket and tie right now."
            if persistent.ldmtnphotos:
                ap "Hey, you know those pictures we took with my phone last week?  I got prints made.\nThe pictures are on the dining table if you want to take a look."
                scene arihouse3
                "You go to the table, there are the pictures you took of Ariane."
                y "Hey this isn't all of them, where are the pictures of me?"
                ap "In a safe place. A girl has got to keep some incriminating pictures around\nin case she needs to extort some money."
                "You are not sure what to say."
                ap "I'm joking of course.  I posted them online, on a gay porn site I found."
                ap "Joking again of course."
            scene arihouse5    
            if not persistent.ldstrip:
                a "You know what? I think that blonde bitch at the bar did us a favor.\nWe don't need no fancy night out, Let's just have a little fun tonight."
            if persistent.ldstrip and not persistent.ldstripwon:
                a "You know what? I think that strip club bitch did us a favor.\nWe don't need no fancy night out, Let's just have a little fun tonight."
            if persistent.ldstrip and persistent.ldstripwon:
                a "You know what? Stacy did us a favor.\nWe don't need no fancy night out, Let's just have a little fun tonight."
                a "I'm still going to make her buy me a new dress, though."
            y "I agree, Let's turn a bad experience into a reason to party."
            a "Great, I'm starved.\nLet's eat."
        if persistent.ldeverything:
            scene arihouse1
            ap "Well so much for the formal night out. Have a seat on the couch."
            scene arihouse2
            ap "(yelling from the bedroom) I guess it is time for plan B... movie night."
            y "(yelling back from the living room) Great, I'll get out of this suit if you don't mind."
            ap "Hey, you know those pictures we took with my phone that one time?" 
            y "Was that the park fountain photo shoot, or the one up in the mountains?"
            ap "The one in the mountains,  I got prints made.\nThe pictures are on the dining table if you want to take a look."
            scene arihouse3
            "You go to the table, there are the pictures you took of Ariane."
            y "Hey this isn't all of them, where are the pictures of me?"
            ap "In a safe place. A girl has got to keep some incriminating pictures around\nin case she needs to extort some money."
            "You are not sure what to say."
            ap "I'm joking of course.  I posted them online, on a gay porn site I found."
            ap "Joking again of course."
            scene arihouse5    
            a "You know what? Stacy did us a favor.\nWe don't need no fancy night out, Let's just have a little fun tonight."
            a "I'm still going to make her buy me a new dress, though."
            a "And, I'm not going to tell her I got it on sale either."
            y "What do you say we turn this bad experience into a reason to party.\nShall we go to the movies then?."
            a "I'm starved. Let's eat first."
        if persistent.ldhotdate and not persistent.ldeverything:
            scene arihouse4
            ap "So our formal night out did not work out so good."
            $ menuplaceX = 0.1
            $ menuplaceY = 0.8
            menu:
                ap "I just feel so bummed right now."
                "Why was it so important to you?":
                    ap "Well when I get upset I get brutally honest, so watch out."
                    if not "brutal" in persistent.arilist:
                        $ persistent.arilist.append("brutal")
                    ap "We slept together on the first date, that is not normally me."
                    ap "I figured that if we were serious lovers, it would be better than casual lovers."
                    y "So a fancy night out was a way to form a relationship with me?"
                    ap "Well when you put it that way it sounds kind of stupid."
                    y "How so?"
                    ap "Because I am not relationship material, never have been."
                    y "But you are an amazing woman Ariane, you deserve to be happy."
                    $ menuplaceX = 0.1
                    $ menuplaceY = 0.8
                    menu:
                        ap "Yes, and I am always happier when I am not in a relationship."
                        "I'm sorry you feel that way.":
                            y "I am looking for a relationship, and I think it is sweet that you tried."
                            ap "And now that I realized my mistake, I feel kind of dumb."
                            ap "You and I are incompatible. I have no desire to change who I am, to become what you want."
                            y "You don't need to change, you are perfect as is, you only have to be yourself."
                            ap "The problem is we don't want the same things.\nYou just said you want a relationship, something I don't want."
                            y "In the generic sense of the word, we already have a relationship, it just needs definition."
                            ap "What, like \"fuck buddies\"?"
                            y "How about \"friends with benefits\"?"
                            ap "I don't know, every movie and TV show I have seen about\n\"friends with benefits\" has resulted in disaster."
                            y "Shall we find out?"
                            ap "OK, Let's give it a shot, and see how it goes."
                            scene arisex
                            play sound "sexbed.mp3" fadein 0.1
                            $ renpy.pause(13)
                            stop sound fadeout 1
                            scene arirobe1
                            stop sound fadeout 1
                            ap "Thanks, I'm much more relaxed."
                            y "You're welcome."
                            ap "Here's some cab fare to get you to your car downtown.\nGoodnight!"
                            scene black
                            $ persistent.adatecount += 1
                            if persistent.aending8 == False or persistent.epilogue > 0:
                                $ persistent.aending8 = True
                                show picenda9 at achievepos1 with moveinleft
                                if persistent.story1 == False or persistent.epilogue > 0:
                                    $ persistent.story1 = True
                                    show picenda1 at achievepos2 with moveinleft
                                    $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                                $ achievement_frame("","Fuck Buddies","", xcenter = 0.1, yalign = 0.1)    
                            card "Looks like you and Ariane just became fuck buddies.\nYou are not sure what that means for the future, but it probably won't last.\n\nTHE END"
                            return
                        "I feel the same way.":
                            ap "So we both agree this formal night out was a waste of time."
                            y "Well not a complete waste, you got a great haircut out of it."
                            ap "(laughs) Yes I did.\nSo romance is not the answer."
                            y "We are just not \"formal\" type of people."
                            ap "I'm not interested in a relationship with you,\nand, you're not interested in a relationship with me."
                            y "We are just two people that like to get together and have some fun."
                            ap "We are together tonight to have a good time, so DAMMIT!! LET'S HAVE A GOOD TIME!!!"
                "We should just go out and have some fun.":
                    ap "You know, you are right. We tried and we are just not formal people."
                    y "Couldn't agree more."
                    ap "We are together tonight to have a good time, so DAMMIT!! LET'S HAVE A GOOD TIME!!!"
            scene arihouse1
            ap "I'm going to find something more casual to wear."
            y "Great, I'm taking off this suit and tie."
            scene arihouse5    
            y "By the way, you are still in charge of the evening."
            a "Great, I'm starved.\nLet's eat."
           
        scene dinerdriveup
        if persistent.lddiner or persistent.ldeverything:
            card "You go out again to the Drive-N-Dine. The same scantily clad waitress is there."
        else:
            card "You go to a 50's themed fast food chain called the Drive-N-Dine, \na place famous for its hot waitresses and small waitress uniforms.\n\nThey also serve food there."
        scene dinerorder
        wa "May I take your order?"
        a "I'm really hungry, I'll take the double burger, fries, and a cola."
        wa "And you sir?"
        y "The same"
        wa "Coming right up"
label datediscussion:       
        if persistent.ldeverything:
            jump doneeverything 
        scene dinerwait
        y "So, here we are on our second date."
        a "Yeah, I know, so far nothing like our last date."
        scene dinerserved
        y "What do you remember from our last date?"
        scene dinereat
        if persistent.soundtrack == True:
            play song "comicaltragedy.ogg" fadein 0.1
        show ldpic9 at memory with dissolve
        a "Well Let's see...  You came over to my place.  We talked, and drank some wine."
        
        if persistent.ldname == "generic date":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldfondle1 at memory with dissolve
            a "We made out on the couch"
            y "I remember that part fondly."
            a "Don't you mean \"fondle-ly\""
            show ldrock1 at memory with dissolve
            a "We danced to some music on the boombox"
            show ldbgame1 at memory with dissolve
            a "We played some Parcheesi."
            y "I don't even remember who won."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."

        if persistent.ldname == "downtown diner":
            show lddiner1 at memory with dissolve
            a "We ate here at the Drive-N-Dine."
            y "Hey, I think this place is starting to grow on me."
            show lddowntown1 at memory with dissolve
            a "We took a drive downtown."
            show ldmuseum1 at memory with dissolve
            a "We went to the art museum"
            y "Yes some amazing paintings there."
            show ldpatio1 at memory with dissolve
            a "Then we went home and I put on a bikini."
            show ldswim1 at memory with dissolve
            a "and we went swimming in my pool."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."

        if persistent.ldname == "downtown restaurant":
            show ldrestaurant1 at memory with dissolve
            a "We went to the Cafe Da Silva, and actually got a table."
            y "Yes, I was looking forward to a return trip."
            show ldclub1 at memory with dissolve
            a "We went to Lizard's Nightclub."
            y "You said it was the hottest club in town, so I had to see it for myself."
            show ldpark2 at memory with dissolve
            a "Then we went home and took a walk to the park."
            show ldpark6 at memory with dissolve
            a "and did some gymnastics in the nude."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."

        if persistent.ldname == "quickie date":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldfondle1 at memory with dissolve
            a "We made out on the couch"
            y "I remember that part fondly."
            a "Don't you mean \"fondle-ly\""
            show ldcouch1 at memory with dissolve
            y "That led to sex on the couch."
            a "And that was pretty much all there was to the date."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "It was a short date but the sex was great."
            a "Agreed, we had a nice time."

        if persistent.ldname == "hot tub date":
            show ldpatio1 at memory with dissolve
            a "I put on a bikini."
            y "You look great in a swimsuit, by the way."
            a "Thank you, ... Let's see what else..."
            show ldpicnic1 at memory with dissolve
            a "We had a poolside picnic in our swimsuits."
            show ldswim1 at memory with dissolve
            a "and we went swimming in my pool."
            show ldhottub1 at memory with dissolve
            a "Then we soaked in the hot tub."
            y "Yes, very relaxing."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We had a nice fuck in the hot tub, and then after drying off,\nwe went to the bedroom where we had sex a few more times until we fell asleep."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date."
            
        if persistent.ldname == "skinny dipping":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldpatio1 at memory with dissolve
            a "Then we went home and I put on a bikini."
            show ldswim1 at memory with dissolve
            a "and we went swimming in my pool."
            show ldskinny1 at memory with dissolve
            a "Then we took off our swimsuits."
            y "Wish I had my own pool, I'd always skinny dip, ... it feels very liberating."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We slept together and had sex multiple times all night long, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "out of gas":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show lddrive1 at memory with dissolve
            a "We took a drive into the mountains."
            show lddrive2 at memory with dissolve
            a "We ran out of gas."
            y "I don't think I'll ever live that down will I."
            scene dinerend
            
        if persistent.ldname == "passed out drunk":
            show lddiner1 at memory with dissolve
            a "We ate here at the Drive-N-Dine."
            y "Hey, I think this place is starting to grow on me."
            show ldstore1 at memory with dissolve
            a "We went to the local convenience store for beer."
            show ldbeer1 at memory with dissolve
            a "Then we went back to my place where we drank beer and got naked."
            y "I remeber some naughty touching, too."
            show ldabsinthe at memory with dissolve
            a "So we tried stepping up to the hard stuff."
            y "Yes, this is where things got a little fuzzy."
            show ldabsinthe2 at memory with dissolve
            a "So we drove back to the Drive-N-Dine naked, and invited that waitress to join us."
            y "We did?"
            show ldstore2 at memory with dissolve
            a "Then we went back to the convenience store and invited Jessie along too."
            y "Wow, I have no memory of that."
            show ldabsinthe3 at memory with dissolve
            a "Then the four of us ended up naked in the hot tub making out with each other."
            y "Wait, I would have remembered that."
            scene dinerend
            a "You are right, that didn't happen. You passed out."
            a "After I let you sleep it off on the couch, the next morning, I threw your drunk ass into a taxi."
            
        if persistent.ldname == "beer run":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldrock1 at memory with dissolve
            a "We danced to some music on the boombox"
            show ldstore1 at memory with dissolve
            a "We went to the local convenience."
            show ldstore6 at memory with dissolve
            a "Then we went back to my place where we drank it."
            y "I remeber some naughty touching, too."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "bikini beer run":
            show ldpatio1 at memory with dissolve
            a "I put on a bikini."
            y "You look great in a swimsuit, by the way."
            a "Thank you, ... Let's see what else..."
            show ldpicnic1 at memory with dissolve
            a "We had a poolside picnic in our swimsuits."
            show ldstore1 at memory with dissolve
            a "We went to the local convenience store and met Jessie the store clerk."
            show ldstore5 at memory with dissolve
            y "And, all you were wearing was a small bikini."
            a "I go there all the time in a bikini.  I have my own pool, I swim a lot, \nand sometimes I need stuff at the store, and I'm too lazy to dress."
            show ldbeer1 at memory with dissolve
            a "Then we went back to my place where we drank beer and got naked."
            y "I remeber some naughty touching, too."
            a "But that is as far as it got."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "naked beer run":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldpatio1 at memory with dissolve
            a "I put on a bikini."
            y "You look great in a swimsuit, by the way."
            show ldhottub1 at memory with dissolve
            a "Then we soaked in the hot tub."
            y "And played \"truth or dare\"."
            show ldstore2 at memory with dissolve
            a "Which involved me going to a convenience store completely naked."
            y "You are lucky we were the only ones there, and that Jessie was cool with it\nor you would have ended up in jail."
            a "Jessie talks about how boring work is all the time,\n I thought I would liven it up."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We slept together and had sex multiple times all night long, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "gymnastics":
            show ldpark1 at memory with dissolve
            a "We walked down to the park."
            show ldpark5 at memory with dissolve
            a "I took off my pants and demonstrated some gymnastics skills."
            y "You could be a gymnast, or an exotic dancer."
            a "um, thanks, I think."
            show lddiner1 at memory with dissolve
            a "We ate here at the Drive-N-Dine."
            y "Hey, I think this place is starting to grow on me."
            show ldmuseum1 at memory with dissolve
            a "We went to the art museum"
            y "Yes some amazing paintings there."
            show ldfondle1 at memory with dissolve
            a "We made out on the couch"
            y "I remember that part fondly."
            a "Don't you mean \"fondle-ly\""
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "bikini basketball":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldswim1 at memory with dissolve
            a "I put on a bikini and we went swimming in my pool."
            show ldpark4 at memory with dissolve
            a "We walked down to the park."
            show ldpark8 at memory with dissolve
            a "We played basketball."
            y "Yeah, neither of us are very good at it, it turns out."
            a "Well in my defense, Basketball is not really a good sport to play in a bikini."
            y "But, I enjoyed the way to tried to defend the basket."
            a "You mean by distracting you by flashing my boobs?"
            y "Yeah, that."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "fountain photoshoot":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldpatio1 at memory with dissolve
            a "I put on a bikini and we went swimming in my pool."
            show ldpark3 at memory with dissolve
            a "We walked down to the park."
            show ldpark11 at memory with dissolve
            a "You took photos of me in my bikini in front of the fountain."
            y "Those were on a digital camera too, can you e-mail me some copies?"  
            show ldpark12 at memory with dissolve
            a "I posed nude in some of those photos."
            y "I especially want copies of those, please."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "naked gymnastics":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldclub1 at memory with dissolve
            a "We went to Lizard's Nightclub."
            y "You said it was the hottest club in town, so I had to see it for myself."
            show ldpark2 at memory with dissolve
            a "Then we went home and took a walk to the park."
            show ldpark6 at memory with dissolve
            a "and did some gymnastics in the nude."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We slept together and had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "naked basketball":
            show ldpatio1 at memory with dissolve
            a "I put on a bikini."
            y "You look great in a swimsuit, by the way."
            a "Thank you, ... Let's see what else..."
            show ldpicnic1 at memory with dissolve
            a "We had a poolside picnic in our swimsuits."
            show ldhottub1 at memory with dissolve
            a "Then we soaked in the hot tub."
            y "And played \"truth or dare\"."
            show ldpark9 at memory with dissolve
            a "Which involved shooting freethrows completely naked."
            y "You made me do it too, and I got caught." 
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "romantic date":
            show ldrestaurant1 at memory with dissolve
            a "We went to the Cafe Da Silva, and actually got a table."
            y "Yes, I was looking forward to a return trip."
            show ldclub1 at memory with dissolve
            a "We went to Lizard's Nightclub."
            y "You said it was the hottest club in town, so I had to see it for myself."
            show ldclub2 at memory with dissolve
            a "We got kicked out of Lizard's Nightclub."
            y "Yes, for punching that asshole who grabbed you, he totally deserved it."
            show ldlake1 at memory with dissolve
            a "We went to the lake."
            show ldlake6 at memory with dissolve
            a "We went for a romantic walk on the beach."
            y "Yes it was a beautiful night with the moon glimmering on the waves."
            a "You held my hand, and kissed me."
            y "Wonderful memories"
            show ldlake7 at memory with dissolve
            a "I took off my dress on the beach."
            y "Very wonderful memories."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We went back to my place and had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "lake boating":
            show ldpatio1 at memory with dissolve
            a "I put on a bikini."
            y "You look great in a swimsuit, by the way."
            a "Thank you, ... Let's see what else..."
            show ldpicnic1 at memory with dissolve
            a "We had a poolside picnic in our swimsuits."
            show ldlake1 at memory with dissolve
            a "We went to the lake."
            show ldlake2 at memory with dissolve
            a "We rented a boat."
            y "Kind of late for a boating adventure, but there was a bright moon, so it seemed safe." 
            show ldlake4 at memory with dissolve
            y "And then, the moon set behind the mountains, and we could not see anymore."
            a "Yep, we had to spend the night on the boat."
            y "And we drank all the beer, and the deck was very uncomfortable."
            a "Well there was only room for one of us on the cushioned bench."
            show ldlake5 at memory with dissolve
            y "And you woke me at dawn to drive the boat back to the dock."
            scene dinerend
            a "They would have charged us for the whole day if it wasn't back by 6 AM."
            y "And then back at your place we kissed goodbye on your patio."
            
        if persistent.ldname == "nude skiing":
            show ldrestaurant1 at memory with dissolve
            a "We went to the Cafe Da Silva, and actually got a table."
            y "Yes, I was looking forward to a return trip."
            show ldclub1 at memory with dissolve
            a "We went to Lizard's Nightclub."
            y "You said it was the hottest club in town, so I had to see it for myself."
            show ldclub2 at memory with dissolve
            a "We got kicked out of Lizard's Nightclub."
            y "Yes, for punching that asshole who grabbed you, he totally deserved it."
            show ldlake1 at memory with dissolve
            a "We went to the lake."
            show ldlake2 at memory with dissolve
            a "We rented a boat."
            y "Kind of late for a boating adventure, but there was a bright moon, so it seemed safe." 
            show ldlake3 at memory with dissolve
            a "I went water skiing, but I didn't bring a suit, so I did it naked."
            y "I would have too, but I'm not very good."
            a "That's OK, I love skiing."
            show ldlake4 at memory with dissolve
            y "And then, the moon set behind the mountains, and we could not see anymore."
            a "Yep, we had to spend the night on the boat."
            y "And we drank all the beer, and the deck was very uncomfortable."
            a "Well there was only room for one of us on the cushioned bench."
            show ldlake5 at memory with dissolve
            y "And you woke me at dawn to drive the boat back to the dock."
            scene dinerend
            a "They would have charged us for the whole day if it wasn't back by 6 AM."
            y "And then back at your place we kissed goodbye on your patio."
            
        if persistent.ldname == "walk on the beach":
            show ldpatio1 at memory with dissolve
            a "I put on a bikini."
            y "You look great in a swimsuit, by the way."
            a "Thank you, ... Let's see what else..."
            show ldpicnic1 at memory with dissolve
            a "We had a poolside picnic in our swimsuits."
            show ldlake1 at memory with dissolve
            a "We went to the lake."
            show ldlake6 at memory with dissolve
            a "We took a walk on the beach."
            show ldlake8 at memory with dissolve
            a "I fell in the lake and ruined my dress."
            y "I told you to be careful."
            a "I know, I only blame myself."
            show ldlake9 at memory with dissolve
            y "At least you took it of and wrung it out before it got completely ruined."
            a "You {i}would{/i} remember that, wouldn't you."
            scene dinerend
            a "They would have charged us for the whole day if it wasn't back by 6 AM."
            y "And then back at your place we kissed goodbye on your patio."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We went back to my place and had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "marco polo":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldshopping1 at memory with dissolve
            a "We went shopping."
            show ldrebecca1 at memory with dissolve
            a "You met Rebecca."
            y "Charming girl."
            show ldrebecca2 at memory with dissolve
            a "She took us to a nightclub."
            y "Charming {i}drunk{/i} girl." 
            show ldrebecca3 at memory with dissolve
            a "Then we ended up back at my place."
            show ldrebecca6 at memory with dissolve
            if not "rebnude" in persistent.reblist:
                $ persistent.reblist.append("rebnude")
            a "The three of us ended up skinny dipping in my pool."
            y "In a spirited game of {i}Marco Polo{/i}, with plenty of naughty touching."
            show ldrebecca11 at memory with dissolve
            a "Then Rebecca left us alone together."
            y "She's fun, but she can be a bit too much."
            a "At least she broke the first date tension a bit."
            y "Yes, I felt the date went better after she left."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "met rebecca":
            show lddiner1 at memory with dissolve
            a "We ate here at the Drive-N-Dine."
            y "Hey, I think this place is starting to grow on me."
            show ldshopping1 at memory with dissolve
            a "We went shopping."
            show ldrebecca1 at memory with dissolve
            a "You met Rebecca."
            y "Charming girl."
            show ldrebecca2 at memory with dissolve
            a "She took us to a nightclub."
            y "Charming {i}drunk{/i} girl." 
            show ldrebecca3 at memory with dissolve
            a "Then we ended up back at my place."
            show ldrebecca5 at memory with dissolve
            a "The three of us ended up swimming in my pool. Rebecca and I shared a bikini."
            y "As I recall, Rebecca was cool with swimming nude, and letting you have the whole bikini.\nSo it was very nice of you to let her have your top."
            show ldrebecca10 at memory with dissolve
            a "Then Rebecca left us alone together."
            y "She's fun, but she can be a bit too much."
            a "At least she broke the first date tension a bit."
            y "Yes, I felt the date went better after she left."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "strip club lost":
            show ldrestaurant1 at memory with dissolve
            a "We went to the Cafe Da Silva, and actually got a table."
            y "Yes, I was looking forward to a return trip."
            show ldclub1 at memory with dissolve
            a "We went to Lizard's Nightclub."
            y "You said it was the hottest club in town, so I had to see it for myself."
            show ldrebecca1a at memory with dissolve
            a "You met Rebecca."
            y "Charming girl."
            show ldrebstrip1 at memory with dissolve
            a "She took us to a strip club."
            y "and a completely crazy girl too."
            show ldrebstrip4 at memory with dissolve
            a "Rebecca and I danced at a strip club on amateur night. She got completely nude, I kept my clothes on. We both lost."
            if not "rebnude" in persistent.reblist:
                $ persistent.reblist.append("rebnude")
            show ldrebstrip5 at memory with dissolve
            y "And then you and Rebecca left me there all alone... in a Strip Club... with a wallet full of singles."
            scene dinerend
            
        if persistent.ldname == "strip club won":
            show ldrestaurant1 at memory with dissolve
            a "We went to the Cafe Da Silva, and actually got a table."
            y "Yes, I was looking forward to a return trip."
            show ldclub1 at memory with dissolve
            a "We went to Lizard's Nightclub."
            y "You said it was the hottest club in town, so I had to see it for myself."
            show ldrebecca1a at memory with dissolve
            a "You met Rebecca."
            y "Charming girl."
            show ldrebstrip1 at memory with dissolve
            a "She took us to a strip club."
            y "and a completely crazy girl too."
            show ldrebstrip3 at memory with dissolve
            a "Rebecca and I danced at a strip club on amateur night. We both danced nude on stage, I won and she lost."
            y "I did not think anyone could top the old Tennis Instructor routine.  But you did it.  Congratulations again."
            if not "rebnude" in persistent.reblist:
                $ persistent.reblist.append("rebnude")
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "sleepover":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldshopping1 at memory with dissolve
            a "We went shopping."
            show ldrebecca1 at memory with dissolve
            a "You met Rebecca."
            y "Charming girl."
            show ldrebecca2 at memory with dissolve
            a "She took us to a nightclub."
            y "Charming {i}drunk{/i} girl." 
            show ldrebecca4 at memory with dissolve
            a "Rebecca made herself at home and ran around naked."
            y "She was not the only one as I recall."
            a "Yeah, but it was my house."
            show ldrebecca9 at memory with dissolve
            a "The three of us had a sleep over, but we were all too tired to do more than sleep."
            y "There I was lying naked between two naked women, and I fell right asleep.\n What the hell was in that alcohol you poured us?"
            if not "rebnude" in persistent.reblist:
                $ persistent.reblist.append("rebnude")
            scene dinerend
            
        if persistent.ldname == "dance and lost":
            show lddiner1 at memory with dissolve
            a "We ate here at the Drive-N-Dine."
            y "Hey, I think this place is starting to grow on me."
            show ldstrip1 at memory with dissolve
            a "You took me to a place called Live Cabaret, that turned out to be a strip club."
            y "I'm new in town, I'm not yet familiar with the bad places. to avoid."
            a "Hey, I had never been there either."    
            a "There was an amateur contest going on, and you talked me into participating."
            y "Well $500 is decent money for a few minutes on stage."
            show ldstrip4 at memory with dissolve
            a "True, but you have to win, and despite dancing in front of a room full of strangers, I lost."
            y "I wanted to console you in your loss, but then you left with some other guy.\nYou left me alone in a strip club, with a wallet full of singles. So I did not feel too bad."
            a "At least I kept my clothes on.  Basically, I chickened out."
            y "Hey, it took a lot of courage to even try."
            show ldstrip7 at memory with dissolve
            a "Well I should have stayed with you, the guy I met backstage was a loser, \nand that is why you are here tonight."
            y "Thank you for giving me a second chance."
            scene dinerend
            
        if persistent.ldname == "strip to undies won":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldstrip1 at memory with dissolve
            a "You took me to a place called Live Cabaret, that turned out to be a strip club."
            y "I'm new in town, I'm not yet familiar with the bad places. to avoid."
            a "Hey, I had never been there either."    
            show ldstrip4 at memory with dissolve
            a "There was an amateur contest going on, and you talked me into participating."
            y "Well $500 is decent money for a few minutes on stage."
            show ldstrip5 at memory with dissolve
            a "It was a lot harder than it looked. I danced and stripped down to my underwear in front of an audience to win."
            y "Yeah, but you won, and you totally earned it. You were spectacular for it being your first time and all." 
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "strip nude and won":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldstrip1 at memory with dissolve
            a "You took me to a place called Live Cabaret, that turned out to be a strip club."
            y "I'm new in town, I'm not yet familiar with the bad places. to avoid."
            a "Hey, I had never been there either."    
            show ldstrip3 at memory with dissolve
            a "There was an amateur contest going on, and you talked me into participating."
            y "Well $500 is decent money for a few minutes on stage."
            show ldstrip6 at memory with dissolve
            a "It was a lot harder than it looked. I danced and stripped nude in front of an audience to win."
            y "Yeah, but you won, and you totally earned it. You were spectacular for it being your first time and all." 
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date." 
            
        if persistent.ldname == "makeout interrupted":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldrock1 at memory with dissolve
            a "We danced to some music on the boombox"
            show lddrive1 at memory with dissolve
            a "We took a drive into the mountains."
            show lddrive3 at memory with dissolve
            a "We made out in the car, but got interrupted by another couple."
            y "We could have stayed and given them a show."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "photoshoot":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldrock1 at memory with dissolve
            a "We danced to some music on the boombox"
            show lddrive1 at memory with dissolve
            a "We took a drive into the mountains."
            show lddrive4 at memory with dissolve
            a "We took photos at the scenic view."
            y "Well, more pictures of you than the scenic view.  You are far more interesting."
            show lddrive6 at memory with dissolve
            a "You took photos of my bare ass at the scenic view."
            y "Well I did it first."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We finished the date on my front porch, and you kissed me goodnight."
            y "I thought that was a very nice date."
            a "Agreed, we had a nice time."
            
        if persistent.ldname == "nude photoshoot":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldrock1 at memory with dissolve
            a "We danced to some music on the boombox"
            show lddrive1 at memory with dissolve
            a "We took a drive into the mountains."
            show lddrive4 at memory with dissolve
            a "We took photos at the scenic view."
            y "Well, more pictures of you than the scenic view.  You are far more interesting."
            show lddrive6 at memory with dissolve
            a "You took photos of my bare ass at the scenic view."
            show lddrive7 at memory with dissolve
            a "Then I got completely naked."
            y "You seemed to be having a lot of fun too, until you made me stop."    
            y "Then you talked me into posing nude for you."
            show lddrive8 at memory with dissolve
            a "Yes you were a great sport about it."
            y "Fair is fair, but I have a feeling those naked pictures of me will\nshow up some day if I make you mad."
            a "They may indeed."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date."
            
        if persistent.ldname == "sex in car":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldrock1 at memory with dissolve
            a "We danced to some music on the boombox"
            show lddrive1 at memory with dissolve
            a "We took a drive into the mountains."
            show lddrive4 at memory with dissolve
            a "We took photos at the scenic view."
            y "Well, more pictures of you than the scenic view.  You are far more interesting."
            show lddrive6 at memory with dissolve
            a "You took photos of my bare ass at the scenic view."
            show lddrive7 at memory with dissolve
            a "Then I got completely naked."
            y "You seemed to be having a lot of fun too, until you made me stop."    
            y "Then you talked me into posing nude for you."
            show lddrive8 at memory with dissolve
            a "Yes you were a great sport about it."
            y "Fair is fair, but I have a feeling those naked pictures of me will\nshow up some day if I make you mad."
            a "They may indeed."
            show lddrive9 at memory with dissolve
            a "Then we had sex in the car."
            y "Yes that was crazy,  It felt right at the time, but since then\nI keep thinking what would have happen had another car come by."
            a "They would have slowed down, seen what we were doing, and then immediately would have left."
            a "In fact that is exactly what both cars did."
            y "Really? I did not see any other cars."
            a "That is because your back was to the road. I was facing it."
            y "Damn, how embarrassing."
            scene dinerend
            
        if persistent.ldname == "oral sex":
            show lddinner1 at memory with dissolve
            a "We made ourselves dinner."
            y "You are a great cook, by the way."
            a "Thank you, ... Let's see what else..."
            show ldrock1 at memory with dissolve
            a "We danced to some music on the boombox"
            show lddrive1 at memory with dissolve
            a "We took a drive into the mountains."
            show lddrive4 at memory with dissolve
            a "We took photos at the scenic view."
            y "Well, more pictures of you than the scenic view.  You are far more interesting."
            show lddrive6 at memory with dissolve
            a "You took photos of my bare ass at the scenic view."
            show lddrive7 at memory with dissolve
            a "Then I got completely naked."
            y "You seemed to be having a lot of fun too, until you made me stop."    
            y "Then you talked me into posing nude for you."
            show lddrive8 at memory with dissolve
            a "Yes you were a great sport about it."
            y "Fair is fair, but I have a feeling those naked pictures of me will\nshow up some day if I make you mad."
            a "They may indeed."
            show lddrive9 at memory with dissolve
            a "Then I gave you a blow job."
            y "You definitely know what you are doing down there."
            a "And then you returned the favor."
            y "A gentleman always does."
            scene dinerend
            y "And, do you remember how our date ended?" 
            a "We had sex multiple times, and you left the next morning."
            y "A great night. We did not get much sleep with all the sex.\nI ended up going home and sleeping till about noon."
            a "I spent the day wired on caffeine, reminiscing over the night before. Yes an epic first date."
                
        if persistent.ldhotdate:
                stop song fadeout 3
                a "And, then you left, and didn't call me for over a week."
                y "Hey once again, I am sorry about that."
                y "Work has been a bitch, this week. \nI probably should have called to at least say \"hi\" or something."
                $ menuplaceX = 0.1
                $ menuplaceY = 0.7
                menu:
                    a "You know, if work is going that badly and you need someone to talk to,\n feel free to call me up and rant.  I know it helps ME out sometimes."
                    "Be careful, I may just take you up on that offer.":
                        a "Go ahead... as long as you understand that I may call you up and rant about stuff from time to time too."
                    "No, I could never do that to you.":
                        a "Why not?  If we have are going to have a relationship, we should \nbe able to talk to one another about anything, and not just when we are out on a date."
                        y "So you are OK if I call you and rant about my terrible day at work?"
                        a "Sure, as long as you understand that I may call you up and rant about stuff from time to time too."
                    "You really want to hear about my bad day at work?":   
                        a "Why not?  If we have are going to have a relationship, we should \nbe able to talk to one another about anything, and not just when we are out on a date."
                        y "What kind of relationship do you think we have?"
                        a "If we are going to be lovers, we should also be friends.\nThat means we should be able to talk, about anything."
                y "OK, well this has been a productive discussion.  I'm glad we had this talk."
                a "On that note, Let's go catch a movie.  Then we can sit in the dark and {i}NOT{/i} talk for a couple of hours."
                a "There should be a bunch that start around 8. If we leave soon, we should make it."
                y "Sounds nice, we're done here. ... And to think, {i}we could be still waiting for a table.{/i}"  
                jump tothemovies
        else:
                stop song fadeout 3
                a "And then I waited by the phone for your call, which did not come until this morning."
                y "You really waited by the phone?"
                a "Well I checked my voice mail a few times."
                y "You know, Ariane, YOU could have called ME back."
                a "I didn't think about that, but you are right.\nWhy is it assumed men always get to make the first move?"
                y "Tradition dating back to the cavemen I suppose."
                a "Fuck the cavemen!\nIt's the 21st century. If I want to call you, I'll call you."
                a "Or maybe I'll leave {i}you{/i} hanging for a week."
                y "Then I'll have to call you."
                a "Not until I call you."
                y "Why do I have to wait for you?"
                play sound "vphone.ogg" fadein 0.2
                "Suddenly your phone starts ringing."
                a "Aren't you going to get it?"
                y "I'll let it go to voice mail."
                play sound "vphone.ogg" fadein 0.2
                a "No, you should answer it."
                y "Very well\n(you pick up the phone) Hello?"
                scene dinerphone
                a "Hey [persistent.playername], it's Ariane, what are you doing?"
                y "I'm on a date actually."
                a "Oh yeah, is she pretty?"
                y "Yes, very."
                a "Sounds HOT!"
                a "Well, I won't talk long, I told you I would call first, so this is me calling first."
                y "Great, then it's OK for me to call you and ask you out again sometime?"
                a "Well, you know [persistent.playername], you don't always have to call for a date."
                a "If we are going to be friends, why not call once in a while just to chat?\nTell me about your bad day at work, that kind of thing."
                y "Well I wasn't sure if you would like me calling just to rant about work."
                a "Of course you can, as long as you are willing to take my calls\nwhen I want to just rant about my day."
                y "It's a deal."
                a "Great, then what do you say we head on over to the movie theater."
                y "OK, let me just ditch my date."
                a "No, let her tag along, she sounds awesome."
                jump tothemovies
                
label doneeverything:
    scene dinerwait
    y "So, here we are on another date."
    a "Yeah, I know, so far the lamest one yet."
    y "Yeah, but it's just getting started."
    scene dinerserved
    y "So, what dates have been our most memorable?"
    scene dinereat
    if persistent.soundtrack == True:
        play music "comicaltragedy.ogg" fadein 0.1
    show ldpic9 at memory with dissolve
    a "Well Let's see...  Probably our first date."
    a "You came over to my place.  We talked, and drank some wine."
    show lddinner1 at memory with dissolve
    a "We made ourselves dinner."
    y "You are a great cook, by the way."
    a "Thank you, ... Let's see what else did we do that night..."    
    show ldrock1 at memory with dissolve
    a "We danced to some music on the boombox"
    show ldbgame1 at memory with dissolve
    a "We played some parcheesi."
    y "I don't even remember who won."
    show ldfondle1 at memory with dissolve
    a "We also made out on the couch that night."
    y "I remember that part fondly."
    a "Don't you mean \"fondle-ly\""
    show ldswim1 at memory with dissolve
    y "Didn't we go swimming that night?"    
    a "That's right, I put on a bikini and we went swimming in my pool."
    show ldpatio1 at memory with dissolve
    y "You look great in a bikini, by the way."
    a "Thank you."
    y "Was that the first date?"
    a "I believe it was."
    show ldpicnic1 at memory with dissolve
    a "Then the next date we started where we left off\nwith a poolside picnic in our swimsuits."
    show ldpark4 at memory with dissolve
    y "We also went to the park in swimsuits."
    show ldpark8 at memory with dissolve
    a "Yes, and played basketball."
    show ldhottub1 at memory with dissolve
    y "Did we also make it to the hot tub that night too?"
    a "Probably, we went there a lot."
    y "I remember some epic games of \"Truth or Dare\" played in the hot tub."
    show ldskinny1 at memory with dissolve
    a "Yes, by night's end we were out of our swimsuits."
    y "And that's how you play \"Truth or Dare\"."
    show ldstore4 at memory with dissolve
    a "Another time you dared me to go to the store for beer wearing nothing but a towel."
    y "I don't remember you actually wearing the towel in the store."
    show ldstore2 at memory with dissolve
    a "That's right, I was completely naked."
    y "You are lucky we were the only ones there,\nand that Jessie was cool with it or you would have ended up in jail."
    a "Jessie talks about how boring work is all the time,\n I thought I would liven it up."
    show ldpark9 at memory with dissolve
    a "But that wasn't the only dare involving public nudity\nYou had me shoot free throws in the nude."
    y "You made me do it too, and I got caught.\nbesides there are plenty of times you were naked in that park."
    show ldpark1 at memory with dissolve
    a "Oh yeah, we went to the park a few times."
    show ldpark5 at memory with dissolve
    a "I took off my pants and demonstrated some gymnastics skills."
    show ldpark10 at memory with dissolve
    a "I also remember at the park you took photos of me in front of the fountain."
    y "Those were on a digital camera too, can you e-mail me some copies?"  
    show ldpark12 at memory with dissolve
    a "I posed nude in some of those photos."
    y "I especially want copies of those, please."
    a "I'll think about it."
    show lddrive1 at memory with dissolve
    y "But that wasn't the only naked photo shoot\nRemember the drive into the mountains."
    show lddrive4 at memory with dissolve
    a "As evidenced by the pictures on my dining room table, yes."
    show lddrive6 at memory with dissolve
    a "You took photos of my bare ass."
    show lddrive7 at memory with dissolve
    a "Then talked me into doing nudes."
    y "Then you talked me into posing nude for you."
    show lddrive8 at memory with dissolve
    a "Yes you were a great sport about it."
    y "Fair is fair, but I have a feeling those naked pictures of me will\nshow up some day if I make you mad."
    a "They may indeed."
    show lddrive9 at memory with dissolve
    a "Then we had sex in the car."
    y "Yes that was crazy,  It felt right at the time, but since then\nI keep thinking what would have happen had another car come by."
    a "They would have slowed down, seen what we were doing, and then immediately would have left."
    a "In fact that is exactly what both cars did."
    y "Really? I did not see any other cars."
    a "That is because your back was to the road. I was facing it."
    y "Damn, how embarrassing."
    a "Then I gave you a blow job."
    y "You definitely know what you are doing down there."
    a "You completely failed to return the favor."
    y "Oh man!  That's what you were hinting at?  I totally failed!"
    y "I will make it up to you right now.  Take your panties off and I'll duck under the table."
    a "Umm, not now.  Just keep in mind that you owe me."
    show lddiner1 at memory with dissolve
    y "We've done it all, this is not even the first trip to the Drive-N-Dine."
    show ldmuseum1 at memory with dissolve
    a "Yeah and we went to the art museum afterwords."
    show ldshopping1 at memory with dissolve
    y "Then we went downtown and did some shopping."
    show ldrebecca1 at memory with dissolve
    a "That was the night you met Rebecca."
    y "Charming girl."
    show ldrebecca2 at memory with dissolve
    a "She took us to a nightclub."
    y "Charming {i}drunk{/i} girl." 
    show ldamusement1 at memory with dissolve
    y "Then we ditched her at the bar and went to an Amusement Park, and rode rides until I got sick."
    a "I promise, no more corn dogs, ever!"
    show ldrebecca3 at memory with dissolve
    a "Then another night we ran into Rebecca again, and ended up back at my place."
    show ldrebecca6 at memory with dissolve
    a "The three of us ended up skinny dipping in my pool."
    y "In a spirited game of {i}Marco Polo{/i}, with plenty of naughty touching."
    if not "rebnude" in persistent.reblist:
        $ persistent.reblist.append("rebnude")
    show ldrebecca4 at memory with dissolve
    a "Rebecca made herself at home and ran around naked."
    y "She was not the only one as I recall."
    a "Yeah, but it was my house."
    show ldrebecca9 at memory with dissolve
    a "The three of us had a sleep over, but we were all too tired to do more than sleep."
    y "There I was lying naked between two naked women, and I fell right asleep.\n What the hell was in that alcohol you poured us?"
    scene dinereat
    a "OK, all of those nights were great nights,\nbut we still have not mentioned my favorite night."
    y "I know which one you are talking about, it was the romantic night...."
    show ldrestaurant1 at memory with dissolve
    y "We went to the Cafe Da Silva, and actually got a table."
    show ldclub1 at memory with dissolve
    y "Then went dancing at Lizards Night Club"
    show ldclub2 at memory with dissolve
    a "Don't forget getting thrown out."
    y "Of course..."
    show ldlake1 at memory with dissolve
    y "But then we went to the lake..."
    show ldlake6 at memory with dissolve
    y "And we had that romantic walk..."
    show ldlake7 at memory with dissolve
    a "Did I slip out of my dress at one point..."
    y "Yes you did."
    show ldlake2 at memory with dissolve
    y "Then we rented a boat..."
    show ldlake3 at memory with dissolve
    y "And, you went skinny skiing."
    a "That's right, I like water skiing, but that's the first time\ndoing it while wearing nothing but a life preserver."
    show ldlake4 at memory with dissolve
    a "And then we ended up sleeping on the boat..."
    y "And we drank all the beer, and the deck was very uncomfortable."
    a "Well there was only room for one of us on the cushioned bench."
    show ldlake5 at memory with dissolve
    y "And boated back the next morning."
    a "Yes, also a good night, but still not the best."
    y "Which was?"
    show ldstrip1 at memory with dissolve
    a "The night of the strip club amateur contest, of course."
    show ldstrip4 at memory with dissolve
    y "Really?  OK. you were good."
    show ldstrip3 at memory with dissolve
    y "And you ended up dancing nude.\nI'm surprised that is a highlight."
    show ldstrip6 at memory with dissolve
    a "But, I won $500.  I'd call that a good night."
    y "Well yeah I guess so."
    scene dinerend
    stop music fadeout 3
    y "So we have been on many epic dates now, what kind of relationship do we have?"
    a "Oh my god, I can't believe you said the R word.\nListen, I suck at the R word, always have."
    a "Part of what makes us great is that our R word is undefined.\nAs soon as it gets defined, we are forever locked into following convention."
    y "I get it, you are a free spirit. You are daring, passionate, curious,\nand you don't care what others think of you, and that is why I love being around you."
    a "And you are my muse. I am never as free spirited as I am when I am with you.\nYou inspire me to new heights of enjoyment, and I don't want to lose that."
    y "There we go, we just defined our R word:  We are the SPIRIT and the MUSE."
    a "Ha, I like that.  The SPIRIT and the MUSE: A partnership of fun."
    y "That's so cool, but weren't the muses always female?"
    $ menuplaceX = 0.1
    $ menuplaceY = 0.8
    menu:
        a "Where did you hear that?"
        "Bulfinch's Mythology":
            a "Well it's the 21st century, and women are allowed male muses."
        "The movie {i}Xanadu{/i}":
            a "What was that movie about?"
            y "A muse inspires an artist to paint a beautiful album cover."
            a "No it wasn't, it was a roller disco."
            y "Aha! You did see it!"
            a "Damn it! ... Well my point is that you can't believe bad 80's musicals.\nMuses are those that inspire us, and they can be any gender."
    y "Let's put this partnership of fun to the test.\nCan we defeat all obstacles and still have an amazing night."
    a "Let's find out.... Let's go to the movies!"
    if not "muse" in persistent.arilist:
        $ persistent.arilist.append("muse")
    
label tothemovies:                
        scene freeway2
        if not "dnd" in persistent.plalist:
            $ persistent.plalist.append("dnd")
        card "You leave the Drive-N-Dine, and head back downtown to the movie theater."
        scene theaterlobby1
        show arianelobby1 at comeinleft with moveinleft
        card "The theater downtown has three different movies playing.\n\nAriane can't decide what she wants to see."
        $ menuplaceX = 0.6
        $ menuplaceY = 0.5
        menu:
                a "What do you want to see?"
                "{i}See an Action Movie{/i}":
                        $ movietype = 1
                        jump theater_ariane2
                "{i}See a Romantic Comedy{/i}":
                        $ movietype = 2
                        jump theater_ariane
                "{i}See a Drama{/i}":
                        $ movietype = 3
                        jump theater_ariane3
                "{i}Let Ariane decide{/i}":
                        $ movietype = 4
                        if persistent.ldhotdate and not persistent.ldeverything:
                            y "You said you were making all the choices tonight, so I will leave it up to you."
                            a "I asked for that didn't I. In that case I'll choose the romantic comedy."
                        else:
                            y "It was my choice to go to the movies, it's your choice to pick which one."
                            a "In that case I'll choose the romantic comedy."
                        jump theater_ariane
        
label theater_ariane:
        scene theaterlobby2
        "The theater is crowded with the Saturday night date crowd. \nYou stand in line for popcorn and drinks, while Ariane goes to the ladies room."
        show arianelobby at comeinleft with moveinleft
        "When she gets done, you are still in line."
        a "Maybe I should go save us some seats."
        y "Good idea."
        hide arianelobby with moveoutleft
        scene movierc1
        "You finally get in and the theater is packed."
        "The theater is already dark as the previews begin.\nIt takes you a while for your eyes to adjust and find Ariane who is signaling you."
        scene movierc2
        a "Not the best seats, but we're lucky I found two together."
        scene movierc3
        if not "rc" in persistent.verlist:
            $ persistent.verlist.append("rc")
        "As you take your seat, some girl in black leather and a sitting behind you \nlooks annoyed that your are taking her \"view\"."
        g "Hey down in front."
        y "It's just the previews, you're not missing much."
        scene movierc5
        play sound "vphone.ogg" fadein 0.2
        "You finally get comfortable and the Goth Chick's cell phone goes off."
        scene movierc4
        g "(answering phone) Yo Tanner, whats up?"
        "You turn around and stare at her."
        g "(Looking at you) It's just the previews, you're not missing much."
        g "(back to the caller) Sorry, I'm at the movies..."
        g "Fuck if I know, I snuck in the exit and followed the crowd in..."
        "Ariane is looking annoyed, but isn't saying anything"
        g "A party tonight?  Fuck yeah, I'm there. ..."
        g "I'm outta here... enjoy your precious previews...bitches."
        scene movierc5
        a "Thank god she's gone. I was about ready to go all slayer on that vampire chicks ass."
        "You put your arm around her. She leans against you."
        scene black
        "The movie is starting..."
        play music "martini.ogg" fadein 1
        show rctitle at center
        $ renpy.pause(2.0)
        scene movierc6 with dissolve
        $ renpy.pause(5.0)
        scene movierc7 with dissolve
        $ renpy.pause(5.0)
        scene movierc8 with dissolve
        $ renpy.pause(5.0)
        scene black with dissolve
        card "{b}THE END{/b}"
        scene theater1
        show arianetheater at center0
        stop music fadeout 2
        play ambient "streetnoise.ogg" fadein 1
        a "So, what did you think?"
        if not "rcmov" in persistent.arilist:
            $ persistent.arilist.append("rcmov")
        y "The romance was there, but where was the comedy?"
        y "And, what did you think?"
        a "About what?"
        y "The movie we just saw."
        a "We saw a movie?"
        y "I get it, you found the movie forgettable.\nYou are funnier than the screenwriter."
        a "(laughing) Thanks. So enough about the forgettable movie..."
        if movietype == 4:
            a "I picked out the movie and chose badly.\nIt is quarter to 10, the night is not that old, what do you want to do."
            $ menuplaceX = 0.15
            $ menuplaceY = 0.6
            menu:
                a "What shall we do with the rest of the evening?"
                "{i}Go to the nightclub{/i}":
                    if persistent.ldnightclub or persistent.ldeverything:
                        y "Let's go to that nightclub again, it's just around the corner."
                    else:
                        y "Isn't there a nightclub around the corner? Let's go check it out."    
                    jump NightclubAriane
                "{i}Go back to her place{/i}":
                    jump ToArianesHouse
                "{i}Let her decide what to do{/i}":
                    jump MountainDrive
        else:
            if persistent.ldhotdate:
                a "Well, I let you make the decision on the movie, and the results are as bad as my decision on dinner."
                a "So I will decide what we will do next."
                y "Very well, what next?"
                jump HPAriane
            else:
                a "Well you picked the movie, so it's only fair if I pick what we do next."
                y "Very well, the choice is yours."
                jump HPAriane
                
label theater_ariane2:
        scene theaterlobby2
        "The theater is crowded with the Saturday night date crowd. \nYou stand in line for popcorn and drinks, while Ariane goes to the ladies room."
        show arianelobby3d at comeinleft with moveinleft
        "When she gets done, you are still in line.  Ariane has her 3D glasses on already."
        a "Maybe I should go save us some seats."
        y "Good idea."
        hide arianelobby3d with moveoutleft
        scene moviea1
        "The theater is not as packed as you expected."
        "You find Ariane easily enough."
        a "You picked a movie that has been out for a couple of weeks.\nThe bulk of the crowd is in one of the other theaters."
        y "If you want to see something else..."
        a "No, it's cool.  I prefer less crowded, and these are great seats."
        y "OK then, Let's enjoy the movie."
        scene black
        "The movie is starting..."
        show actitle at center
        play music "actionmusic.ogg" fadein 1
        $ renpy.pause(2.0)
        scene moviea2 with dissolve
        $ renpy.pause(5.0)
        scene moviea3 with dissolve
        play sound "bomb.ogg"
        $ renpy.pause(5.0)
        scene moviea4 with dissolve
        play sound "machinegun.ogg"
        $ renpy.pause(5.0)
        scene black with dissolve
        card "{b}THE END{/b}"
        scene theater1 with dissolve
        show arianetheater at center0
        stop music fadeout 2
        play ambient "streetnoise.ogg" fadein 1
        $ menuplaceX = 0.15
        $ menuplaceY = 0.6
        menu:
            a  "So, what did you think of the movie?"
            "I liked it.":
                a  "Really? You like that dreck?"
                y  "Well there were lots of chase scenes and explosions and that girl was hot!"
                a  "What you say is true... even about the girl... but there was no character \ndevelopment and a mindless plot, and the dialogue could have been written by a 5 year old."
                a  "For me, action movies are more exciting if I care about what happens."
                y  "You weren't at least a little choked up when Smitty died?"
                a  "No, all I knew about Smitty was that he was really good at driving, I barely knew the guy."
                y  "I see your point.  I guess we just have different taste in movies."
            "It wasn't very good.":
                a  "I totally agree.  Lots of chase scenes and bullets, but I did not care about a single character in the film."
                y  "Well the bad guy seemed pretty evil."
                a  "Yeah, but he is the only one in the movie with any integrity.  I was secretly rooting for him."
                y  "Really?"
                a  "Well who else was there to root for?  Chance, who let his partner die?\nThe eye candy chick who wrecked her car twice?"
                y  "(laughing) Oh wow, you are totally right!  Let's face it the movie was designed\nto cater to international audiences.  All visuals, little dialogue."
        a "I let you pick the movie."
        if not "actmov" in persistent.arilist:
            $ persistent.arilist.append("actmov")
        a "So, I will decide what we will do next."
        y "Very well, what next?"
        if not persistent.ldeverything:
            a "Well there is nothing better to get over a bad movie than chocolate ice cream"
            scene icecream1 
            stop ambient fadeout 2
            $ renpy.pause(4.0)
            y "I couldn't help notice that the SUV in the movie is the same make and model that you drive."
            a "Yeah I noticed that too.  Maybe I should add a machine gun\nand sidewinder missile launchers on mine as well.  That'd be COOL!"
            y "Why do you drive an SUV convertible anyways?\nIt does not seem like the kind of vehicle you would drive."
            a "It's our second date, and you still have not figured me out yet?"
            if persistent.ldstrip:
                a "Last date, I danced on stage at a strip club."
            elif persistent.ldparkphotos or persistent.ldmtnphotos:
                a "Last date, I let you take naked pictures of me in a public place."
            elif persistent.ldname == "nude skiing": 
                a "Last date, I went water skiing at night."
            elif persistent.ldname == "lake boating":
                a "Last date, we went boating at night."
            elif persistent.ldname == "romantic date" or persistent.ldname == "walk on the beach":
                a "Last date, I got naked on a public beach."
            elif persistent.ldname == "naked gymnastics" or persistent.ldname == "naked basketball":
                a "Last date, I got naked at a public park."
            elif persistent.ldname == "downtown restaurant" or persistent.ldname == "fountain photoshoot":
                a "Last date, I got naked at a public park."
            elif persistent.ldname == "naked beer run":
                a "Last date, I went to a convenience store naked."
            else:
                a "Well now that I think about it, maybe we have not done anything to clue you in."
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                a  "I am kind of an adrenaline junkie.  I like the thrill of doing dangerous stuff."
                "Really? Me too.":
                    y "Knowing that should make planning our next date a lot of fun."
                    a "Well, I'm not a REAL thrill seeker type.  I'm not into jumping out planes or anything.\nand I don't like getting caught or injured, I won't do anything that is really high risk."
                    y "You do not sound like a real adrenaline junkie then.  What do you consider thrilling?"
                    a "I like driving around in an SUV with no doors or roof.\nDoing an aerial off the high bar is thrilling, and I really like roller coasters."
                    y "So you are a SAFE thrill seeker then.  None of that sounds too dangerous, except the aerial off the high bar."
                "That is something we do not have in common then.":    
                    a "Well, I'm not a REAL thrill seeker type.  I'm not into jumping out planes or anything.\nand I don't like getting caught or injured, I won't do anything that is really high risk."
                    y "So you only do thrilling stuff as long as it is safe to do so?"
                    a "I like driving around in an SUV with no doors or roof.\nDoing an aerial off the high bar is thrilling, and I really like roller coasters."
                    y "Well that's all stuff I can do too, except I can't do an aerial off the high bar."
            a  "I was a gymnast in college."
            if not "gym" in persistent.arilist:
                $ persistent.arilist.append("gym")
            y  "Yes, I would say being a gymnast takes a certain amount of risk and danger."
            y  "Any other kind of dangerous activities you have engaged in?"
            a  "Other sports mostly, water skiing, snow boarding, rollerblading,\nfour wheeling in my SUV, which is why I got it."
            if not "action" in persistent.arilist:
                $ persistent.arilist.append("action")
            if persistent.ldpubnude:
                y "And it seems public nudity is on that list too."
                a "OK, yeah sometimes the thrill of running around naked in a\npublic place is kind of a turn on, assuming the risk of getting caught is low."
                a "If other people are around, NO WAY, unless it is expected\nlike dancing at a strip club, or going to a nude beach or something."
            else:
                y "Again nothing out of the ordinary, have you ever done something weird and gotten a thrill from it?"
                a "Honestly, I have been known to get a thrill from ... being naked in public."
                y "OK, now we are getting somewhere.   When and where does this happen?"
                a "Mostly at home.  As you know I have a pool and hot tub.\nWhen I am home alone I usually just swim naked, and \nmy fences are not very high so all my neighbors can see me."
                y "Any place really public?"
                a "I've been known to go to the store wearing nothing but a towel.\nMy friend Jessie works there and she does not care."
                y "And what about the other store patrons?"
                a "If the store is not empty, I wait for everyone to leave."
            scene icecream5    
            y "But, have you ever been naked in a place that is really public? \nwith other people around? and dressing rooms don't count."
            a "I have been to the nude beach a couple of times."
            y "We have a nude beach?"
            a "Technically no, but at the lake beach about a mile and a half from the main beach\nthere is a rocky ridge coming out of the lake. On the other side there is more beach.\nWhile it is not official, that side of the ridge is considered clothing optional."
            y "You would think that one of the guys at work would have mentioned that to me."
            a "Well they probably haven't since it is so hard to get to, \nand it tends to be a \"sausage fest\" to use the popular term."
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                y "So, it is way more guys than girls then?"
                "I'm not that interested then.":
                    a "I only go when I am with someone.  Keeps the naked guys from bothering me."
                    y "Well maybe we could go together then?"
                    a "Maybe."
                "Still, I'm going to have to check this out.":
                    a "Going alone and going nude is an invitation for naked guys to hit on you."
                    y "Is that why you don't go? I can imagine that would be a problem for women."
                    a "It's a problem for men too, by the way."
                    y "Hmm, Well maybe we should go together then?"
                    a "Maybe."
                "We should go together and you can show me where this nude beach is?":
                    a "Maybe."    
            scene icecream6
            $ renpy.pause(4.0)
            scene icecream7
            a "Is that lightning outside?"
            y "Sure looked like it."
            play sound "distantthunder.ogg" fadein 1 fadeout 1
            "A crash of thunder answers that question."
            a "Where the hell did that storm come from?\nThe sky was perfectly clear when we left the theater."
            y "Wow that is weird. ...  So, uh,  about this trip to a nude beach?"
            scene icecream8
            $ renpy.pause(3.0)
            scene black
            play sound "distantthunder.ogg" fadein 1 fadeout 1
            a "We can talk about another date later, but this one just ended."
            card "With no moon out, and no street lights, it is really dark out. \n\nThe two of you leave the ice cream place \nand head to the parking garage where both of you parked your cars.\n\nThe only light available is coming from your cell phones."
            scene darkari
            $ renpy.pause(3.0)
            y "The electricity looks to be out city wide, is it safe to drive home?"
            $ menuplaceX = 0.8
            $ menuplaceY = 0.1
            menu:
                a "Can't stay here. It's about to rain, and my SUV doesn't have a roof, so I have to leave now."
                "My car is just parked over there, I have a roof, I could drive you home.":
                    a "No, I'll be OK, it's time to call it a night."
                    y "Well, good night then, (You kiss her goodnight)."
                    a "Call me when you get home, let me know your safe."
                    scene black
                    $ persistent.adatecount += 1
                    card "You drive home safely despite the lack of working traffic lights,\n it starts raining just as you get home."
                    card "With nothing to do but sleep, you do.\n\nTHE END"
                    return
                "What? \"Action Girl\" is afraid of a little blackout and thunderstorm?":
                    jump actiongirl
        else:
            a "Well there is nothing better to get over a bad movie than chocolate ice cream"
            scene icecream1 
            stop ambient fadeout 2
            card "You go to an Ice Cream Parlor for dessert."
            y "I couldn't help notice that the SUV in the movie is the same make and model that you drive."
            a "Yeah I noticed that too.  Maybe I should add a machine gun\nand sidewinder missile launchers on mine as well.  That'd be COOL!"
            y "Why do you drive an SUV convertible anyways?\nIt does not seem like the kind of vehicle you would drive."
            a "We have dated quite a lot now, and you still have not figured me out yet?"
            a "I danced on stage at a strip club.\nI let you take naked pictures of me in a public place."
            a "I went waterskiing at night.\nand rode the rollercoaster and the tilt-a-whirl until I got sick."
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                a  "I am kind of an adrenaline junkie.  I like the thrill of doing dangerous stuff."
                "Really? Me too.":
                    y  "Knowing that should make planning our next date a lot of fun."
                    a  "Well, I'm not a REAL thrill seeker type.  I'm not into jumping out planes or anything.\nand I don't like getting caught or injured, I won't do anything that is really high risk."
                    y  "You do not sound like a real adrenaline junkie then.  What do you consider thrilling?"
                    a  "I like driving around in an SUV with no doors or roof.\nDoing an aerial off the high bar thrilling, and I really like roller coasters."
                    y  "So you are a SAFE thrill seeker then.  None of that sounds too dangerous, except the aerial off the high bar."
                "That is something we do not have in common then.":    
                    a  "Well, I'm not a REAL thrill seeker type.  I'm not into jumping out planes or anything.\nand I don't like getting caught or injured, I won't do anything that is really high risk."
                    y "So you only do thrilling stuff as long as it is safe to do so?"
                    a "I like driving around in an SUV with no doors or roof.\nDoing an aerial off the high bar thrilling, and I really like roller coasters."
                    y "Well that's all stuff I can do too, except I can't do an aerial off the high bar."
            a "I was a gymnast in college."
            if not "gym" in persistent.arilist:
                $ persistent.arilist.append("gym")
            y "Yes, I would say being a gymnast takes a certain amount of risk and danger."
            y "Any other kind of dangerous activities you have engaged in?"
            a "Other sports mostly, water skiing, snow boarding, rollerblading\nfour wheeling in my SUV, which is why I got it."
            if not "action" in persistent.arilist:
                $ persistent.arilist.append("action")
            y "And it seems public nudity is on that list too."
            a "OK, yeah sometimes the thrill of running around naked in a\npublic place is kind of a turn on, assuming the risk of getting caught is low."
            scene icecream5    
            y "But, have you ever been naked in a place that is really public? \nwith other people around? and dressing rooms don't count."
            a "I have been to the nude beach a couple of times."
            y "We have a nude beach?"
            a "Technically no, but at the lake beach about a mile and a half from the main beach\nthere is a rocky ridge coming out of the lake. On the other side there is more beach.\nWhile it is not official, that side of the ridge is considered clothing optional."
            y "You would think that one of the guys at work would have mentioned that to me."
            a "Well they probably haven't since it is so hard to get to, \nand it tends to be a \"sausage fest\" to use the popular term."
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                y "So, it is way more guys than girls then?"
                "I'm not that interested then.":
                    a "I only go when I am with someone.  Keeps the naked guys from bothering me."
                    y "Well maybe we could go together then?"
                    a "Sure, put that on the list of things to do."
                "Still, I'm going to have to check this out.":
                    a "Going alone and going nude is an invitation for naked guys to hit on you."
                    y "Is that why you don't go? I can imagine that would be a problem for women."
                    a "It's a problem for men too, by the way."
                    y "Hmm, Well maybe we should go together then?"
                    a "Sure, put that on the list of things to do."
                "We should go together and you can show me where this nude beach is?":
                    a "Sure, put that on the list of things to do."  
            scene icecream6
            $ renpy.pause(4.0)
            scene icecream7
            a "Is that lightning outside?"
            y "Sure looked like it."
            play sound "distantthunder.ogg" fadein 1 fadeout 1
            "A crash of thunder answers that question."
            a "Where the hell did that storm come from?\nThe sky was perfectly clear when we left the theater."
            y "Wow that is weird. ...  So, uh,  about this trip to a nude beach?"
            scene icecream8
            $ renpy.pause(3.0)
            scene black
            play sound "distantthunder.ogg" fadein 1 fadeout 1
            a "We can talk future plans later, what should we do now?"
            card "With no moon out, and no street lights, it is really dark out. \n\nThe two of you leave the ice cream place \nand head to the parking garage where both of you parked your cars.\n\nThe only light available is coming from your cell phones."
            scene darkari
            $ renpy.pause(3.0)
            y "The electricity looks to be out city wide, is it safe to drive home?"
            $ menuplaceX = 0.8
            $ menuplaceY = 0.1
            menu:
                a "Can't stay here. It's about to rain, and my SUV doesn't have a roof, so I have to leave now."
                "My car is just parked over there, I have a roof, I could drive you home.":
                    a "No, I'll be OK, it's time to call it a night."
                    y "Well, good night then, (You kiss her goodnight)."
                    a "Call me when you get home, let me know your safe."
                    scene black
                    $ persistent.adatecount += 1
                    card "You drive home safely despite the lack of working traffic lights,\n it starts raining just as you get home."
                    card "With nothing to do but sleep, you do.\n\nTHE END"
                    return
                "What? \"Action Girl\" is afraid of a little blackout and thunderstorm?":
                    label actiongirl:
                    a "I'm intrigued, you have something daring in mind?"
                    y "Nothing big, but ask yourself, how often do you get to see the city with no lights?"
                    a "I see where you are going, but let's stay off the streets.\nLet's go on the roof of the garage and see whats going on from there."
                    scene blackroof
                    if persistent.soundtrack == True:
                        play song "dancingmice1.ogg" fadein 0.1
                    "You walk up the stairs to the parking garage to the top level."
                    a "Cool, we got some light up here from the Art Museum, they must be running a generator."
                    a "We should be able to see downtown over there in the corner."
                    scene blackout
                    y "Wow, this is kind of eerie, fog usually shows up after rain, not before."
                    a "I see a lot of people coming out of the back exit of the nightclub. It's probably chaos in there."
                    y "Cars piling up at the intersection, no traffic lights to control traffic."
                    y "So, how long before the looting starts?"
                    scene blackoutari
                    a "I'd be shocked if it happens in this town."
                    a "You know, it's kind of romantic up here looking down on the chaos."
                    y "I think so too."
                    "She kisses you."
                    a "There's nobody else up here, you wanna..."
                    show rain fall
                    play ambient "rain.ogg" fadein 2
                    "Suddenly it starts raining."
                    a "Oh, dammit!"
                    scene blackrun
                    show rain fall
                    "The rain is coming down fast all of a sudden."
                    "The two of you run to the stairs where you can get some shelter."
                    y "Let's go to my car, it's more protected."
                    "Ariane nods in agreement"
                    stop ambient fadeout 1
                    scene ariincar1
                    y "Do you want me to drive you home?"
                    a "You saw the traffic mess outside, may as well stay here for now."
                    y "I can turn the heater on if you want."
                    a "Sure. The cold isn't as bad as the wet though."
                    y "There might be a T-Shirt in the back you can use to dry off."
                    a "Let me see if I can find it."
                    scene ariincar2
                    "Ariane climbs into the back"
                    a "Found it... eww it's dirty and greasy."
                    y "Oh yeah, I might have used it to clean the windshield and take off the oil cap."
                    a "Luckily there is a perfectly clean towel back here."
                    y "I forgot I had that."
                    a "And a sleeping bag"
                    y "Just in case I have to camp"
                    a "Good a time as any."
                    scene ariincar3
                    if not "tits" in persistent.arilist:
                        $ persistent.arilist.append("tits")
                    "Ariane takes off her wet clothes and dries herself off with the towel"
                    a "Aww, much better."
                    a "Hey, want to take off your wet clothes and join me in the sleeping bag?"
                    scene ariincar4
                    y "Electricity came back on"
                    a "Well so much for that idea.\nYou may take me home now, [persistent.playername]."
                    scene arihouseoutside2
                    play ambient "rain.ogg"
                    show rain fall
                    "When you get to Ariane's home, Ariane is wearing the towel."
                    a "Come on in out of the rain.\nThere are towels in the bathroom, and I can throw your clothes in the dryer." 
                    stop ambient fadeout 1
                    if not persistent.ldeverything:
                        scene arihousehallway3
                        a "Once I've dried off, what do you say to some hot cocoa?"
                        y "Sounds nice."
                        scene aricocoa
                        a "When it stops raining, and your clothes are dry,\nyou will need to take me back downtown to get my car."
                        scene arirobe2
                        a "Since that is going to be a while..."
                        scene arihousehallway2
                        show arirobe3 at center0
                        hide arirobe3 with moveoutbottom
                        a "Why don't we find something to do in the mean time."
                        y "OK! I could think of a few things... actually I can only think of one."
                        scene aribedroom1
                        if not "nude" in persistent.arilist:
                            $ persistent.arilist.append("nude")
                        card ""
                        a "Glad we are thinking the same way.  Want to fuck?"
                        label genericsexscene:
                        if not "sex" in persistent.arilist:
                            $ persistent.arilist.append("sex")
                        scene arisex
                        play sound "sexbed.mp3" fadein 0.1
                        $ renpy.pause(13)
                        scene black with dissolve
                        stop sound fadeout 1
                        card "Next morning"
                        scene arimorning
                        y "I'm going to have to drive you downtown to get your SUV."
                        a "No rush, it's a lazy Sunday morning."
                        y "Here's to a trouble free Sunday."
                        scene black
                        $ persistent.adatecount += 1
                        if persistent.aending3 == False or persistent.epilogue > 0:
                            $ persistent.aending3 = True
                            show picenda4 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("Blackout","Fun","", xcenter = 0.1, yalign = 0.1)
                        card "The two of you enjoy your Sunday together.\n\nTHE END"
                        return   
                    else:
                        scene arihousehallway3
                        $ menuplaceX = 0.1
                        $ menuplaceY = 0.8
                        menu:
                            a "Are you still up for a daring adventure, something we haven't done before?"
                            "I think we have had enough adventures, let's just have sex.":
                                scene aribedroom1
                                if not "nude" in persistent.arilist:
                                    $ persistent.arilist.append("nude")
                                a "You are probably right. I could use a nice fuck."
                                jump genericsexscene
                            "I don't know what did you have in mind?":
                                a "You'll see, stay right here... and take off your clothes."
                                scene arihousehallway
                                "Ariane rushes off to the bathroom, you do as she asks and strip naked."
                                scene arihousehallway4
                                if not "nude" in persistent.arilist:
                                    $ persistent.arilist.append("nude")
                                a "I've been saving this for a rainy day and since we have one..."
                                a "Here let's lube you up."
                                scene arihouse11
                                a "Are you ready to dance?"
                                scene arisex2
                                if not "anal" in persistent.arilist:
                                    $ persistent.arilist.append("anal")
                                play sound "sexchair.mp3" fadein 0.1
                                $ renpy.pause(8.0)
                                scene arimorning
                                stop sound fadeout 1
                                card "Next morning"
                                y "I'm going to have to drive you downtown to get your SUV."
                                a "No rush, it's a lazy Sunday morning."
                                y "Here's to a trouble free Sunday."
                                scene black
                                $ persistent.adatecount += 1
                                if persistent.aending3 == False or persistent.epilogue > 0:
                                    $ persistent.aending3 = True
                                    show picenda4 at achievepos1 with moveinleft
                                    if persistent.story1 == False or persistent.epilogue > 0:
                                        $ persistent.story1 = True
                                        show picenda1 at achievepos2 with moveinleft
                                        $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                                    $ achievement_frame("Blackout","Fun","", xcenter = 0.1, yalign = 0.1)
                                card "The two of you enjoy your Sunday together.\n\nTHE END"
                                return  
            
label theater_ariane3:
        scene theaterlobby2
        "The theater is crowded with the Saturday night date crowd. \nYou stand in line for popcorn and drinks, while Ariane goes to the ladies room."
        show arianelobby at comeinleft with moveinleft
        "When she gets done, you are still in line."
        a "Maybe I should go save us some seats."
        y "Good idea."
        hide arianelobby with moveoutleft
        scene movied1
        "The theater is not as packed as you expected."
        "You find Ariane easily enough."
        a "Art films like this one don't get crowded."
        y "If you want to see something else..."
        a "No this is cool.  I prefer less crowded, and these are great seats."
        if not "rebname" in persistent.reblist:
            $ persistent.reblist.append("rebname")
        if not "rebari" in persistent.reblist:
            $ persistent.reblist.append("rebari")  
        if persistent.ldrebecca:
            scene movied2
            re "Hey guys!"
            a  "Hey Rebecca.  Wow twice in one day, almost like our college days.\nYou remember [persistent.playername] don't you."
            re "Of course, nice to meet you again, [persistent.playername]."
            if persistent.ldeverything:
                y "Hello again, Rebecca.  You look different since I saw you last."
                re "What do you mean? My hair and makeup is the same as last time.\nAre you talking about my outfit?"
                y "Your clothes, yes, that's got to be it.\nLast time I saw you, you weren't wearing any. Nice change."
                re "Thanks, I think, but I'm not the only one with a new look.\nAriane, Did Heidi hook you up with an appointment?"
                a "Yeah she did, thanks for the tip."
                if not "heiariane" in persistent.reblist:
                    $ persistent.reblist.append("heiariane")
                re "So you're on yet another date with [persistent.playername].  Is he your boyfriend now?"
                a "No, I don't have boyfriends.  He is my Muse."
                y "And she is my Spirit."
                re "Umm, I don't get it."
                a "It's a thing, just go with it."
                re "OK, whatever."
                $ menuplaceX = 0.1
                $ menuplaceY = 0.8
                menu:
                    "The lights are dimming and the movie is about to start\nWhat do you want to do here?"
                    "{i}Invite Rebecca to join you and Ariane{/i}":
                        y "Hey Rebecca, why don't you join us, have a seat by Ariane."
                        re "Are you sure?  I don't want to be a third wheel."
                        y "No problem.  Ariane and I were just discussing how\nour evenings out tend to become epic adventures."
                        y "So far this one hasn't reached that point yet,\nand you have made our dates interesting in the past, so..."
                        a "Yes, Rebecca you should join the adventure!"
                        scene movied3
                        re "Sure, I have nothing else going on tonight."
                        a "Good."
                        re "Just one comment, if you don't mind...\nMovie night dates tend to not be very epic."
                        y "True, but you weren't there for the bar fight."
                        re "The what?"
                        a "Shh, I'll explain later, the movie is starting."
                        jump theater_rebecca
                    "{i}Let Rebecca find a seat elsewhere.{/i}":
                        re "Well good to see you again Ariane, and you too [persistent.playername].\nI'll go sit over there and let you two enjoy the rest of whatever you are calling your night together."
            else:
                if persistent.ldrebecca:
                    y "Hello again, Rebecca.  You have changed your look since I last seen you."
                    re "What? The outfit?"
                    y "Yes, nice outfit, last time I saw you, you were naked."
                    re "Thanks, I think. Ariane, Did Heidi hook you up with an appointment?"
                else:    
                    y "Hello again Rebecca."
                    re "Hey I like your new hair style, Did Heidi hook you up with an appointment?"
                a "Yeah she did, thanks for the tip."
                if not "heiariane" in persistent.reblist:
                    $ persistent.reblist.append("heiariane")
                re "So you're on a second date with [persistent.playername], I would think you'd be better dressed."
                a "Long story, I'll tell you all about it later.\nSo what brings you to the movies, and why are you all dressed up?"
                re "I had a crappy day at work today, working retail I dress nice to work, \nand this is what I was wearing."
                re "This theater is within walking distance, so after a crappy day, decided to treat myself."
                a "Good for you!"
                $ menuplaceX = 0.1
                $ menuplaceY = 0.8
                menu:
                    "The lights are dimming and the movie is about to start\nWhat do you want to do here?"
                    "{i}Invite Rebecca to join you and Ariane{/i}":
                        y "Hey Rebecca, why don't you join us, have a seat by Ariane."
                        re "Are you sure?  I don't want to be a third wheel."
                        y "No problem.  It sounds like you could use a friend, and as Ariane says, this {i}date{/i} has degraded to a\nhangout session already, so why not hangout with us?"
                        scene movied3
                        re "Are you ok with this Ariane?"
                        a "Sure, join the party!"
                        jump theater_rebecca
                    "{i}Let Rebecca find a seat elsewhere.{/i}":
                        re "Well good to see you again Ariane, and you too [persistent.playername].\nI'll go sit over there and let you two enjoy the rest of your date."
        else:
            scene movied2
            re "Hey guys!"
            a  "Hey Rebecca.  Wow twice in one day, almost like our college days."
            a  "Rebecca, I'd like you to meet my date for the evening, [persistent.playername].\n[persistent.playername], this is Rebecca, an old friend from college who I saw again this morning at the gym."
            y  "Nice to meet you Rebecca.  A friend of Ariane is a friend of mine."
            re "Nice to meet you too, [persistent.playername].  Such good manners. \nI see what you see in him Ariane.  So, this was the {i}hot date{/i} you were talking about?"
            a "Yep, this is him.  Thanks for being subtle about it."
            re "Hey I like your new hair style, Did Heidi hook you up with an appointment?"
            a "Yes she did, thanks for the tip."
            if not "heiariane" in persistent.reblist:
                $ persistent.reblist.append("heiariane")
            re "So you are on a second date, I would think you would be better dressed."
            a "Long story, I'll tell you all about it later.\nSo what brings you to the movies, and why are you all dressed up?"
            re "I had a crappy day at work today. I work at the fancy Lingerie boutique downtown,\n and this is what I wore to work."
            if not "rebjob" in persistent.reblist:
                $ persistent.reblist.append("rebjob")
            re "This theater is within walking distance, so after\na crappy day, decided to treat myself to a movie."
            a "Good for you"
            $ menuplaceX = 0.5
            $ menuplaceY = 0.8
            menu:
                "The lights are dimming and the movie is about to start\nWhat do you want to do here?"
                "{i}Invite Rebecca to join you and Ariane{/i}":
                    y "Hey Rebecca, why don't you join us, have a seat by Ariane."
                    re "Are you sure?  I don't want to be a third wheel."
                    y "No problem.  It sounds like you could use a friend, and as Ariane says, this {i}date{/i} has degraded to a\nhangout session already, so why not hangout with us?"
                    scene movied3
                    re "Are you ok with this Ariane?"
                    a "Sure, join the party!"
                    jump theater_rebecca
                "{i}Let Rebecca find a seat elsewhere.{/i}":
                    re "Well good to see you again Ariane, and you too [persistent.playername].\nI'll go sit over there and let you two enjoy the rest of your date."
        scene black
        show dtitle at center
        play song "beforeandafter.ogg" fadein 0.1
        $ renpy.pause(5.0)
        scene movied4 with dissolve
        $ renpy.pause(5.0)
        scene movied5 with dissolve
        $ renpy.pause(5.0)
        scene movied6 with dissolve
        $ renpy.pause(5.0)
        scene movied7 with dissolve
        $ renpy.pause(5.0)
        scene movied7a with dissolve
        $ renpy.pause(5.0)
        scene movied8 with dissolve
        $ renpy.pause(5.0)
        scene movied9 with dissolve
        $ renpy.pause(5.0)
        scene movied10 with dissolve
        $ renpy.pause(5.0)
        scene movied11 with dissolve
        $ renpy.pause(5.0)
        scene black with dissolve
        card "{b}THE END{/b}"
        scene theater1
        show arianetheater at center0
        stop song fadeout 2
        play ambient "streetnoise.ogg" fadein 1 fadeout 1
        $ menuplaceX = 0.2
        $ menuplaceY = 0.8
        menu:
            a  "Well that was depressing.  So what did you think?"
            "I agree, it was a good movie, but very sad.":
                y  "Was this a good movie for a date? What with all  the sex scenes, and nudity?"
                a  "But it was all female nudity, except for a couple of very brief male butt shots."
            "I don't know, it was kind of a chick flick.":
                a "How can you call it a chick flick with all that sex and nudity?"
                a  "If it was a chick flick with sex, you'd see a penis at least once,\na couple of very brief butt shots is all the male nudity I could see."
        y  "Fair or not, Hollywood has a rule.  Female frontal nudity is usually viewed as sexy,\nwhile male frontal nudity is viewed as comical."
        a "Well there was plenty of female nudity, especially in that lesbian scene."
        y "True, but I wasn't going to mention it."
        if not "dramov" in persistent.arilist:
            $ persistent.arilist.append("dramov")
        if persistent.ldrebecca:
            a "I bet Rebecca enjoyed that scene."
            y "Oh right, she's a lesbian herself.  You two met in college?"
            a "Yes... What are you thinking there bud?"
        else:
            a "Whats with men and lesbian sex?  I'm OK with it.  I have lesbian friends.\nRebecca that girl I introduced you to is a lesbian."
            if not "rebgay" in persistent.reblist:
                $ persistent.reblist.append("rebgay")
            y "Really?  And you two went to college together?"
            a "Yes... What are you thinking there bud?"
        a "What do you say we get some ice cream?"
        y "Sure, sounds good"
        scene icecream1
        stop ambient fadeout 2
        "The two of you go to an ice cream parlor for sundaes.  You eat in silence."
        a  "What're you thinking about?"
        if not persistent.ldeverything and not persistent.ldtext == "sleepover":
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                a "Don't tell me, I can read your mind.  You are imagining that \nlesbian scene but with me and Rebecca aren't you?"
                "Yes, I was.  Guilty as charged.":
                    a "Men are so easy to read.  Have your fantasy\nif you want, but we were never together in that way."
                "Well, now I am.  Thanks for the imagery.":
                    a "You are welcome.  Fantasize all you want, \nbut we were never together in that way."
                "Actually, I was fantasizing a three way, with me in the middle.":
                    a "Only in your dreams there, [persistent.playername]."  
                    $ menuplaceX = 0.1
                    $ menuplaceY = 0.7
                    menu:
                        a "If I'm going to be in a three way, it is going to be me and two guys."
                        "I'd be willing to get in on that action.":
                            a "Wow, didn't know you were so secure in your manhood."
                            y "Hey I'm not afraid to make comparisons."
                        "You would have to find two other guys for that job, not me":
                            a "So you are saying you are not secure with your manhood?"
                            y "Well I can handle myself in a contest."
                            if not persistent.ldhotdate:
                                a "Now I am intrigued."
                                y "You should be."
                            else:
                                a "Hey, I have seen your stuff.  Your odds of winning a contest are at best 50-50."
                                y "Ouch, that is harsh."    
                                a "Hey you brought up the topic."
            y "So no threesome with you, me, and Rebecca?"
            a "Sorry to disappoint you."
        else:         
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                a "Don't tell me, I can read your mind.  You are imagining that \nlesbian scene but with me and Rebecca aren't you?"
                "Yes, I was.  Guilty as charged.":
                    a "Men are so easy to read.  Have your fantasy\nif you want, but we were never together in that way."
                "Well, now I am.  Thanks for the imagery.":
                    a "You are welcome.  Fantasize all you want, \nbut we were never together in that way."
                "Just remembering when the three of us were in bed together.":
                    y "We could have had a three way you know."
                    a "Never would have worked out.  Rebecca was more interested in me, than you\nI would have been the one in the middle and I don't swing that way."
                    a "I probably should have just kicked the two of you out of bed,\nbut I was too drunk and tired to even do that."
                    $ menuplaceX = 0.1
                    $ menuplaceY = 0.7
                    menu:
                        a "Besides, if I'm going to be in a three way, it is going to be me and two guys."
                        "I'd be willing to get in on that action.":
                            a "Wow, didn't know you were so secure in your manhood."
                            y "Hey I'm not afraid to make comparisons."
                            a "Hey, I have seen your stuff.  Your odds of winning a contest are at best 50-50."
                            y "Ouch, that is harsh."    
                            a "Hey you brought up the topic."
                        "You would have to find two other guys for that job, not me":
                            a "So you are saying you are not secure with your manhood?"
                            y "I'm secure, I would just not be very comfortable in that kind of situation."
            y "So no threesomes?"
            a "Sorry to disappoint."        
        y "Have you ever \"experimented\" with Rebecca?"
        a "With her? no.   Wait, that sounds evasive... I have never had sex with a woman."
        if not "hetero" in persistent.arilist:
            $ persistent.arilist.append("hetero")
        y "Actually, that sounds even more evasive, have you kissed another woman?"
        a "As a friendly greeting, plenty of times."
        y "How about more than friendly?  Have you ever, as the British say, \"snogged\" another woman?"
        a "Um, OK, yes... once... OK twice... OK three times."
        y "With Rebecca?"
        a "Twice with Rebecca, and we kept our clothes on... mostly...."
        a "...and that other time with another girl.  But  we were both imagining we were with men... at least I was.\nI was really young and naive at the time."
        scene icecream5
        y "We all make embarrassing mistakes when we are young and in love.\nYou don't seem to be naive now."
        a "Comes with lots experience... wait that sounds awful. \nI don't have lots and lots of experience, just enough."
        if not persistent.ldeverything:
            a "OK, that's enough sex talk for tonight,  \nIsn't there a rule that sexual honesty does not happen until the third date?"
            y "Are you saying there will be a third date?"
            scene icecream6
            $ renpy.pause(4.0)
            scene icecream7
            a "Was that lightning outside?"
            play sound "distantthunder.ogg" fadein 1 fadeout 1
            "A crash of thunder answers that question."
            a "Where the hell did that storm come from?\nThe sky was perfectly clear when we left the theater."
            y "Wow that is weird. ...  So, uh,  about this third date?"
            scene icecream8
            $ renpy.pause(3.0)
            scene black
            a "Well we can talk third date later, but this one just ended."
        else:
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                a "OK, that's enough Ariane sex talk for tonight,\nAny embarrassing sex stories from your past you wish to share?"
                "Yes, but now is not the time":
                    a "Why not?"
                    y "Well, a visual demonstration would be more appropriate."
                    a "Ooh, maybe we should move this to my place then."
                "No, nothing to share.":
                    a "You just said we all make embarrassing mistakes."
                    y "And I have made a few, but I do not want to talk about it."
                    a "So no good stories then?"
                    y "Nope."
                    a "Maybe we should go back to my place and make some then."
            scene icecream6
            $ renpy.pause(4.0)
            scene icecream7
            a "Was that lightning outside?"
            play sound "distantthunder.ogg" fadein 1 fadeout 1
            "A crash of thunder answers that question."
            a "Where the hell did that storm come from?\nThe sky was perfectly clear when we left the theater."
            y "Wow that is weird. ...  So, uh,  about this trip to your place?"
            scene icecream8
            $ renpy.pause(3.0)
            scene black
            a "Sex can wait, we should probably worry more about our safety."
        play sound "distantthunder.ogg" fadein 1 fadeout 1
        card "With no moon out, and no street lights, it is really dark out.\nYour only light source are cell phone screens. \n\nThe two of you leave the ice cream place \nand head to the parking garage where both of you parked your cars."
        scene darkari
        $ renpy.pause(3.0)
        y "The electricity looks to be out city wide, is it safe to drive home?"
        a "Can't stay here. It's about to rain, and my SUV doesn't have a roof, so I have to leave now."
        y "My car is just parked over there, I have a roof, I could drive you home."
        a "No, I'll be OK, it's time to call it a night."
        y "Well, good night then, (You kiss her goodnight)."
        a "Call me when you get home, let me know your safe."
        scene black
        card "You drive home safely despite the lack of working traffic lights,\n it starts raining just as you get home."
        scene phone
        "You give Ariane a call like you promised."
        show ariphone3 at center0 with moveinright 
        a "{i}Hey [persistent.playername].{/i}"
        y "You make it home OK?"
        a "{i}I think so, the electricity is out, so I can't see for sure{/i}"
        scene black
        show ariphone3 at center0
        a "{i}The drive was a pain, passed an accident on the freeway,\nand some idiot followed me for a couple of miles with his brights on.{/i}"
        a "{i}City people don't know how to drive without streetlights.{/i}"
        y "Tell me about it, I had to get through two major intersections with no light signals, or cops directing traffic."
        a "{i}Glad you made it.{/i}"
        y "So is it raining where you are at?  It is here."
        $ menuplaceX = 0.5
        $ menuplaceY = 0.75
        menu:
            a "{i}Nope, but it's headed this way.{/i}"
            "Well stay safe Ariane, I'll talk to you later.":
                a "{i}Another memorable crazy night. Let's definitely do it again.{/i}"
                scene black
                $ persistent.adatecount += 1
                if persistent.aending11 == False or persistent.epilogue > 0:
                    $ persistent.aending11 = True
                    show picenda1 at achievepos1 with moveinleft
                    if persistent.story1 == False or persistent.epilogue > 0:
                         $ persistent.story1 = True
                         show picenda2 at achievepos2 with moveinleft
                         $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                    $ achievement_frame("","Ice Cream","", xcenter = 0.1, yalign = 0.1)
                card "With the electricity still out, you go to bed,\nremembering to turn off the alarm first.\n\nYou dream of new adventures.\n\nTHE END"
                return
            "So, uh, what are you wearing?":
                a "{i}Still in the clothes you saw me in, why?{/i}"
                y "Um, (ahem), want to try again?"
                if persistent.soundtrack == True:
                    play music "lapdance.ogg" fadein 0.1
                a "{i}Ooooh,... I am naked actually.{/i}"
                hide ariphone3 with moveoutleft
                show ariphone4 at center0 with moveinleft 
                y "And where are you?"
                a "{i}Umm, ...I'm in my shower.{/i}"
                show arishower1 at center0 with moveintop
                scene arishower1
                show ariphone4 at center0 with moveinbottom
                a "{i}The hot steamy water glistening off my naked body.{/i}"
                scene arishower2
                play ambient "shower.ogg" fadein 1
                y "I'm there with you.  My hands lathered in soap."
                y "I push you against the shower wall and clean your breasts so well they shine."
                a "{i}I lather up my hands, my soapy hands caressing your chest.{/i}"
                scene arishower3
                a "{i}I slowly move my hands down your body{/i}"
                y "Oh yeah!"
                a "{i}Your abs, your stomach...{/i}"
                y "Keep going."
                scene arishower4
                a "{i}I'm washing your waist, my hands so low I crouch down.{/i}"
                y "And then..."
                a "{i}There you are you little sucker, I've been looking all over for you!{/i}"
                stop music
                stop ambient
                y "Huh? What?"
                a "{i}Oops, sorry... I just found my lighter so I can light some candles.{/i}"
                show ariphone5 with moveinbottom
                y "Well that was a mood killer."
                a "{i}Hey the electricity came on.{/i}"
                scene ariphone6
                y "Here too."
                a "{i}Great.  Hey want to hang out and watch TV together?{/i}"
                scene ariphone7
                y "Sure, when can we do that?"
                a "{i}Right now, turn on NBC, we'll watch Saturday Night Live together.{/i}"
                y "OK, cool."
                scene black
                $ persistent.adatecount += 1
                if persistent.aending2 == False or persistent.epilogue > 0:
                    $ persistent.aending2 = True
                    show picenda3 at achievepos1 with moveinleft
                    if persistent.story1 == False or persistent.epilogue > 0:
                         $ persistent.story1 = True
                         show picenda1 at achievepos2 with moveinleft
                         $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                    $ achievement_frame("","Phone Sex","", xcenter = 0.1, yalign = 0.1)
                card "You watch SNL until Weekend Update.  Both of you start feeling tired.\n\nYou hang up and go to bed.\n\nTHE END"
                return
        
label theater_rebecca:
        scene black
        show dtitle at center
        play song "beforeandafter.ogg" fadein 0.1
        $ renpy.pause(5.0)
        scene movied4 with dissolve
        $ renpy.pause(5.0)
        scene movied5 with dissolve
        $ renpy.pause(5.0)
        scene movied6 with dissolve
        $ renpy.pause(5.0)
        scene movied7 with dissolve
        $ renpy.pause(5.0)
        scene movied7a with dissolve
        $ renpy.pause(5.0)
        scene movied8 with dissolve
        $ renpy.pause(5.0)
        scene movied9 with dissolve
        $ renpy.pause(5.0)
        scene movied10 with dissolve
        $ renpy.pause(5.0)
        scene movied11 with dissolve
        $ renpy.pause(5.0)
        scene black with dissolve
        card "{b}THE END{/b}"
        scene theater1
        stop song fadeout 2
        play ambient "streetnoise.ogg" fadein 2
        show aritheater2 at left0
        show rebtheater2 at right0
        a  "Well that was depressing."
        if not "dramov" in persistent.arilist:
            $ persistent.arilist.append("dramov")
        re  "True, but it was a good movie though."
        scene theater1
        show aritheater at left0
        show rebtheater at right0
        $ menuplaceX = 0.5
        $ menuplaceY = 0.8
        menu:
            re"What did you think [persistent.playername]?"
            "I agree, it was a good movie, but very sad.":
                scene theater1
                show aritheater2 at left0
                show rebtheater at right0
                re  "At least they did not skimp on the sex scenes, and nudity."
                scene theater1
                show aritheater2 at left0
                show rebtheater2 at right0
                a  "But it was all female nudity, except for a couple of very brief butt shots."
                scene theater1
                show aritheater at left0
                show rebtheater at right0
                y  "The lack of male nudity did not bother me."
                scene theater1
                show aritheater2 at left0
                show rebtheater at right0
                re "Me neither, though it throws me when two obviously straight actresses try to act like lesbians."
                "You and Ariane have nothing to say about that."
            "I don't know, it was kind of a chick flick.":
                re "How can you call it a chick flick with all that sex and nudity.\nI think the film qualified as soft core porn"
                scene theater1
                show aritheater2 at left0
                show rebtheater2 at right0
                a  "It's not soft core porn if you never see penis, a couple of very brief\nbutt shots is all the male nudity I could see."
                re "(chuckle) You said penis."
                scene theater1
                show aritheater at left0
                show rebtheater at right0
                y  "Rebecca has a point, female frontal nudity is usually viewed as sexy,\nwhile male frontal nudity is viewed as comical."
                scene theater1
                show aritheater at left0
                show rebtheater2 at right0
                re "Yeah, lack of male nudity is not as bad as when two obviously straight actresses try to act like lesbians."
                "You and Ariane have nothing to say about that."
        scene theater1
        show aritheater2 at left0        
        show rebtheater at right0
        re "Well the cure for a depressing film is right next door, who is up for some ice cream?"
        if persistent.ldrebecca:
            scene icecream2c
            stop ambient fadeout 2
            "The three of you go to an ice cream parlor for sundaes"
            y "So Rebecca, we were just talking earlier about our last date when we met you."
            if persistent.ldstrip and not persistent.ldeverything:    
                scene icecream2b
                re   "Oh when I took you guys to a strip club?"
                a   "Yeah that was a bit weird."
                scene icecream2a
                re  "You found the strip club trip weird?"
                if persistent.ldstripwon: #Strip Club Lost
                    a   "The whole thing was weird, the place, the tennis instructor routine,you did,\nthe fact that you talked me into dancing nude on stage."
                    re  "Yeah, but you won $500, then the two of you left together,\nleaving me all alone... in a Strip Club... with a purse full of singles."
                    re  "You two probably went back to her place and had hot naked sex didn't you?"
                    scene icecream2c
                    y  "Yes we did."
                    re "Well you are very welcome!  My weird actions got you two love birds together."
                else: #Strip Club Won
                    a   "The whole thing was weird, the place, the tennis instructor routine, you did,\n the fact that you talked me into dancing on stage."
                    scene icecream2c
                    y   "Let's not forget the bit where you two left together,\nleaving me all alone... in a Strip Club... with a wallet full of singles."
                    re  "Aww, you poor thing.  If it is any consolation, you probably had more fun than we did."
            if not persistent.ldstrip and not persistent.ldeverything:    
                re   "Oh, when I took you guys to a nightclub?"
                y   "Yeah that part was OK."            
                if persistent.ldname == "met rebecca": #met rebecca
                    scene icecream2b
                    a "Then we all ended up back at my place."
                    re "Oh yeah, The three of us ended up swimming in my pool. Ariane and I shared a bikini."
                    scene icecream2a
                    a  "You got the top half and I the bottom."
                    re "It's only fair, your boobs are bigger then mine, they should be shared with everyone."
                    re "So what happened after I left?"
                    a "Not much, the date ended soon after."
                    re "So no sex?"
                    a "That's none of your business, Rebecca."
                    a "but, no."
                if persistent.ldname == "marco polo": #marco polo
                    scene icecream2b
                    a "Then we all ended up back at my place."
                    re "Oh yeah, The three of us ended up swimming naked in the pool."
                    scene icecream2c
                    y "Yes, we played {i}Marco Polo{/i} in the nude."
                    re "Hey, it was fun trying to get you two past your inhibitions."
                    scene icecream2a
                    re "So what happened after I left?"
                    a "Not much."
                    re "So no sex?"
                    a "That's none of your business, Rebecca."
                    a "But actually there was a lot of sex."
                    re "My devious plan worked then."
                    a "Yes, it did."
                if persistent.ldname == "sleepover": #sleepover
                    scene icecream2a
                    a "Then we all ended up back at my place."
                    re "Yes, we all slept together in Ariane's bed, but we were all too tired to do more than sleep."
                    scene icecream2c
                    y "There I was lying naked between two naked women, and I fell right asleep."
                    scene icecream2
                    re "And someone was hogging all the covers."
                    scene icecream2a
                    a  "They were my covers."
                    re "Yeah, but I ended up spooning with [persistent.playername] just to stay warm."
                    y "Oh, that was you?"
                    scene icecream2b
                    re "Guilty, that was a crazy night."
                    re "And then here I am, interfering again."
                    a "Believe me, there was nothing to interfere with tonight."
            if persistent.ldeverything:
                re "Oh yeah, The three of us ended up swimming naked in the pool."
                y "Yes, we played {i}Marco Polo{/i} in the nude."
                re  "I remember there being a sleep over, but we were all too tired to do more than sleep."
                y  "There I was lying naked between two naked women, and I fell right asleep."
                scene icecream2
                re "And someone was hogging all the covers."
                scene icecream2a
                a  "They were my covers."
                re "Yeah, but I ended up spooning with [persistent.playername] just to stay warm."
                y "Oh, that was you?"
                scene icecream2b
                re "Guilty, that was a crazy night."
                a "One of many with [persistent.playername]."
                re "Oh yeah? Tell me about the others..."
        else:
            scene icecream2b
            stop ambient fadeout 2
            "The three of you go to an ice cream parlor for sundaes"
            if not "rebgay" in persistent.reblist:
                $ persistent.reblist.append("rebgay")
            y  "So Rebecca, in our chat about the movie, I get the impression that you are...\nUh, whats the politically correct way to say it..."
            $ menuplaceX = 0.05
            $ menuplaceY = 0.7
            menu:
                re  "A Lesbian?  Yes I am a lesbian, I am into other girls, you got a problem with that?"
                "Not a problem with it at all, I know a few myself.":
                    re   "Great then we should get along just fine, why do you bring it up?"
                    y  "Well, you were making big hints about it, figure I would get it out there for you."
                    y "So now that it is out there, I'm curious to know how well did you two know each other in College?"
                "I don't have a problem with it, just a bit curious, I don't know that many lesbians.":
                    re "More than likely, you know a few, but for obvious reasons, we keep private about things."
                    y "That being cleared up, how well did you two know each other in College?"
                "Sorry, I can't help imagining you two together.":
                    re  "Sorry to bust your bubble, but we were never together {i}in that way{/i}."
                    scene icecream2a
                    a  "Well we were never lovers, true.  But, we did stuff."
                    re  "That doesn't count.  I have got more action doing bra fittings at work than that."
                    scene icecream2c
                    y "So, how well did you two know each other in College?"
            a  "We were in the same dorm for a couple of years, and ended up in a Dance class together."
            y  "You were both Dance majors?"
            scene icecream2b
            re "I was, Ariane just took a class, she was a Liberal Arts major."
            if not "major" in persistent.arilist:
                $ persistent.arilist.append("major")
            if not "rebmaj" in persistent.reblist:
                $ persistent.reblist.append("rebmaj")    
            a "I thought a dance class would be easy with my gymnastics background, it wasn't."
            scene icecream2a
            re "You should have taken ballet as a youngster instead of gymnastics."
            a "Hey a stint on the gymnastics team paid half my tuition."
            if not "gym" in persistent.arilist:
                $ persistent.arilist.append("gym")
            re "And my dancing job paid all of mine."
            a "You were a nude dancer at the Live Cabaret, \nthat is generally not something ballet dancers aspire to."
            if not "rebdance" in persistent.reblist:
                $ persistent.reblist.append("rebdance")
            re "No, but it paid nicely and I had a lot of fun doing it.\nI still occasionally go there for amateur nights."
            scene icecream2
            a "This is Rebecca in a nutshell, she is an attention whore.\nShe flaunts her sexuality because it gets her attention.\nShe dances naked on stage, just to get more attention."
            re "Why did you have to say something like that?"
            scene icecream2a
            a "It's true, isn't it?"
            re "Yes, but mentioning I was gay and and a nude dancer, turns guys on.\nCalling me an \"attention whore\" cheapens it, and turns them off.\nI was trying to help you out on your date, Ariane. I'm your wing man."
            scene icecream2b
            re "And speaking of attention whores, guess what Ariane did to pay for the other half of college."
            a "What!...  Shh!... Don't!...  Why are you doing this to me."
            if not "cheer" in persistent.arilist:
                $ persistent.arilist.append("cheer")
            $ menuplaceX = 0.9
            $ menuplaceY = 0.8
            menu:
                re "She was a CHEERLEADER!"
                "You were a cheerleader? That's so cool!":
                    scene icecream2
                    a "Yeah, yeah, rah, rah, sis boom bah, and all that shit."
                    a "I only did it for a couple of years until I made the gymnastics squad.\nI was glad to get out of there."
                "No way!  You just do not seem to be the \"cheerleader\" type Ariane":
                    scene icecream2
                    a "I liked doing flips and twists when people throw me in the air."
                    a "I didn't like acting all happy and cheerful, and shit, when the football team went 2 and 10 that year."
                    a "Which is why I gave it up after only two years.\nThat stuff was too crazy for me, I much preferred the Gymnastics squad."
                "You wouldn't happen to still have your uniform would you?":
                    scene icecream2
                    a  "Interested in a little role play or something? You are out of luck, it is long gone.\nTurned it in after I made the Gymnastics squad."    
        scene icecream3
        "More time passes..."
        if persistent.ldeverything:
            re "Wow you guys have had quite a few adventures, I especially like the strip club one."
            a "Wait weren't you at the strip club that night too?"
            re "I might have been, I sometimes go to amateur night.\nI used to work there you know."
            y "Yeah, I think you might have mentioned that before."
        a "Wow, we have been talking for almost an hour.\nMaybe we ought to wrap up this party."
        scene icecream4
        $ renpy.pause(1.0)
        scene icecream9
        re  "Whoa, was that lightning?  I saw no sign of a storm when we left the theater."
        play sound "distantthunder.ogg" fadein 1 fadeout 1
        a  "Yeah, that's freaky."
        scene icecream10
        card "A second strike of lightning nearby kills all the electricity downtown."
        scene black
        re "Oh great, well it is time to leave,  I need to run home before it starts raining."
        play sound "distantthunder.ogg" fadein 1 fadeout 1
        a "Oh that is right you don't have a car, how far is your house?"
        re "I have an apartment above the lingerie store, only about a half mile away.\nIf I leave now, I can get there before the rain starts."
        a "Don't be silly, it's not safe when it is this dark out.\nI can drive you home and make sure you get in safely."
        if not "helper" in persistent.arilist:
            $ persistent.arilist.append("helper")
        scene darkreb
        $ renpy.pause(3.0)
        card "With no moon or streetlights, it is really dark.\n\nThe three of you make it to the parking garage\nusing the light of your cell phones to see."
        a "My SUV does not have a roof, so I best be going before it rains myself."
        y "I could drive you both to your homes."
        a "No, that's OK, time to call it a night. Let's go, Rebecca."
        if persistent.ldrebecca:
            y "Very well goodnight to you both, catch you both later. \nI'll call you later Ariane."
        else:
            y "Very well goodnight to you both. Nice to meet you Rebecca. \nI'll call you later Ariane."
        scene black
        $ persistent.adatecount += 1
        if persistent.aending1 == False or persistent.epilogue > 0:
            $ persistent.aending1 = True
            show picenda2 at achievepos1 with moveinleft
            if persistent.story1 == False or persistent.epilogue > 0:
                $ persistent.story1 = True
                show picenda1 at achievepos2 with moveinleft
                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
            $ achievement_frame("Rebecca","And","Ariane", xcenter = 0.1, yalign = 0.1)
        card "You drive home safely despite the lack of working traffic lights,\n it starts raining just as you get home.\n\nWith nothing to do but sleep, you do,\npromising yourself you will sleep in tomorrow.\n\nTHE END"
        return  
            
label NightclubAriane:
        scene inline1
        "The club is full, and there is a line to get in.\nApparently there is a live band tonight and it has drawn quite a crowd.\nThe line does not seem to be moving much."
        "Ariane is reading the promotional poster."
        a "Tonight Only!! See local band Ameca Meca, premier their debut album, and kick off their national tour."
        a "A Celebrity Extravaganza not to be missed."
        a "What celebrities can an album premiere from some unknown band generate?"
        scene inline2
        if not "lizard" in persistent.wenlex:
            $ persistent.wenlex.append("lizard")
        "As if on cue a limo pulls up and the sportscaster and weather girl from channel 12 news get out."
        "They stand by the car a while, and people are pulling out cell phones\nwith cameras trying to get a picture of them."
        scene inline1
        a "That's the best \"celebrities\" they could come up with?"
        y "Are there any big celebrities in this town at all?"
        a "Well there is Jake Herman, our all star third baseman.\nSorry if I sound like a little girl, but he's a \"hunk\"."
        if abaseball == 1:
            y "Jake Herman played in that marathon extra inning game tonight. \nLast score I saw was 9-9 in the bottom of the 12th."
            y "I doubt Jake Herman would make it to a concert after that.\nMaybe I should ask the sportscaster from channel 12 what the final score was."
            "Some eavesdropper mentions that we won 11-10 in 14 innings."
            y "(to eavesdropper) Thanks.\n(Back to Ariane) Any other famous local celebrities? I'm fairly new here, it's nice to know these things."
        else:
            y "Any other famous local celebrities? I'm fairly new here, it's nice to know these things."
        a "Other than a couple of \"has been\" rock stars \nand the newest {i}Loco-Cola{/i} supermodel, Roxy something, I can't think of anyone."
        a "Sorry, this town is kind of lame."
        y "Well maybe a year from now we can add the band Ameca Meca to the list."
        "Ariane does not say anything for a while, and the line continues not to move."
        a "Listen, I'm not in the mood for a concert anymore. Let's leave."
        y "OK, we can go."
        scene garage1
        stop ambient fadeout 1
        "You walk her back to her SUV, in the parking garage\nwhere your car is still parked."
        if persistent.ldhotdate and not persistent.ldeverything:
            a "Well, here we are.  I learned something about myself tonight. I suck at making choices."
            a "Call me Monday, and we'll make plans, together this time."
            y "OK Monday, sounds like a plan."
        elif not persistent.ldhotdate and not persistent.ldeverything:
            a "Well, here we are.  Your car is just over there, maybe we should just end the date here."
            y "Are you sure? It still seems early."
            a "True, but between the bar incident, the theater incident,\nand the pointless waiting in line, I say we cut our losses."
        else:
            a "Well challenge failed. We tried to make a lame date amazing\nand it still turned out lame."
            y "One stumble does not make us failures.\nWe could still go to your house and..."
            a "Tempting, but I'm not in the mood for consolation sex.\nLet's just cut our losses, and try again another night."
            y "Very well Spirit, your Muse will leave you for tonight."
        "She gives you a goodnight kiss.  Then gets in her car to drive away."
        scene black
        $ persistent.adatecount += 1
        if persistent.aending4 == False or persistent.epilogue > 0:
            $ persistent.aending4 = True
            show picenda5 at achievepos1 with moveinleft
            if persistent.story1 == False or persistent.epilogue > 0:
                 $ persistent.story1 = True
                 show picenda1 at achievepos2 with moveinleft
                 $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
            $ achievement_frame("Celebrity","Sightings","", xcenter = 0.1, yalign = 0.1)
        card "You go home alone, again. \n\nand to make an already lame night worse, a storm hits on your way home.\nBy the time you reach your home, you have no electricity.\n\nSo you go to bed early."
        return
        
label ToArianesHouse:
        a "OK, Since we are both parked in the parking garage, we may\nas well save another trip here.  Just follow me home.\nYou know how to get there."
        stop ambient fadeout 1
        if not persistent.ldhotdate:
            scene freeway3
            stop music fadeout 1
            "You follow Ariane back to her place."
            scene gasstation2
            $ menuplaceX = 0.5
            $ menuplaceY = 0.8
            menu:
                "She stops at a convenience store on the way home."
                "Stop at the store as well":
                    scene gasstation3
                    a "Just realized I have nothing at home in the adult beverage department."
                    y "Oh, OK. Let me pay for that."
                    sto "OK, Is there anything else you need?"
                    y "No, I'm good."
                    a "Thanks Jessie." 
                "Continue driving to her house.":
                    scene arihouseoutside
                    "You wait around outside for Ariane."
                    scene ariwhiskey
                    "She arrives a few minutes after you, with a bottle of liquor."
            scene arihouse7        
            a "Two things we can do tonight, drinking or dancing"
            $ menuplaceX = 0.3
            $ menuplaceY = 0.3
            menu:
                a "What do you want to do first?"
                "Break out the liquor":
                    scene arihouse8
                    "Ariane pours you a glass."
                    scene arihouse9
                    "Then she takes a swig herself."
                    scene arihouse10
                    a  "That's enough drinking for now, Let's dance."
                "Crank up the tunes!":
                    scene arihouse10
                    a "Got a cool hip hop CD to try out."
            if renpy.exists("clubdance2.mp3"):
                play music "clubdance2.mp3"
            else:
                play music "fashionista.ogg"
            scene aridance1
            a  "I love dancing.  WOOOOO..."
            $ renpy.pause(5)
            scene arihouse9
            a  "OK time for a drink."
            scene aridance3
            a  "Back to dancing"
            $ renpy.pause(5)
            if persistent.ldeverything:
                scene arihouse9
                a "It's about time for a little...."
                scene aridance8
                if not "tits" in persistent.arilist:
                    $ persistent.arilist.append("tits")
                a  "dancing in our undies!"
            card "The cycle between drinking and dancing continues for a while until..."
            scene black
            stop music
            a "(drunkenly)  Hey the music stopped!"
            y "Uhhh, maybe because the electricity went out?"
            a "The electricity went out?"
            y "Yeah, it did. Look outside, all the houses are dark, as are the street lights."
            a "Good, 'cause I thought I was passing out."
            if renpy.exists("clubdance2.mp3"):
                play music "clubdance2.mp3"
            else:
                play music "fashionista.ogg"
            "The music starts again."
            y "Wait, how is that possible?"
            a "It's a portable stereo, silly, it can run on batteries... PARTAY!"
            y "Actually, maybe we should use it to listen \nto the local news, find out what's going on."
            stop music
            a "(dejectedly) Dammit, that sounds sensible.  You find a station, I'll find the candles."
            if not persistent.ldeverything:
                scene arihousedrunk1
                "Ariane manage to light some candles,\nbut soon she passes out drunk on the couch."
                "The radio says the electricity is out in most of the city, due to a freak lightning storm."
                "Looks like you are stuck here for the night."
                $ menuplaceX = 0.8
                $ menuplaceY = 0.2
                menu:
                    "What do you want to do?"
                    "Carry Ariane to bed":
                        scene black
                        "You pick up Ariane off the couch, she wakes up groggily as you carry her."
                        a  "Thanks. Just sit me down on the bed."
                        "You go back in the living room and grab the candles."
                        scene arihousedrunk3 
                        if not "tits" in persistent.arilist:
                            $ persistent.arilist.append("tits")
                        a "You can sleep here with me if you want.\nJust no funny business."
                        y "Agreed"
                        scene black
                        $ persistent.adatecount += 1
                        "You strip to your underwear, blow out the candles, then climb in bed."
                        if persistent.aending7 == False or persistent.epilogue > 0:
                            $ persistent.aending7 = True
                            show picenda8 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("Getting","Drunk At","Ariane's", xcenter = 0.1, yalign = 0.1)
                        card "The next morning, you both have hangovers.\n\nYou wonder if you should stay, but Ariane would rather you leave,\n\n\"Call me in a couple of days after my head stops pounding, OK?,\" she says.\nYou agree to call her then.\n\nTHE END"
                        return
                    "Leave Ariane alone":
                        "You let her sleep it off. Meanwhile, there is a big\ncomfy bed waiting for you to sleep on it, which you do."
                        scene black
                        $ persistent.adatecount += 1
                        if persistent.aending7 == False or persistent.epilogue > 0:
                            $ persistent.aending7 = True
                            show picenda8 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("Getting","Drunk At","Ariane's", xcenter = 0.1, yalign = 0.1)
                        card "The next morning, you both have hangovers.\n\nYou wonder if you should stay, but Ariane would rather you leave,\n\n\"Call me in a couple of days after my head stops pounding, OK?,\" she says.\nYou agree to call her then.\n\nTHE END"
                        return
                    "Finish off the bottle":
                        "You pass out next to Ariane on the couch"
                        scene black
                        $ persistent.adatecount += 1
                        if persistent.aending7 == False or persistent.epilogue > 0:
                            $ persistent.aending7 = True
                            show picenda8 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("Getting","Drunk At","Ariane's", xcenter = 0.1, yalign = 0.1)
                        card "The next morning, you both have hangovers.\n\nYou wonder if you should stay, but Ariane would rather you leave,\n\n\"Call me in a couple of days after my head stops pounding, OK?,\" she says.\nYou agree to call her then.\n\nTHE END"
                        return
                    "Check to see if Ariane is wearing underwear":
                        scene arihousedrunk2 
                        if not "tits" in persistent.arilist:
                            $ persistent.arilist.append("tits")
                        "Ariane is wearing panties under her skirt, but she is not wearing a bra." 
                        "You pull her skirt back down, then let her sleep it off. \nMeanwhile, there is a big comfy bed waiting for you to sleep on it, which you do."
                        scene black
                        $ persistent.adatecount += 1
                        if persistent.aending7 == False or persistent.epilogue > 0:
                            $ persistent.aending7 = True
                            show picenda8 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("Getting","Drunk At","Ariane's", xcenter = 0.1, yalign = 0.1)
                        card "The next morning, you both have hangovers.\n\nYou wonder if you should stay, but Ariane would rather you leave,\n\n\"Call me in a couple of days after my head stops pounding, OK?,\" she says.\nYou agree to call her then.\n\nTHE END"
                        return
            else:
                scene arihousedrunk4
                "Ariane manage to light some candles,\nbut soon she passes out drunk on the couch."
                "The radio says the electricity is out in most of the city, due to a freak lightning storm."
                "Looks like you are stuck here for the night."
                $ menuplaceX = 0.8
                $ menuplaceY = 0.2
                menu:
                    "What do you want to do?"
                    "Carry Ariane to bed":
                        scene black
                        "You pick up Ariane off the couch, she wakes up groggily as you carry her."
                        a  "Thanks. Just sit me down on the bed."
                        "You go back in the living room and grab the candles."
                        scene arihousedrunk3 
                        if not "tits" in persistent.arilist:
                            $ persistent.arilist.append("tits")
                        a "Stay the night?"
                        y "Of course."
                        scene black
                        "You blow out the candles, then climb in bed.\nYou reach over to Ariane, but she is already asleep again."
                        scene aricocoa
                        card "Next Morning"
                        a "Morning Muse, I made coffee."
                        y "Thanks, love some."
                        a "So, how does last night rank among our past dates?"
                        y "I'll tell you when the room stops spinning. What do you think?"
                        a "I wish I could remember what all happened."
                        scene black
                        $ persistent.adatecount += 1
                        if persistent.aending7 == False or persistent.epilogue > 0:
                            $ persistent.aending7 = True
                            show picenda8 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("Getting","Drunk At","Ariane's", xcenter = 0.1, yalign = 0.1)
                        card "The two of you enjoy your Sunday morning together.\n\nTHE END"
                        return
                    "Leave Ariane alone":
                        "You let her sleep it off. Meanwhile, there is a big\ncomfy bed waiting for you to sleep on it, which you do."
                        scene black
                        card "Next Morning"
                        scene aricocoa
                        a "Morning Muse, I made coffee."
                        y "Thanks, love some."
                        a "So, I wokeup on the couch, and now I am all stiff and sore."
                        y "Sorry, you passed out there and you looked all peaceful."
                        a "Well, I need to go back to bed. Think you can make it home?"
                        y "Yeah, I think I've sobered up enough to drive home."
                        a "Might want to take some aspirin before you go."
                        scene black
                        $ persistent.adatecount += 1
                        if persistent.aending7 == False or persistent.epilogue > 0:
                            $ persistent.aending7 = True
                            show picenda8 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("Getting","Drunk At","Ariane's", xcenter = 0.1, yalign = 0.1)
                        card "You get home and go right to bed.\nAnother crazy night with Ariane ends in a pounding headache.\n\nTHE END"
                        return
                    "Finish off the bottle":
                        "You pass out next to Ariane on the couch"
                        scene black
                        card "Next Morning"
                        scene arimorning
                        a "Wake up sleepy head."
                        y "Oh man, we fell asleep on the couch."
                        a "I feel like crap too, and sore from sleeping on the couch."
                        y "Ditto, I shouldn't have finished off the bottle."
                        a "I'm going to the bed if you want to join me."
                        scene black
                        $ persistent.adatecount += 1
                        if persistent.aending7 == False or persistent.epilogue > 0:
                            $ persistent.aending7 = True
                            show picenda8 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("Getting","Drunk At","Ariane's", xcenter = 0.1, yalign = 0.1)
                        card "You both adjourn to Ariane's bed,\nand sleep for another two hours.\n\nTHE END"
                        return         
        else:
            ## You have had sex
            a  "Hey, by the way, could you stop at a convenience store on the way there and get some beer?"
            scene freeway3
            stop music fadeout 1
            "You follow Ariane back to her place"
            scene gasstation4
            "As promised, you stop at a convenience store on the way to her place."
            scene gasstation5
            $ menuplaceX = 0.2
            $ menuplaceY = 0.7
            menu:
                sto "Do you just need the beer? Or something else?"
                "Just the beer thanks":
                    sto "That will be ten dollars even then."
                "I'll take a HooBoy, condoms, a bottle of burbon, and a pack of bubble gum, too":
                    sto "That will be $27.52"
            "You get in the car and head back to Ariane's"        
            scene arihouse6            
            if not "nude" in persistent.arilist:
                $ persistent.arilist.append("nude")
            y "I got the beer, sorry I only got five, well actually I got six but one...  WHOA!!"
            a "I want to forget about tonight.  It did not go the way I was hoping."
            a "So let's instead go back to our first date and start again where we left off."
            y "I was so hoping you would say that."
            if not "sex" in persistent.arilist:
                $ persistent.arilist.append("sex")
            scene arisex
            play sound "sexbed.mp3" fadein 0.1
            $ renpy.pause(13)
            scene black
            stop sound fadeout 2
            card "The next morning you hear on the news that a freak thunderstorm \npassed through town knocking out electricity for nearly an hour."
            card "Neither of you ever noticed, because you were enjoying yourselves too much."
            $ persistent.adatecount += 1
            if persistent.aending9 == False or persistent.epilogue > 0:
                $ persistent.aending9 = True
                show picenda9 at achievepos1 with moveinleft
                if persistent.story1 == False or persistent.epilogue > 0:
                    $ persistent.story1 = True
                    show picenda1 at achievepos2 with moveinleft
                    $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                $ achievement_frame("","Makeup Sex","", xcenter = 0.1, yalign = 0.1)
            card "The two of you enjoy your Sunday together.\n\nTHE END"
        return
        
label MountainDrive:
        stop ambient fadeout 4
        if not persistent.ldhotdate and not persistent.ldeverything:
            a "All night you have been letting me make all the decisions."
            y "Well on our last date, I made all the decisions, tonight it's your turn."
            a "That's so sweet."
            y "Come up with something that you think we will both enjoy."
            if persistent.ldmtnphotos:
                a "OK, I got an idea, and I know you will like it, because we did it before."
            else:
                a "OK, I got an idea. Despite all the problems,we have been following\na \"traditional\" date pattern tonight.  Dinner, movie, and then..."
        elif persistent.ldhotdate and not persistent.ldeverything:
            a "All night you have been letting me make all the decisions."
            y "Well that is the way you wanted it."
            a "I thought I did, but it seems I prefer a little give and take."
            y "How about a compromise, come up with something that you think we will both enjoy."
            if persistent.ldmtnphotos:
                a "OK, I got an idea, and I know you will like it, because we did it before."
            else:
                a "OK, I got an idea. Despite all the problems,we have been following\na \"traditional\" date pattern tonight.  Dinner, movie, and then..."
        else: 
            a "You want me to pick what to do next?"
            y "You may have picked out the movie, \nbut it was my choice to go to the movies in the first place."
            a "Well like you, I'm fresh out of ideas we have not already done."
            y "Let's do something we have already done and do it differently then."
            a "Hmm, a good idea just popped into my head,"
        y "What have you got in mind?"
        a "Let's get in my car, and I'll drive you there."
        scene mountaindrive1
        if persistent.soundtrack == True:
            play song "dancingmice4.ogg"   
        "Ariane heads out of town, driving into the mountains."
        if not persistent.ldeverything:
            a  "So, a traditional date consists of dinner and a movie,\nand of course a make out session in a car at some make out spot."
            if persistent.mtnphotos:
                a "Remember the look out point we went to last time?  That is where we are going."
                y "Sounds like a plan I can live with."
            else:
                a "Up in the mountains, there is a spot where you\ncan see the whole city. It is romantic there at night."
                y "Sounds interesting, I can hardly wait."
            scene mountaindrive2    
            "It's a slow twisty road to the top, but you finally arrive,\nonly to find you are not alone."
            scene mountaindrive3
            "Two other cars are here, and from the steamed up windows, \nthey are unlikely to care about you two."
            y "It looks like a couple of other couples had the same idea."
            a "Yeah, oh well, I've complained enough tonight, I'm over it."
            a "I'm going to drive to the edge of the scenic view near those trees.\nThe view is obscured, but we will have some privacy there."
            y "Sounds like a good plan."
        else:
            y "So are we going to the scenic view again where we did the photo shoot?"
            a "And this time no camera, we'll just have to find something else to do."
            y "I can think of a few things."
            a "Dinner, movie, and a secluded make out point\n...finally a traditional date."
            scene mountaindrive2    
            "It's a slow twisty road to the top, but you finally arrive,\nonly to find you are not alone."
            scene mountaindrive3
            "Two other cars are here, and from the steamed up windows, \nthey are unlikely to care about you two."
            y "It looks like a couple of other couples had the same idea."
            a "Well see that just make things more interesting."
            a "I'm going to drive to the edge of the scenic view near those trees.\nThe view is obscured, but we will have some privacy there."
            y "Privacy from the cars on the road, but not the other two cars."
            a "If they are not already distracted, let them watch.  Maybe they can learn a thing or two."
        scene aricar1
        a "Well here we are, so are you going to kiss me or what?"
        scene aricar2
        $ renpy.pause(4.0)
        scene aricar1
        a "I have been wanting that to happen all night.  Shall we do it?"
        y "I'm not sure we can, not in this car."
        y "Even away from the other cars, without doors or windows,\nthe other cars will see what we are doing."
        $ menuplaceX = 0.55
        $ menuplaceY = 0.5
        menu:
            a "Is the lack of privacy a problem for you?"
            "Yes":
                a "Well I don't give a damn what they think.\nShut up and take your shirt off."
            "No":
                a "Then, shut up and take your shirt off."
        "You take your shirt off.  Ariane drapes the shirt over the rail bars behind your seat hiding the other cars view."
        scene aricarback1
        show aricar3  
        "She then gets on your lap, straddling her legs around you."     
        scene aricarback2
        show aricar3 
        "You start making out in the car."
        scene aricar4 #carback3
        "Ariane is unzipping your fly."
        scene aricar4a #carback4
        "Ariane straddles you, your cock is out, you manoever along her leg up her skirt\nadjusting her panties so you can access her pussy."
        scene aricarback5
        show aricar3:
                xalign 0.5 yalign 0.5
                ease 0.5 yalign 0.6
                ease 0.5 yalign 0.5
                repeat
        "The two of you are fucking in a public place."
        if not "sex" in persistent.arilist:
            $ persistent.arilist.append("sex")
        "It is not very comfortable for either of you, but you both revel in the stealth."
        scene aricar5 #carback7
        "Ariane feels daring enough to unbutton her top."
        scene aricarback8
        if not "tits" in persistent.arilist:
            $ persistent.arilist.append("tits")
        show aricar6:
                xalign 0.5 yalign 0.5
                ease 0.5 yalign 0.6
                ease 0.5 yalign 0.5
                repeat
        $ renpy.pause(5.0)
        card ""
        scene aricar7a #carback6 and 9
        stop song
        play sound "thunder.ogg"
        $ renpy.pause(3.0)
        scene aricar8 #carback6
        a "What the hell was that?!"
        y "Thunder and lightning.\nA very quickly developing storm for sure."
        scene aricar9a
        "Startled, Ariane gets off of you.\nYou quickly put your dick back in your fly and zip up."
        a "Maybe we should get out of here before it starts raining."
        scene black
        show aricar9b
        play sound "thunder.ogg"
        $ renpy.pause(3.0)
        scene aricar9c
        a "Wow, did you see the lightning strike the hydroelectric dam."
        y "No actually I was busy staring at your tits."
        a "Well, maybe you noticed it has gotten darker, the strike\ntook out the main generators, there are no lights in the city now."
        scene aricar9d
        "Ariane turns on the headlights and starts the car."
        a "I think it is time to head back."
        scene mountaindrive1
        show rain fall
        play ambient "rain.ogg" fadein 2
        if not persistent.ldeverything:
            a "(laughing) Can you believe this night?"
            y "I still don't get the joke."
            a "Bar incident, ruined dress, stuck eating fast food, \nannoying girl at the theater, boring movie, and now just as I was\n blissfully forgetting, the whole bad night, we get rained on." 
            y "(You join in laughing) Yeah, what else could possibly go wrong?"
            a "Don't jinx it any further."
        else:
            a "So how does tonight rank among our past dates?"
            y "What should I base it on?"
            a "Bar incident, ruined dress, stuck eating fast food, \nannoying girl at the theater, boring movie, and now we get rained on."
            y "Well on the fun scale it ranks pretty low, but it already ranks pretty high on the unforgettable scale."
            a "Funny how those two are so mutually exclusive."
        scene ariwet
        show rain fall
        "When you get to Ariane's home you are both soaked."
        a "Come on in out of the rain, at least the electricity is back on.\nThere are towels in the bathroom, and I can throw your clothes in the dryer." 
        stop ambient fadeout 1
        scene arirobe1
        "She goes into her bedroom and comes out in a robe"
        a "What do you say to some hot cocoa."
        y "Sounds nice."
        scene aricocoa
        y "Wow this is great cocoa, what's your recipe?"
        a "Milk, chocolate mix, and microwave for 3 minutes."
        y "Tastes better than it sounds."
        a "Your clothes aren't dry, yet, and it is still raining"
        scene arihousehallway2
        show arirobe3 at center0
        hide arirobe3 with moveoutbottom
        a "Why don't you spend the night?"
        y "OK! If you insist..."
        scene aribedroom1
        if not "nude" in persistent.arilist:
            $ persistent.arilist.append("nude")
        card ""
        a "Let's get back to where we left off, when we were rudely interrupted by Mother Nature"
        y "Hmm, what were we doing then...  Oh yeah we were having sex."
        scene arisex
        play sound "sexbed.mp3" fadein 0.1
        $ renpy.pause(13)
        stop sound fadeout 1
        scene arimorning
        card "Next morning"
        if not persistent.ldeverything:
            a "I'm going to have to drive you downtown to get your car."
            y "No rush, it's a lazy Sunday morning."
            a "Here's to a trouble free Sunday."
        else:
            a "So Muse, I'm going to have to drive you downtown to get your car."
            y "No rush Spirit, it's a lazy Sunday morning."
            a "Here's to a trouble free Sunday."
        scene black
        $ persistent.adatecount += 1
        if persistent.aending10 == False or persistent.epilogue > 0:
            $ persistent.aending10 = True
            show picenda10 at achievepos1 with moveinleft
            if persistent.story1 == False or persistent.epilogue > 0:
                $ persistent.story1 = True
                show picenda1 at achievepos2 with moveinleft
                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
            $ achievement_frame("Safety","Pullout","", xcenter = 0.1, yalign = 0.1)
        card "The two of you enjoy your Sunday morning together.\n\nTHE END"
        return
        
label HPAriane:
    a "Can't think of a thing."
    y "Doing nothing. Sounds like like fun."
    a "Ha Ha Mr. sarcasm.  Let's walk downtown and see what we can find."
    scene inline1
    y "Want to stand in line and try to get into the concert?"
    a "Doesn't sound very fun.  Wish I could think of something better to do."
    scene inline3
    $ renpy.pause(2.0)
    mwf "Hey couldn't help overhearing, got an invite to a house party,\nbut the girfriend wants to go to this concert instead."
    mwf "It's yours if you want."
    a "Sure I'll take the invite off your hands."
    scene inline1
    $ menuplaceX = 0.62
    $ menuplaceY = 0.6
    menu:
        a "Want to go to a house party?"
        "Let's stick with the concert":
            a "Looking over the flyer you might have made the right choice."
            a "Sponsored by the Adult Channel? Must consent to be filmed?"
            a "On the other hand there is the concert poster:"
            a "Tonight Only!! See local band Ameca Meca, premier their debut album, and kick off their national tour."
            a "I think we need a third choice that's less crowded.\nLet's keep going down the street."
            jump cantina
        "It's your turn to choose, remember?":
            a "Great house party it is, Let's take your car."
            stop ambient fadeout 2
            scene hpfrontariane
            a "I have not been to a house party since college."
            y "Yeah, these \"keggers\" tend to attract the underage drinking crowd"
            a "That's not an age comment I hope."
            y "No of course not, you look great for, uh..."
            if not "age" in persistent.arilist:
                $ persistent.arilist.append("age")
            a "23, I graduated at age 21."
            y "Thanks, you look so good I never felt the need to ask."
            a "Nice recovery there, [persistent.playername]."
            scene hparty1
            play ambient "partynoise.ogg" fadein 3
            a "Hey they got a pool.  I see a few people in swim suits."
            y "I don't see anyone swimming though."
            a "Let's go get a couple of glasses of whatever swill they are serving in those red cups."
            y "Sounds like a plan."
            scene hparty2ari
            play song "partytechno.mp3" fadein 10
            a "Hey Rick, Hey Lana, haven't seen you two in a while, whats up?"
            lana "Hey Ariane, We are working the party."
            a "Cool...  So Lana, I can't help notice you don't have a shirt on, interesting fashion statement."
            lana "Yeah, they are paying me to run around topless, Rick is my body guard."
            a "Interesting, why would they do that?"
            lana "This party is sponsored by the Adult Channel."
            a "That premium porn channel on cable?"
            lana "Yeah, they are filming the party and they want people to know it's OK to get naked here."
            a "Wow, that's nice of them, good to know.\nCould you hold my drink a second?"
            scene hparty3ari
            lana "Sure."
            $ renpy.pause(3)
            scene hparty4ari
            if not "hp" in persistent.arilist:
                $ persistent.arilist.append("hp")
            if not "tits" in persistent.arilist:
                $ persistent.arilist.append("tits")    
            a "Ahh, there.  Much better."
            a "Well nice catching up with you, Lana.\nAnd Rick, good job standing there looking mean."
            scene hparty5ari
            $ menuplaceX = 0.1
            $ menuplaceY = 0.7
            menu:
                a "Hang on to my shirt will you?"
                "Are you sure you want to run around the party shirtless?":
                    a "Just supporting my friend Lana."
                    if not "helper" in persistent.arilist:
                        $ persistent.arilist.append("helper")
                    y "That's nice of you but there is a porn channel filming here you know.\nYou want your breasts on national TV?"
                    a "You make an interesting argument, and I'll have to answer: Yes, I'm cool with it."
                    a "And let me ask you something in return, [persistent.playername]."
                    y "OK, shoot."
                    a "Why aren't we dancing?"
                "OK, want to dance?":
                    a "Awesome idea!"
            show hparty6ari
            $ renpy.pause(5.0)
            card ""
            scene hparty7ari
            stop song fadeout 5
            a "The guy behind the camera threw me this t-shirt,\nguess they saw enough of my tits."
            y "Is that possible?"
            a "(laughs) Well maybe, I guess they want to see other girls tits now.\nThey are starting a wet t-shirt contest."
            scene hparty8ari
            director "OK everybody what do you think?"
            play song "applause.ogg"
            "The girls scream YAY!, the guys watching the spectacle are hooting and hollering."
            scene hparty9ari
            show rain fall
            play sound "distantthunder.ogg" fadein 1
            play ambient "rain.ogg" fadein 2
            $ renpy.pause(3)
            "Then suddenly, everybody had a wet t-shirt"
            scene hparty10ari
            show rain fall
            a "Wow best wet t-shirt contest ever!  Let's get out of here."
            scene black
            stop ambient fadeout 2
            card "As you approach downtown you discover the electricity is out.\n\n You drop Ariane off at her car."
            scene darkari2
            a "Well that was a crazy party, one for the books.\nLet's call it a night before it gets crazier."
            y "Ok, we'll say goodnight here. (you kiss her)"
            y "Traffic is crazy, right now without working traffic lights\nso be careful.  Text me when you get home safe."
            a "Will do!"
            scene black
            $ persistent.adatecount += 1
            if persistent.aending6 == False or persistent.epilogue > 0:
                $ persistent.aending6 = True
                show picenda7 at achievepos1 with moveinleft
                if persistent.story1 == False or persistent.epilogue > 0:
                    $ persistent.story1 = True
                    show picenda1 at achievepos2 with moveinleft
                    $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                $ achievement_frame("House Party","With","Ariane", xcenter = 0.1, yalign = 0.1)
            card "As you get home, you receive a text, \"safe and sound\"\n\nThe electricity comes back on, but you turn out the lights and go to bed.\n\nTHE END"
            return

label cantina:
    scene cantina1
    a "Let's go in here."
    y "Do you have a sudden craving for Tacos?"
    a "No, I'm still full from the double burger.\nThis place has a bar, too."
    stop ambient
    scene cantina2
    if persistent.soundtrack == True:
        play song "mexicanromance.ogg" fadein 0.1
    a "Señor, traigame una tequila, por favor."
    scene cantina3
    $ renpy.pause(2)
    scene cantina3a 
    $ renpy.pause(2)
    scene cantina3 
    a "Una mas, por favor?"
    scene cantina3a 
    y "I didn't know you speak Spanish."
    scene cantina4
    a "I'm not fluent, but I know the important words:\ntequila, cerveza, marijuana, chingame"
    "The girl next to Ariane laughs."
    scene cantina5
    a "What? Something wrong with my accent?"
    mex "Well yeah, but what you said was funny."
    mex "I'm Lydia by the way."
    a "Hey Lydia, I'm Ariane."
    l "Nice to meet you. You were that girl from the gym this morning."
    a "You were there?"
    l "Yeah, I was on a treadmill watching you on the balance beam\nYou are a pretty good at that thing."
    a "Thanks, and I recognize you from the poster I saw five minutes ago.\nYou are in that band Ameca Meca, right?"
    l "Guilty, it's our big night, and I'm a nervous wreck."
    a "And you decided tequila shots are the answer?"
    l "Only had two, just waiting for the buzz to kick in."
    a "I see."
    a "So, tell me Lydia, where did the name Ameca Meca come from?"
    l "It's the name of a village in central Mexico,\nmy Abuelos were born and raised there. Thought the name sounded cool."
    a "It does, and it's sweet to be reminded of your\ngrandparents when you hear the name."
    scene cantina6
    l "Yeah, but lately it reminds me more of my lost love."
    a "Oh?"
    l "The band used to be a foursome, two couples."
    l "Then our keyboardist decided she prefers guys, and left me and the band."
    a "That Bitch!"
    l "Yeah, I wrote a song about her, it's the song that landed\nour record deal and our first single."
    a "How Taylor Swift of you."
    l "Thanks, but we used to make out before concerts to relax our nerves."
    l "It worked better than this Tequila.\nApparently, all Tequila does is make me open up to complete strangers."
    scene cantina7
    $ renpy.pause(5)
    scene cantina8 
    l "What was that for?"
    a "You seem to need it, and apparently Tequila makes me kiss complete strangers."
    if not "helper" in persistent.arilist:
            $ persistent.arilist.append("helper")
    l "Good enough."
    scene cantina9
    $ renpy.pause(8)
    scene cantina8
    l "Oh, I'm sorry..."
    a "Don't be."
    l "But, you are not gay."
    a "You can tell by only a couple of kisses?"
    l "You are with this guy aren't you?"
    scene cantina10
    if persistent.ldeverything:
        a "Yes, this is [persistent.playername], he is my muse.\nHe does not mind me kissing girls in front of him."
        y "No, not at all."
    elif persistent.ldhotdate:
        a "Yes, this is [persistent.playername], we are on our second date.\nHe knows I'm not gay, either."
        y "Yeah, we did it.  Don't worry, I don't mind."
    else:
        a "Yes, this is [persistent.playername], we are on our second date."
        y "We are not in a relationship, just dating."
    y "If it helps, I could make out with you, too."
    l "No, that's OK. I'm feeling more relaxed now."
    l "By the way, What time is it?"
    y "It's 10:15."
    scene cantina6
    l "Ay Dios Mio, the concert starts in 15 minutes."
    a "Can't start without you, you better hurry though."
    scene cantina5
    l "Why don't you two come with, as my guests backstage."
    scene cantina4
    a "[persistent.playername], are you OK with that?"
    y "Sure, let's go."
    stop song fadeout 3
    scene backstage1 
    play ambient "partynoise.ogg" fadeout 1 fadein 1
    drum "Lydia, where have you been?"
    l "Don't worry, I'm ready to go on."
    scene backstage2
    l "A kiss for good luck?"
    scene backstage3
    $ renpy.pause(3)
    scene backstage2
    a "Good luck!"
    scene backstage4
    play sound "applause.ogg" fadein 0.1
    $ renpy.pause(3)
    scene backstage5
    if renpy.exists("rock.mp3"):
        play song "rock.mp3"
    else:
        play song "amecameca.mp3"
    $ renpy.pause(5.0)
    "The band sounds awesome, Lydia is having a good time on stage."
    scene black
    stop song
    play ambient "partynoise.ogg" fadein 0.1
    play sound "distantthunder.ogg" fadein 1 fadeout 1
    "That is until the lights go out"
    scene backstage6
    liz "Wendy, see if you can find the box of glow sticks in the supply closet."
    liz "Anyone know anything about old generators?"
    a "How old are we talking?"
    liz "Dates back to when this building was a medical center."
    a "That's before I was born, but I can give it a shot.\nDad was a mechanic, he taught me a few things."
    if not "mech" in persistent.arilist:
        $ persistent.arilist.append("mech")
    liz "Come with me then."
    scene backstage7
    w "I'm going to hand these out to the handful of people that haven't left yet."
    play ambient "generator.ogg" fadein 3
    drum "Great, so much for the concert."
    l "Wait what's that sound?"
    scene backstage8
    play sound "applause.ogg" fadein 0.1
    drum "Whoa, let there be light."
    scene backstage9 
    a "Piece of cake!"
    liz "Got enough gas for an hour of power, if you want to get back on stage."
    scene backstage10
    l "Let's Rock and Roll, people!"
    scene backstage5
    stop ambient
    play ambient "partynoise.ogg" fadeout 1 fadein 1
    play sound "applause.ogg" fadein 0.1
    if renpy.exists("rock.mp3"):
        play song "rock.mp3"
    else:
        play song "amecameca.mp3"
    "The band finishes their set with a much smaller crowd."
    "Mr Lizzard opens the doors to anybody looking to escape the rain,\nby the end of the set, the crowd is pretty big again."
    scene backstage2
    stop song fadeout 3
    l "So what did you guys think of the show?"
    a "You guys sounded awesome. (You agree with her)"
    l "Ariane, you really helped us out tonight.\nI feel something with you I haven't felt in a while."
    a "I see. ... but I'm not..."
    l "I know, I'm just ... looking to hang out.\nWith the both of you if that is all right."
    l "I don't mind being a \"tercera\". The band\nleaves tomorrow so there won't be another chance for months."
    if not persistent.ldeverything:
        if not persistent.ldhotdate:
            a "I'm sorry Lydia. We're just on our second date,\nand we haven't even... It would be too complicated."
        else:
            a "I'm sorry Lydia. We're just on our second date,\nand it would complicate things if you joined us."
        a "Here's my number. Call me when you get back.\nWe'll have dinner and you can tell me about the tour."
        l "(a little sad) I understand, it was a long shot\nbut, I'll definitely call you on that dinner."
        a "In the mean time, go enjoy the after party.  You deserve it!"
        stop ambient fadeout 1
        scene garage1
        card "The two of you leave.\nThe lights are back on.\n\nYou cross the street to the garage."
        a "Sorry, I don't feel like staying for the after party.\nLet's go back to my place instead. We both have\nour cars here.  Just follow me home, you know the way."
        a "Hey, by the way, could you stop at a convenience store on the way there and get some beer?"
        scene freeway3
        "You follow Ariane back to her place"
        scene gasstation4
        "As promised, you stop at a convenience store on the way to her place."
        scene gasstation5
        $ menuplaceX = 0.7
        $ menuplaceY = 0.6
        menu:
            sto "Do you just need the beer? Or something else?"
            "Just the beer thanks":
                sto "That will be ten dollars even then."
            "I'll take a HooBoy, condoms, a bottle of burbon, and a pack of bubble gum, too":
                sto "That will be $27.52"
        "You get in the car and head back to Ariane's"        
        scene arihouse6            
        if not "nude" in persistent.arilist:
            $ persistent.arilist.append("nude")
        y "I got the beer, sorry I only got five, well actually I got six but one...  WHOA!!"
        if not persistent.ldhotdate:
            a "You were really cool tonight. I'm not sure what that was with Lydia,\nbut it got me in a sexy mood, and we haven't done it yet,"
            a "So let's do it!"
        else:
            a "You were really cool tonight. I'm not sure what that was with Lydia,\nbut it got me thinking about our first date."
            a "So let's just top this odd night off with a nice fuck."
        y "I was so hoping you would say that."
        if not "sex" in persistent.arilist:
            $ persistent.arilist.append("sex")
        scene arisex
        play sound "sexbed.mp3" fadein 0.1
        $ renpy.pause(13)
        stop sound fadeout 1
        scene black
        stop sound fadeout 2
        $ persistent.adatecount += 1
        if persistent.aending5 == False or persistent.epilogue > 0:
            $ persistent.aending5 = True
            show picenda6 at achievepos1 with moveinleft
            if persistent.story1 == False or persistent.epilogue > 0:
                $ persistent.story1 = True
                show picenda1 at achievepos2 with moveinleft
                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
            $ achievement_frame("","Tequila Shots","", xcenter = 0.1, yalign = 0.1)
        card "As you lie in bed at Ariane's side, enjoying the post coital afterglow,\nyou think back on the events of the night and Lydia's failed pass at Ariane.\n\nSuddenly you realized, you almost had a three way.\n\nTHE END"
        return
    else:
        a "If it is OK with [persistent.playername], then yeah we can go to my place and hang out."
        y "Yeah, its OK by me."
        l "Great, let me change into something more casual."
        a "By the way, I have a pool and a hot tub."
        l "Sounds nice, I'll grab a suit then, too."
        scene freeway3
        stop ambient fadeout 1
        "The three of you decide to go to Ariane's place and \"hang out\"."
        scene tercera1
        lb "Wow, nice place you have here. I want a place like this someday."
        a "Thank you. Aren't you a rock star?\nYou could easily get a house better than this."
        lb "Not a rock star yet. Maybe I can make enough on this tour\nto afford a house. Meanwhile, it's the hotel room life for me."
        a "I'm sure you will do fine. Let me give you the tour."
        scene tercera2
        play ambient "hottubloop.mp3" fadein 1
        "Inevitably, the tour ends up at the hot tub."
        lg "House checklist item number 6:\nMust have a hot tub."
        card ""
        lg "Got anything to drink here, Ariane?"
        a "I got some beer in the fridge, nothing stronger."
        $ menuplaceX = 0.5
        $ menuplaceY = 0.7
        menu:
            a "Let me go get it."
            "Why don't I go instead?":
                lg "Hey [persistent.playername], can you hand me my purse?"
                scene kitchenback
                stop ambient
                "You go grab three beers out of the fridge."
                scene tercera3
                play ambient "hottubloop.mp3" fadein 1
                "By the time you get back, the girls have started the party without you."
                label smokingdoob:
                scene tercera4
                a "Damn, that's good shit."
                lg "Music industry execs may be the scum of the earth,\nbut they know where to score the best weed."
                y "Here's your beer."
                if not "weed" in persistent.arilist:
                    $ persistent.arilist.append("weed")
                scene tercera5
                $ menuplaceX = 0.5
                $ menuplaceY = 0.7
                menu:
                    lg "Thanks, dude. Wanna hit?"
                    "Sure":
                        "Thanks"
                    "I think I'll pass.":
                        a "You don't mind if we..."
                        y "No, you two enjoy."
                scene tercera6
                "The party continues, not a lot of talking, just relaxing silently."
                y "So, uh..., you girls want to have a threesome?"
                scene tercera7
                "Ariane snorts with laughter."
                a "Sorry, that just sounded so blunt coming from you."
                lg "hehe, you said \"blunt\"."
                scene tercera7a
                a "Oh my god, Lydia!"
                y "Well we were talking about it earlier, and..."
                scene tercera6a
                a "I'm sorry, yeah we were. Shall we talk about it now?"
                lg "Are you sure, Ariane? You are the one in the middle after all."
                scene tercera7a
                "Ariane bursts with laughter again."
                a "That sounds like a lot of work on my part."
                scene tercera7
                a "Sorry guys, I'm just not feeling sexy anymore."
                y "What, no three way?"
                a "Aww, you sound so disappointed.\nIt was never a three way for you anyways."
                y "Still, I would've liked to watch."
                scene tercera7
                a "Yeah, I can tell. Your dick is already imagining it."
                y "Oops."
                a "Why don't you get out of the tub a while, and go make us some sandwiches."
                scene black
                stop ambient
                $ persistent.adatecount += 1
                if persistent.aending5 == False or persistent.epilogue > 0:
                    $ persistent.aending5 = True
                    show picenda6 at achievepos1 with moveinleft
                    if persistent.story1 == False or persistent.epilogue > 0:
                        $ persistent.story1 = True
                        show picenda1 at achievepos2 with moveinleft
                        $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                    $ achievement_frame("","Tequila Shots","", xcenter = 0.1, yalign = 0.1)
                card "So much for the promise of a threesome.\n\nTHE END"
                return
            "Why don't I go with you?":
                lg "Hey, can you hand me my purse?"
                y "Sure."
                scene tercera8
                stop ambient
                a "So, Muse, what do you think of making tonight an epic date..."
                a "By getting Lydia to join us in bed?"
                y "Are you sure? We had Rebecca in bed before, and all we did was sleep."
                a "I've known Rebecca too long, she will never be more than a friend."
                y "This is odd, I've never seen you attracted to another woman, before."
                a "Oh, there are occasionally others,\nbut I have never gone beyond the make out stage."
                a "Rebecca is too aggressive. I don't like aggressive.\nLydia is more of an artist, more demure, more inviting."
                y "A little more your type."
                a "Yes, I guess."
                y "And this means you feel up to a {i}menage a trois{/i} with me and another woman?"
                a "Sounds good for you, but I'll be the one in the middle in this scenario."
                $ menuplaceX = 0.5
                $ menuplaceY = 0.7
                menu:
                    a "Are you willing to share me with another woman?"
                    "Yes":
                        y "No matter how it turns out, this will be another memorable night."
                        a "I figured you would be up to it."
                        scene tercera9
                        play ambient "hottubloop.mp3" fadein 1
                        a "Lydia's carrying! Can I have a hit?"
                        lg "Sure."
                        scene tercera3
                        "Ariane takes a drag on Lydia's joint."
                        jump smokingdoob
                    "Since you put it that way, no.":
                        a "In that case, we won't."
                        y "Did you really want to?"
                        a "Part of me is willing, but part of me imagines it getting very awkward."
                        a "If you have doubts, than so do I."
                        a "What I want to do now is relax in the hot tub and drink some beer."
                        scene tercera9
                        play ambient "hottubloop.mp3" fadein 1
                        a "Lydia's carrying! Can I have a hit?"
                        lg "Sure."
                        scene tercera3
                        "Ariane takes a hit on Lydia's joint."
                        scene tercera4
                        a "Damn, that's good shit."
                        lg "Music industry execs may be the scum of the earth,\nbut they know where to score the best weed."
                        y "Here's your beer."
                        if not "weed" in persistent.arilist:
                            $ persistent.arilist.append("weed")
                        scene tercera5
                        $ menuplaceX = 0.5
                        $ menuplaceY = 0.7
                        menu:
                            lg "Thanks, dude. Wanna hit?"
                            "Sure":
                                "Thanks"
                            "I think I'll pass.":
                                a "You don't mind if we..."
                                y "No, you two enjoy."
                        scene tercera6
                        a "So Lydia, we were talking and I don't think either one of us is up for a threesome."
                        lg "I figured as much. Threesome's sound sexy,\nbut they can get a little weird."
                        lg "I'm good just relaxing naked in a hot tub,\nwith you cool people. Good way to end a crazy exciting day."
                        lg "I only offered because I wanted to have sex with Ariane anyways."
                        scene tercera7
                        "Ariane snorts with laughter."
                        a "Sorry, that just sounded a little blunt."
                        lg "hehe, you said \"blunt\"."
                        scene tercera7a
                        a "Oh my god, Lydia!"
                        lg "Wow, that wasn't that funny, no more weed for you, girl."
                        scene black
                        stop ambient
                        $ persistent.adatecount += 1
                        if persistent.aending5 == False or persistent.epilogue > 0:
                            $ persistent.aending5 = True
                            show picenda6 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("","Tequila Shots","", xcenter = 0.1, yalign = 0.1)
                        card "The three of you spend the night at Ariane's.\nLydia took the couch.\n\nThe next morning a limo arrives for Lydia.\n\nTHE END"
                        return
            "{i}Let Ariane go get the beer.{/i}":
                scene tercera10
                lg "So [persistent.playername], have you ever slept with two women before?"
                y "Well \"slept\" yes, had sex with two women at the same time, no."
                lg "I'd like to propose something in between then."
                y "What do you have in mind?"
                lg "I want to help you have sex with Ariane,\nin exchange for helping me have sex with Ariane."
                y "Well I have had sex with Ariane a few times not sure how you can help."
                lg "Oh I am sure I can help, I can make it better.\nBetter sex than you and Ariane have ever had."
                $ menuplaceX = 0.1
                $ menuplaceY = 0.7
                menu:
                    lg "What do you say, you in?"
                    "If Ariane is willing, then I am too.":
                        lg "Good to hear, let me do the talking then when she comes back."
                        jump threeway
                    "I'm not sure I want to share Ariane with you.":
                        lg "I get it, I thought I'd ask."
                        lg "I'm not sure Ariane would be willing anyways, she is obviously not gay."
                        y "She is not gay, no, but I know her well enough that she obviously likes you."
                        lg "You think so?"
                        y "I know so."
                        lg "That is reassuring to hear.  I've never had feeling for another\nsince I lost what I thought was the love of my life."
                        lg "Maybe there is hope for me after all."
                        y "I'm sure you will find another girlfriend."
                        lg "Thanks, well since there is not going to be sex tonight\ncould you get out and grab my purse for me?"
                        y "Sure."
                        "Lydia pulls out a joint and a cigarette lighter from her purse."
                        scene tercera9
                        a "Lydia's carrying! Can I have a hit?"
                        lg "Sure."
                        scene tercera3
                        "Ariane takes a drag on Lydia's joint."
                        if not "weed" in persistent.arilist:
                            $ persistent.arilist.append("weed")
                        scene tercera4
                        a "Damn, that's good shit."
                        lg "Music industry execs may be the scum of the earth,\nbut they know where to score the best weed."
                        scene tercera5
                        $ menuplaceX = 0.5
                        $ menuplaceY = 0.7
                        menu:
                            lg "Wanna hit?"
                            "Sure":
                                "Thanks"
                            "I think I'll pass.":
                                a "You don't mind if we..."
                                y "No, you two enjoy."
                        scene tercera6
                        lg "So Ariane, we were talking and I don't think either one of us is up for a threesome."
                        a "Actually, I wasn't sure I wanted to either."
                        lg "Good, we all want the same thing, then."
                        lg "I only offered a threesome because I wanted to have sex with you."
                        scene tercera7
                        "Ariane snorts with laughter."
                        a "Sorry, that just sounded a little blunt."
                        lg "hehe, you said \"blunt\"."
                        scene tercera7a
                        a "Oh my god, Lydia!"
                        lg "Wow, it wasn't that funny, no more weed for you, girl."
                        scene black
                        stop ambient
                        $ persistent.adatecount += 1
                        if persistent.aending5 == False or persistent.epilogue > 0:
                            $ persistent.aending5 = True
                            show picenda6 at achievepos1 with moveinleft
                            if persistent.story1 == False or persistent.epilogue > 0:
                                $ persistent.story1 = True
                                show picenda1 at achievepos2 with moveinleft
                                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
                            $ achievement_frame("","Tequila Shots","", xcenter = 0.1, yalign = 0.1)
                        card "The three of you spend the night at Ariane's.\nLydia took the couch.\n\nThe next morning a limo arrives for Lydia.\n\nTHE END"
                        return
        label threeway:
        y "So I don't get to touch you?"
        lg "Not in any sexual way, no.\nbut I could really use a back rub."
        y "Come over here then."
        scene tercera11
        a "Well, aren't the two of you looking all cozy together."
        lg "Nothing to get jealous about, he's just giving me a back rub."
        lg "Between the concert prep and the concert itself it has been a long day."
        a "Normally, I'd be OK with [persistent.playername] giving other women back rubs,\nbut you are both nearly naked in a hot tub, seems a bit sensual."
        lg "Well then you better come in and join us."
        scene tercera12
        a "Ahh, that feels nice."
        lg "When you are ready, we should move this to the bedroom."
        a "Hmmm, I don't know."
        lg "Having second thoughts? We can talk about it first."
        scene tercera6a
        a "Lydia, You obviously want to do this because you want me."
        lg "True."
        a "And you are aware, I'm not gay."
        lg "I got it, but I can tell from the bar, that you are attracted to me."
        a "OK, I'll admit that I find some women attractive, and you are one,\nbut I'm not going to go gay because of it."
        lg "Not asking you to. This was a big night for me, and \nI didn't want to spend it alone, or with a huge party crowd."
        lg "An intimate evening is all I am looking for.\nWhatever you are comfortable with, I will work with."
        a "That's good to hear. We have been dating a few times,\nand every date gets more and more epic."
        a "Our goal is to break the mold and do something different."
        lg "So you may be willing to explore new territory,\nthat's good for me to hear."
        a "Great, so where should we start?"
        lg "You really want to know? You don't just want to be spontaneous?"
        a "I've never been in a {i}menage a trois{/i} before,\nI'd be more comfortable if I knew what to expect."
        lg "OK, what would be comfortable for you?"
        a "I'm not sure?"
        lg "Well you and [persistent.playername] have had sex already, so that should make you comfortable."
        a "Yes, I'm comfortable with that."
        $ menuplaceX = 0.5
        $ menuplaceY = 0.7
        menu:
            lg "So why don't you two have sex while I watch?"
            "I'd be OK with that.":
                a "Not sure I am, we would be having sex with an audience."
                y "Just one person, it's not like we are having sex on stage at the {i}Live Cabaret{/i}."
                lg "And I would not just be watching, I would totally be masturbating along with you."
                a "That actually makes me more uncomfortable."
            "I'm already feeling performance anxiety thinking about it.":
                a "Me too, having sex with an audience?\nEven an audience of one would be intimidating."
                lg "Well, I would not just be watching, I would totally be masturbating along with you."
                a "That actually makes me more uncomfortable."
        lg "Very well, what if while you two are at it, I give you a back massage."
        a "Ummm..."
        lg "Let's just say I know the right places to rub during an orgasm."
        a "OK, I'm intrigued, that sounds like it could be very enjoyable."
        y "Great, it's agreed, let's get out of the hot tub and head to the bedroom."
        scene arisex3slow
        stop ambient
        play sound "sexbed2.mp3" fadein 0.1
        $ renpy.pause(9)
        stop sound fadeout 1
        scene tercera13
        stop sound fadeout 2
        a "Oh god, that was awesome sex!"
        scene tercera14
        l "Glad you liked it, now it is my turn."
        scene tercera15
        $renpy.pause(5)
        card ""
        scene tercera16
        a "Wait, what are we doing?"
        l "You had your orgasm, now its my turn."
        a "That seems fair, but how do we do this?"
        l "If you think about it too much, you will spoil the mood."
        a "Well it is already moving a little too fast for me."
        scene tercera14
        l "OK, what do you want to do?"
        a "If you want a great sexual experience, both [persistent.playername] and I can work together."
        l "What do you have in mind?"
        a "I'll handle foreplay, [persistent.playername] will handle oral sex."
        scene tercera17
        $ menuplaceX = 0.6
        $ menuplaceY = 0.8
        menu:
            a "He's pretty good, I coached him myself."
            "I think I can handle that job.":
                l "So Ariane makes out and fondles my boobs, while [persistent.playername] licks my pussy?"
                a "Yeah, tag team orgasm."
                l "Hmm, intriguing idea..."
            "Ariane, are you giving me permission to lick another woman's pussy?":
                a "Yeah, we made a goal to do something different,\nwe have never done this before."
                y "Yes, definitely a new experience for us."
                l "Wait, hold on guys, I'm the person in the middle, I get a say in this."
        scene tercera14
        l "I'd be willing to participate in this, on one condition..."
        l "[persistent.playername] will be the one to fondle my boobs, and Ariane will be the one to lick my pussy."
        a "Wait! That's..."
        scene tercera18
        l "It's easy Ariane, all you have to do is lick me right here and swirl your tongue around a bit."
        a "Yeee Ahhh Ahhh Ahhh Yesss!"
        scene tercera19
        a "I've never done anything like this to another woman."
        l "Find my clit, use your finger."
        a "Eww, gooey."
        l "Come on, you have certainly done this to yourself before."
        a "Yeah, but I didn't have to look at it."
        l "I get it you are uncomfortable doing something you have never done before.\nWhat can I do to make you more comfortable?"
        scene tercera20
        $ menuplaceX = 0.9
        $ menuplaceY = 0.7
        menu:
            a "I think [persistent.playername] needs to leave the room."
            "No way, I'm not leaving, I want to see this!":
                a "I'm sorry [persistent.playername], I can't do this with you watching me like that."
                a "You did your job Muse, now if you will go wait for me\n in the living room, I'll make it worth your while later."
                y "Oh very well, I'll wait in the living room."
                a "Thanks, [persistent.playername]."
            "If you don't feel comfortable, Ariane, maybe you shouldn't.":
                a "No no, I want to try this, I'd rather not do it my first time in front of you."
                a "Maybe the next time we have an orgy, I'll feel less self-conscious."
                y "Very well, for the promise of future orgies, I'll leave you alone."
            "If that's what you want, I'll leave the room.":
                a "Thank you, I'll make it up to you later."
                y "You'd better. If you need me back, I'll be on the couch masturbating."
                a "Take the box of tissues on my desk with you then."
        scene arihouse2
        card "You wait in the living room while screams, moaning, and giggling are coming out of the bedroom."
        scene tercera21
        card "After what seems like an hour, Ariane and Lydia come out,\nhug each other and say goodbye."
        a "I wish you didn't have to leave."
        lb "Tour bus leaves bright and early."
        scene tercera22
        "After Lydia leaves, Ariane grabs a beer and sits on the couch."
        a "I'm sorry [persistent.playername], I'm not ready to talk about it, yet."
        y "Very well, when you are ready."
        card ""
        scene tercera23
        "Suddenly Ariane's somber face turns to a satisfied grin\n(or is it a guilty grin?)"
        scene tercera24
        "Then she breaks into uncontrollable laughter so infectious\nthat you start joining in the giggle fest which goes quite a while."
        a "That's it, no more Tequila, ever!!!"
        if not "tercera" in persistent.arilist:
            $ persistent.arilist.append("tercera")
        scene black
        $ persistent.adatecount += 1
        if persistent.aending5 == False or persistent.epilogue > 0:
            $ persistent.aending5 = True
            show picenda6 at achievepos1 with moveinleft
            if persistent.story1 == False or persistent.epilogue > 0:
                $ persistent.story1 = True
                show picenda1 at achievepos2 with moveinleft
                $ achievement_frame("Finished a","Date With","Ariane", xcenter = 0.1, yalign = 0.4)
            $ achievement_frame("","Tequila Shots","", xcenter = 0.1, yalign = 0.1)
        card "Sex with two women did not go exactly the way you fantisized it.\nBut, your streak of adventurous dates with Ariane continues.\n\nTHE END"
        return