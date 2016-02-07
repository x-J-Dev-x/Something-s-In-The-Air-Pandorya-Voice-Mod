# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice
# menuplace:
# 0 = upper right
# 1 = upper left
# 2 = lower left
# 3 = lower right
# 4 = lower center

screen choice(items):

    window:
        style "menu_window"
        xalign menuplaceX
        yalign menuplaceY
        
        vbox:
            style "menu"
            spacing 10

            for caption, action, chosen in items:
            
                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"
            
init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.35)
        xmaximum int(config.screen_width * 0.35)
        yminimum 60
    
    style menu_quarter_button is button:
        xminimum int(config.screen_width * 0.25)
        xmaximum int(config.screen_width * 0.25)
        yminimum 60
        
    style menu_eighth_button is button:
        xminimum int(config.screen_width * 0.18)
        xmaximum int(config.screen_width * 0.18)
        yminimum 50


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    if persistent.opening == 1:
        window:
            style "mm_root"
        imagemap:
            ground "title1.jpg"
            hover "title1hover.jpg"
        
            hotspot (490, 290, 300, 83) action Start()
            hotspot (495, 390, 290, 45) action ShowMenu("load")
            hotspot (530, 450, 225, 45) action ShowMenu("preferences")
            hotspot (540, 500, 225, 45) action Start("Endings")
            hotspot (565, 550, 140, 50) action Help()
            hotspot (575, 610, 130, 55) action Quit(confirm=False)
    elif persistent.opening == 2:
        window:
            style "mm_root"
        imagemap:
            ground "title2.jpg"
            hover "title2hover.jpg"
        
            hotspot (490, 290, 300, 83) action Start()
            hotspot (495, 390, 290, 45) action ShowMenu("load")
            hotspot (530, 450, 225, 45) action ShowMenu("preferences")
            hotspot (540, 500, 225, 45) action Start("Endings")
            hotspot (565, 550, 140, 50) action Help()
            hotspot (575, 610, 130, 55) action Quit(confirm=False)
    elif persistent.opening == 3:
        window:
            style "mm_root"
        imagemap:
            ground "title3.jpg"
            hover "title3hover.jpg"
        
            hotspot (490, 290, 300, 83) action Start()
            hotspot (495, 390, 290, 45) action ShowMenu("load")
            hotspot (530, 450, 225, 45) action ShowMenu("preferences")
            hotspot (540, 500, 225, 45) action Start("Endings")
            hotspot (565, 550, 140, 50) action Help()
            hotspot (575, 610, 130, 55) action Quit(confirm=False)
    elif persistent.opening == 4:
        window:
            style "mm_root"
        imagemap:
            ground "title6.jpg"
            hover "title6hover.jpg"
        
            hotspot (490, 290, 300, 83) action Start()
            hotspot (495, 390, 290, 45) action ShowMenu("load")
            hotspot (530, 450, 225, 45) action ShowMenu("preferences")
            hotspot (540, 500, 225, 45) action Start("Endings")
            hotspot (565, 550, 140, 50) action Help()
            hotspot (575, 610, 130, 55) action Quit(confirm=False)
    else:    
        window:
            style "mm_root"
        imagemap:
            ground "title7.jpg"
            hover "title7hover.jpg"
        
            hotspot (490, 290, 300, 83) action Start()
            hotspot (495, 390, 290, 45) action ShowMenu("load")
            hotspot (530, 450, 225, 45) action ShowMenu("preferences")
            hotspot (540, 500, 225, 45) action Start("Endings")
            hotspot (565, 550, 140, 50) action Help()
            hotspot (575, 610, 130, 55) action Quit(confirm=False)
    vbox:
        style "menu"
        spacing 10
        xpos .005
        ypos .95
        text "Dies ist eine modifizierte Version und ist möglicherweise instabil" style "menu_caption"
#init -2:

    # Make all the main menu buttons be the same size.
    #style mm_button:
    #    size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return() style "menu_eighth_button"
        textbutton _("Preferences") action ShowMenu("preferences") style "menu_eighth_button"
        textbutton _("Save Game") action ShowMenu("save") style "menu_eighth_button"
        textbutton _("Load Game") action ShowMenu("load") style "menu_eighth_button"
        textbutton _("Main Menu") action MainMenu() style "menu_eighth_button"
        textbutton _("Help") action Help() style "menu_eighth_button"
        textbutton _("Quit") action Quit() style "menu_eighth_button"

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Prequel Stuff")
                label _("See a list of pre configured Ariane first dates:")
                textbutton _("Prequel Menu") action ShowMenu("prequel") style "menu_choice_button" xalign 0.5
            
            frame:
                style_group "pref"
                has vbox
                
                label _("Press button to change to a different name the next time you play a new game")
                textbutton _("Clear Character Name") action [SetField(persistent, "playername", ""),ShowMenu("Inputname")] style "menu_choice_button" xalign 0.5
                label _("Or you can")
                textbutton _("Pick a name from a list") action ShowMenu("Pickname") style "menu_choice_button" xalign 0.5
                
        vbox:        
            frame:    
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window") style "menu_choice_button" xalign 0.5
                textbutton _("Fullscreen") action Preference("display", "fullscreen") style "menu_choice_button" xalign 0.5
                
            frame:    
                style_group "pref"
                has vbox

                label _("Soundtrack")
                textbutton _("Soundtrack On") action SetField(persistent, "soundtrack", True) style "menu_choice_button" xalign 0.5
                textbutton _("Soundtrack Off") action SetField(persistent, "soundtrack", False) style "menu_choice_button" xalign 0.5

            
        vbox:        
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume") xalign 0.5

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume") xalign 0.5
                
            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time") xalign 0.5
                    

                               
                        
screen prequel:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 4 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Normal Dates")
                textbutton _("Generic Date"):
                    action [SetField(persistent, "ldname", "generic date"),
                        Jump("GenericDate")]
                    xalign 0.5
                textbutton _("Downtown Diner"): 
                    action [SetField(persistent, "ldname", "downtown diner"),
                        Jump("DowntownDiner")]
                    xalign 0.5
                textbutton _("Downtown Restaurant"): 
                    action [SetField(persistent, "ldname", "downtown restaurant"),
                        Jump("DowntownRestaurant")]
                    xalign 0.5
                textbutton _("Quickie Date*"):
                    action [SetField(persistent, "ldname", "quickie date"),
                        Jump("QuickieDate")]
                    xalign 0.5
                textbutton _("Hot Tub Date*"):
                    action [SetField(persistent, "ldname", "hot tub date"),
                        Jump("HotTubDate")]
                    xalign 0.5
                textbutton _("Skinny Dipping*"): 
                    action [SetField(persistent, "ldname", "skinny dipping"),
                        Jump("SkinnyDipping")] 
                    xalign 0.5
            frame:
                style_group "pref"
                has vbox

                label _("Bad Dates")
                textbutton _("Out of Gas"):
                    action [SetField(persistent, "ldname", "out of gas"),
                        Jump("OutOfGas")]
                    xalign 0.5 
                textbutton _("Passed out drunk"):
                    action [SetField(persistent, "ldname", "passed out drunk"),
                        Jump("PassedOutDrunk")]
                    xalign 0.5 
            frame:
                style_group "pref"
                has vbox
                label _("* = Had sex at the end of the date. Two of the Ariane endings require one of these.")
        vbox:        
            frame:
                style_group "pref"
                has vbox

                label _("Beer Run Dates")
                textbutton _("Beer Run"):
                    action [SetField(persistent, "ldname", "beer run"),
                        Jump("BeerRun")]
                    xalign 0.5
                textbutton _("Bikini Beer Run"):
                    action [SetField(persistent, "ldname", "bikini beer run"),
                        Jump("BikiniBeerRun")]
                    xalign 0.5
                textbutton _("Naked Beer Run*"):
                    action [SetField(persistent, "ldname", "naked beer run"),
                        Jump("NakedBeerRun")]
                    xalign 0.5
                
            frame:
                style_group "pref"
                has vbox

                label _("Park Dates")
                textbutton _("Gymnastics"):
                    action [SetField(persistent, "ldname", "gymnastics"),
                        Jump("Gymnastics")]
                    xalign 0.5
                textbutton _("Bikini Basketball"):
                    action [SetField(persistent, "ldname", "bikini basketball"),
                        Jump("BikiniBasketball")]
                    xalign 0.5
                textbutton _("Fountain Photoshoot"):
                    action [SetField(persistent, "ldname", "fountain photoshoot"),
                        Jump("FountainPhotoshoot")]
                    xalign 0.5
                textbutton _("Naked Gymnastics*"):
                    action [SetField(persistent, "ldname", "naked gymnastics"),
                        Jump("NakedGymnastics")]
                    xalign 0.5
                textbutton _("Naked Basketball"): 
                    action [SetField(persistent, "ldname", "naked basketball"),
                        Jump("NakedBasketball")]
                    xalign 0.5    
            frame:
                style_group "pref"
                has vbox
                
                label _("Press button if you have done it all with Ariane:")
                textbutton _("Did It All!!"): #fffff
                    action [SetField(persistent, "ldname", "did it all"),
                        Jump("DidItAll")]
                    style "menu_choice_button"
                    xalign 0.5     
            
        vbox:        
            frame:
                style_group "pref"
                has vbox

                label _("Lake Dates")
                textbutton _("Romantic Date*"): #95736
                    action [SetField(persistent, "ldname", "romantic date"),
                        Jump("RomanticDate")]
                    xalign 0.5
                textbutton _("Lake Boating"): #d4d2
                    action [SetField(persistent, "ldname", "lake boating"),
                        Jump("LakeBoating")]
                    xalign 0.5
                textbutton _("Nude Skiing"): #ad436
                    action [SetField(persistent, "ldname", "nude skiing"),
                        Jump("NudeSkiing")]
                    xalign 0.5
                textbutton _("Walk on the beach*"): #d5716
                    action [SetField(persistent, "ldname", "walk on the beach"),
                        Jump("WalkOnTheBeach")]
                    xalign 0.5
                
            frame:
                style_group "pref"
                has vbox

                label _("Rebecca Dates")
                textbutton _("Met Rebecca"): #1a880
                    action [SetField(persistent, "ldname", "met rebecca"),
                        Jump("MetRebecca")]
                    xalign 0.5
                textbutton _("Marco Polo*"): #9af22
                    action [SetField(persistent, "ldname", "marco polo"),
                        Jump("MarcoPolo")]
                    xalign 0.5
                textbutton _("Strip Club Lost"): #2f821
                    action [SetField(persistent, "ldname", "strip club lost"),
                        Jump("StripClubLost")]
                    xalign 0.5
                textbutton _("Strip Club Won*"): #eff36
                    action [SetField(persistent, "ldname", "strip club won"),
                        Jump("StripClubWon")]
                    xalign 0.5
                textbutton _("Sleepover"): #aa8f6
                    action [SetField(persistent, "ldname", "sleepover"),
                        Jump("Sleepover")]
                    xalign 0.5        
            frame:
                style_group "pref"
                has vbox
                label _("Note: Be warned, changing the prequel date in the middle of the game may cause odd things to happen, including a game crash. Save your game before changing.") 
        vbox:        
            frame:
                style_group "pref"
                has vbox

                label _("Strip Club Dates")
                textbutton _("Dance and Lost"): #27081
                    action [SetField(persistent, "ldname", "dance and lost"),
                        Jump("DanceAndLost")]
                    xalign 0.5
                textbutton _("Strip to Undies Won*"): #a7206
                    action [SetField(persistent, "ldname", "strip to undies won"),
                        Jump("StripToUndiesWon")]
                    xalign 0.5
                textbutton _("Strip Nude and Won*"): #e7706
                    action [SetField(persistent, "ldname", "strip nude and won"),
                        Jump("StripNudeAndWon")]
                    xalign 0.5
                
            frame:
                style_group "pref"
                has vbox

                label _("Scenic View Dates")
                textbutton _("Makeout Interrupted"): #e0d2
                    action [SetField(persistent, "ldname", "makeout interrupted"),
                        Jump("MakeoutInterrupted")]
                    xalign 0.5
                textbutton _("Photoshoot"): #1e000
                    action [SetField(persistent, "ldname", "photoshoot"),
                        Jump("Photoshoot")]
                    xalign 0.5
                textbutton _("Nude Photoshoot*"): #1e206
                    action [SetField(persistent, "ldname", "nude photoshoot"),
                        Jump("NudePhotoshoot")]
                    xalign 0.5       
                textbutton _("Sex in Car*"): #7e606
                    action [SetField(persistent, "ldname", "sex in car"),
                        Jump("SexInCar")]
                    xalign 0.5   
                textbutton _("Oral Sex*"): #be706
                    action [SetField(persistent, "ldname", "oral sex"),
                        Jump("OralSex")]
                    xalign 0.5 
                
screen Pickname:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    style_group "prefs"
    xfill True
    # The left column.
    frame:
        vbox:
            hbox:
                textbutton _("Alex") action SetField(persistent, "playername", "Alex") style "menu_eighth_button"
                textbutton _("Bob") action SetField(persistent, "playername", "Brad") style "menu_eighth_button"
                textbutton _("Charles") action SetField(persistent, "playername", "Chuck") style "menu_eighth_button"
                textbutton _("Daniel") action SetField(persistent, "playername", "Daniel") style "menu_eighth_button"
                textbutton _("Ed") action SetField(persistent, "playername", "Eric") style "menu_eighth_button"
                textbutton _("Frank") action SetField(persistent, "playername", "Frank") style "menu_eighth_button"
                textbutton _("Gary") action SetField(persistent, "playername", "Gary") style "menu_eighth_button"
                textbutton _("Henry") action SetField(persistent, "playername", "Henry") style "menu_eighth_button"
            hbox:
                textbutton _("Isaac") action SetField(persistent, "playername", "Isaac") style "menu_eighth_button"
                textbutton _("John") action SetField(persistent, "playername", "John") style "menu_eighth_button"
                textbutton _("Kevin") action SetField(persistent, "playername", "Kevin") style "menu_eighth_button"
                textbutton _("Larry") action SetField(persistent, "playername", "Larry") style "menu_eighth_button"
                textbutton _("Michael") action SetField(persistent, "playername", "Michael") style "menu_eighth_button"
                textbutton _("Nick") action SetField(persistent, "playername", "Nick") style "menu_eighth_button"
                textbutton _("Omar") action SetField(persistent, "playername", "Omar") style "menu_eighth_button"
                textbutton _("Pete") action SetField(persistent, "playername", "Peter") style "menu_eighth_button"
            hbox:
                textbutton _("Quincy") action SetField(persistent, "playername", "Quincy") style "menu_eighth_button"
                textbutton _("Robert") action SetField(persistent, "playername", "Robert") style "menu_eighth_button"
                textbutton _("Steve") action SetField(persistent, "playername", "Steve") style "menu_eighth_button"
                textbutton _("Ted") action SetField(persistent, "playername", "Ted") style "menu_eighth_button"
                textbutton _("Upton") action SetField(persistent, "playername", "Upton") style "menu_eighth_button"
                textbutton _("Victor") action SetField(persistent, "playername", "Victor") style "menu_eighth_button"
                textbutton _("Will") action SetField(persistent, "playername", "Will") style "menu_eighth_button"
                textbutton _("Xander") action SetField(persistent, "playername", "Xander") style "menu_eighth_button"
            hbox:
                textbutton _("Yannis") action SetField(persistent, "playername", "Yannis") style "menu_eighth_button"
                textbutton _("Zach") action SetField(persistent, "playername", "Zach") style "menu_eighth_button"
                textbutton _("Dude") action SetField(persistent, "playername", "Dude") style "menu_eighth_button"
                textbutton _("Bozo") action SetField(persistent, "playername", "Bozo") style "menu_eighth_button"
                textbutton _("Sherlock") action SetField(persistent, "playername", "Sherlock") style "menu_eighth_button"
                textbutton _("Oberyn") action SetField(persistent, "playername", "Oberyn") style "menu_eighth_button"
                textbutton _("Clem") action SetField(persistent, "playername", "Clem") style "menu_eighth_button"
                textbutton _("Zaphod") action SetField(persistent, "playername", "Zaphod") style "menu_eighth_button"
            hbox:
                textbutton _("Joaquim") action SetField(persistent, "playername", "Joaquim") style "menu_eighth_button"
                textbutton _("Ahmed") action SetField(persistent, "playername", "Ahmed") style "menu_eighth_button"
                textbutton _("Miguel") action SetField(persistent, "playername", "Miguel") style "menu_eighth_button"
                textbutton _("Haruto") action SetField(persistent, "playername", "Haruto") style "menu_eighth_button"
                textbutton _("Deshi") action SetField(persistent, "playername", "Deshi") style "menu_eighth_button"
                textbutton _("Maxime") action SetField(persistent, "playername", "Maxime") style "menu_eighth_button"
                textbutton _("Igor") action SetField(persistent, "playername", "Igor") style "menu_eighth_button"
                textbutton _("Ragnar") action SetField(persistent, "playername", "Ragnar") style "menu_eighth_button"
            hbox:
                textbutton _("Mark") action SetField(persistent, "playername", "Mark") style "menu_eighth_button"
                textbutton _("Paul") action SetField(persistent, "playername", "Paul") style "menu_eighth_button"
                textbutton _("Chris") action SetField(persistent, "playername", "Chris") style "menu_eighth_button"
                textbutton _("Tom") action SetField(persistent, "playername", "Tom") style "menu_eighth_button"
                textbutton _("Joe") action SetField(persistent, "playername", "Joe") style "menu_eighth_button"
                textbutton _("Richard") action SetField(persistent, "playername", "Richard") style "menu_eighth_button"
                textbutton _("David") action SetField(persistent, "playername", "David") style "menu_eighth_button"
                textbutton _("James") action SetField(persistent, "playername", "James") style "menu_eighth_button"
            label _("\nClick \"Return\" once you are happy with your choice, or go back to \"Preferences\" and select \"Clear Character Name\" to pick your own.")

screen Inputname:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    style_group "prefs"
    xfill True
    vbox:
        xpos 0.5
        ypos 0.5
        xalign 0.5
        yalign 0.5
        if persistent.playername == "":
            text "Give your character a name:" color "#ffffff" xalign 0.5
            text "Press \"Return\" button on the right to save.\n" color "#ffffff" xalign 0.5
            input length 10 xalign 0.5 changed SetName
            textbutton "Or pick from a list" style "menu_choice_button" text_style "menu_choice" action ShowMenu("Pickname") xpos 0.5 ypos 0.7 xalign 0.5
        else:
            textbutton "You picked [persistent.playername]" style "menu_choice_button" text_style "menu_choice" action Return(persistent.playername)
        
                
init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 14
        idle_color "#cccc"
        hover_color "#ffff"
        selected_idle_color "#dd0d"
        selected_hover_color "#ff0"
        insensitive_color "#6668"

label GenericDate:
    $ persistent.ldname = "generic date"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label DowntownDiner: 
    $ persistent.ldname = "downtown diner"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = True 
    return
label DowntownRestaurant: 
    $ persistent.ldname = "downtown restaurant"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = True
    $ persistent.lddiner = False 
    return
label QuickieDate:
    $ persistent.ldname = "quickie date"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False 
    return
label HotTubDate:
    $ persistent.ldname = "hot tub date"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False 
    return
label SkinnyDipping: 
    $ persistent.ldname = "skinny dipping"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False 
    return
label OutOfGas:
    $ persistent.ldname = "out of gas"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return 
label PassedOutDrunk:
    $ persistent.ldname = "passed out drunk"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = True
    return 
label BeerRun:
    $ persistent.ldname = "beer run"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label BikiniBeerRun:
    $ persistent.ldname = "bikini beer run"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label NakedBeerRun:
    $ persistent.ldname = "naked beer run"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label Gymnastics:
    $ persistent.ldname = "gymnastics"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = True
    return
label BikiniBasketball:
    $ persistent.ldname = "bikini basketball"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label FountainPhotoshoot:
    $ persistent.ldname = "fountain photoshoot"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = True
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label NakedGymnastics:
    $ persistent.ldname = "naked gymnastics"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label NakedBasketball: 
    $ persistent.ldname = "naked basketball"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return    
label DidItAll: #fffff
    $ persistent.ldname = "did it all"
    $ persistent.ldeverything = True
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = True
    $ persistent.ldstripwon = True
    $ persistent.ldmtnphotos = True
    $ persistent.ldparkphotos = True
    $ persistent.ldrebecca = True
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = True
    $ persistent.lddiner = True
    return     
label RomanticDate: #95736
    $ persistent.ldname = "romantic date"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = True
    $ persistent.lddiner = False
    return
label LakeBoating: #d4d2
    $ persistent.ldname = "lake boating"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label NudeSkiing: #ad436
    $ persistent.ldname = "nude skiing"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label WalkOnTheBeach: #d5716
    $ persistent.ldname = "walk on the beach"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label MetRebecca: #1a880
    $ persistent.ldname = "met rebecca"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = True
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = True
    return
label MarcoPolo: #9af22
    $ persistent.ldname = "marco polo"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = True
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label StripClubLost: #2f821
    $ persistent.ldname = "strip club lost"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = True
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = True
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = True
    $ persistent.lddiner = False
    return
label StripClubWon: #eff36
    $ persistent.ldname = "strip club won"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = True
    $ persistent.ldstripwon = True
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = True
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = True
    $ persistent.lddiner = False
    return
label Sleepover: #aa8f6
    $ persistent.ldname = "sleepover"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = True
    $ persistent.ldnightclub = True
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return 
label DanceAndLost: #27081
    $ persistent.ldname = "dance and lost"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = False
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = True
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = True
    return
label StripToUndiesWon: #a7206
    $ persistent.ldname = "strip to undies won"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = False
    $ persistent.ldstrip = True
    $ persistent.ldstripwon = True
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label StripNudeAndWon: #e7706
    $ persistent.ldname = "strip nude and won"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = True
    $ persistent.ldstripwon = True
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label MakeoutInterrupted: #e0d2
    $ persistent.ldname = "makeout interrupted"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label Photoshoot: #1e000
    $ persistent.ldname = "photoshoot"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = False
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = False
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return
label NudePhotoshoot: #1e206
    $ persistent.ldname = "nude photoshoot"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = True
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return       
label SexInCar: #7e606
    $ persistent.ldname = "sex in car"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = True
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return   
label OralSex: #be706
    $ persistent.ldname = "oral sex"
    $ persistent.ldeverything = False
    $ persistent.ldhotdate = True
    $ persistent.ldnude = True
    $ persistent.ldpubnude = True
    $ persistent.ldstrip = False
    $ persistent.ldstripwon = False
    $ persistent.ldmtnphotos = True
    $ persistent.ldparkphotos = False
    $ persistent.ldrebecca = False
    $ persistent.ldnightclub = False
    $ persistent.ldrestaurant = False
    $ persistent.lddiner = False
    return 
         