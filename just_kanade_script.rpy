# 1. REGISTER THE SUBMOD SYSTEM
init python:
    mas_submod_utils.register_submod(
        id="just_kanade_total_conversion",
        name="Just Kanade",
        description="Replaces the game visuals and dialogue with Kanade Yoisaki and the Empty Sekai.",
        version="1.0.0",
        settings_pane=None
    )

# 2. SET UP KANADE'S DEEP PURPLE NAME AND YURI'S PURPLE TEXT BOX
define k = Character("Kanade", color="#664F8C", window_background="mod_assets/source/y_textbox.png")

# 3. OVERRIDE THE INITIAL MEETING LINE
label ch0_main_override:
    scene expression "mod_assets/location/empty_sekai.png" with fade
    show expression "mod_assets/monika/c/kanade_leaning.png" at t11
    k "Hi... Um, did you find me here in the Empty Sekai?"
    k "I'm glad you came... It's usually very quiet here."
    return

# 4. CUSTOM NICKNAME INTERACTION LOGIC
label mas_nickname_handling_override:
    $ player_input = mas_get_nickname_input()
    
    if player_input == "Mafuyu" or player_input == "mafuyu":
        k "How did you know her name?.."
        k "Mafuyu is a very dear friend of mine. Did she talk to you?"
        jump mas_nickname_rejected_loop
        
    elif player_input == "Ena" or player_input == "ena" or player_input == "Mizuki" or player_input == "mizuki":
        k "Wait... how do you know them?"
        k "They are the ones I make music with inside Nightcord. Have you been listening to our songs?"
        jump mas_nickname_rejected_loop
        
    elif player_input == "Father" or player_input == "father" or player_input == "Dad" or player_input == "dad":
        k "Dad?.."
        k "That word brings back a lot of memories."
        k "I'm still working hard to compose the song that will save everyone... just like he wanted."
        jump mas_nickname_rejected_loop

    else:
        # If they type a normal nickname, the game accepts it safely
        $ m.name = player_input
        k "Thank you... I will cherish the name [player_input]."
        return

label mas_nickname_rejected_loop:
    k "Could you please choose a different name for me instead?"
    call screen mas_nickname_input_screen
    return
