# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ref = Character("Referee")

define game_background = Image("game_play_background.jpg")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene game_play_background 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show team_with_bot

    # These display lines of dialogue.

    ref "Line up to be inspected! Make sure to organize your
    team tables before we call people over to the drivers meeting."

    ref "Get ready FTC teams!"


    scene ftc_inspection
    with fade 

    ref "Line up for inspection"

    ref "Your bot is outside of the sizing limit"
    menu:
        "Make quick changes to be inside the 18x18":
            "Go back to your table and start making changes"
            jump go_to_table

        "Go home":
            "Leave the comp and hope that you do better next time"
            jump end_game
            #return
    
    
    # This ends the game.

    return

label go_to_table:
    "You rush back to your table and clip your flywheel intake. You are inside the 18x18"

    scene game_play_background 

    ref "Match schedule is out. Match 1 and 2 line up for queueing"

    return

label end_game:
    "You wave goodbye and head home. Next comp, you will be more prepaired"
    return