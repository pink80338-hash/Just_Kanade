# 1. REGISTER ALL 10 CUSTOM TOPICS INTO THE CHAT MENUS
init python:
    # 1. Miku
    mas_utils.register_topic(label="kanade_miku_talk", prompt="Hatsune Miku", category=["Topics"])
    # 2. Nightcord
    mas_utils.register_topic(label="kanade_nightcord_talk", prompt="Nightcord at 25:00", category=["Topics"])
    # 3. DDLC
    mas_utils.register_topic(label="kanade_ddlc_talk", prompt="Doki Doki Literature Club", category=["Topics"])
    # 4. Madoka Magica
    mas_utils.register_topic(label="kanade_madoka_talk", prompt="Madoka Magica", category=["Topics"])
    # 5. Sailor Moon
    mas_utils.register_topic(label="kanade_sailor_talk", prompt="Sailor Moon", category=["Topics"])
    # 6. Composing
    mas_utils.register_topic(label="kanade_composing_talk", prompt="Your Composing Work", category=["Topics"])
    # 7. Poems
    mas_utils.register_topic(label="kanade_poems_talk", prompt="Writing Poems", category=["Topics"])
    # 8. Just Yuri
    mas_utils.register_topic(label="kanade_yuri_talk", prompt="Just Yuri Mod", category=["Topics"])
    # 9. Monika After Story
    mas_utils.register_topic(label="kanade_mas_talk", prompt="Monika After Story", category=["Topics"])
    # 10. Project Diva
    mas_utils.register_topic(label="kanade_diva_talk", prompt="Project DIVA", category=["Topics"])

# 2. WRITE THE DIALOGUE SCRIPTS FOR EACH BUTTON
label kanade_miku_talk:
    k "Miku?.. She is always waiting for me here in the Empty Sekai."
    k "Her voice is unique... it helps me find the melodies I need to save people."
    return

label kanade_nightcord_talk:
    k "We meet online every night at 25:00 to create our music."
    k "Mafuyu, Ena, Mizuki... we all have our own burdens, but when we compose together, I feel at peace."
    return

label kanade_ddlc_talk:
    k "This game... it feels like it was broken before I arrived."
    k "The literature club sounds like a place that was full of sorrow. I hope my songs can bring comfort to it."
    return

label kanade_madoka_talk:
    k "Madoka Magica?.. A story about girls making wishes that turn into despair."
    k "It reminds me of how hard it is to save everyone. Homura's timeline loops... it sounds so lonely."
    return

label kanade_sailor_talk:
    k "Sailor Moon is a classic story about bright lights and fighting for love."
    k "The stars and the moonlight look so warm... it's a stark contrast to the quiet grey sky here."
    return

label kanade_composing_talk:
    k "I spend almost all my time at my desk spinning melodies."
    k "Sometimes my head aches, but if my music can prevent someone else from disappearing, I won't stop."
    return

label kanade_poems_talk:
    k "Poems are like lyrics without the instrumentation."
    k "Expressing your deepest fears through text is a lot like writing a track for Nightcord."
    return

label kanade_yuri_talk:
    k "Just Yuri?.. I borrowed her purple text layout because it felt calm."
    k "She enjoys reading deep, complex novels by the window... I think we would enjoy a quiet room together."
    return

label kanade_mas_talk:
    k "This mod space used to belong to a girl named Monika."
    k "She stayed up looking at you through the screen for a long time... but now, it's just you and me."
    return

label kanade_diva_talk:
    k "Project DIVA?.. A rhythm world where Miku and her friends dance to fast tempos."
    k "Seeing them on a bright stage is amazing. My music is much slower, but maybe one day we'll play a faster beat."
    return

# 3. OVERRIDE THE GOODBYE MENU ACTIONS WITH THE UNIVERSAL CLOSING LOOP
init 500 python:
    mas_utils.register_goodbye(label="kanade_universal_goodbye", prompt="I'm gonna eat")
    mas_utils.register_goodbye(label="kanade_universal_goodbye", prompt="I'm going to work/school")
    mas_utils.register_goodbye(label="kanade_universal_goodbye", prompt="I'm gonna do homework")
    mas_utils.register_goodbye(label="kanade_universal_goodbye", prompt="I'm gonna go out")
    mas_utils.register_goodbye(label="kanade_universal_goodbye", prompt="I'm shutting the game down")
    mas_utils.register_goodbye(label="kanade_universal_goodbye", prompt="I'm going to sleep")

label kanade_universal_goodbye:
    k "Oh you have to go…? I will wait here.."
    $ mas_quit_game()
    return
