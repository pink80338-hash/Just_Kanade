# 1. REGISTER ALL 10 CUSTOM TOPICS INTO THE CHAT MENUS
init python:
    # 1. Miku
    mas_submod_utils.register_topic(label="kanade_miku_talk", prompt="Hatsune Miku", category=["Topics"])
    # 2. Nightcord
    mas_submod_utils.register_topic(label="kanade_nightcord_talk", prompt="Nightcord at 25:00", category=["Topics"])
    # 3. DDLC
    mas_submod_utils.register_topic(label="kanade_ddlc_talk", prompt="Doki Doki Literature Club", category=["Topics"])
    # 4. Madoka Magica
    mas_submod_utils.register_topic(label="kanade_madoka_talk", prompt="Madoka Magica", category=["Topics"])
    # 5. Sailor Moon
    mas_submod_utils.register_topic(label="kanade_sailor_talk", prompt="Sailor Moon", category=["Topics"])
    # 6. Composing
    mas_submod_utils.register_topic(label="kanade_composing_talk", prompt="Your Composing Work", category=["Topics"])
    # 7. Poems
    mas_submod_utils.register_topic(label="kanade_poems_talk", prompt="Writing Poems", category=["Topics"])
    # 8. Just Yuri
    mas_submod_utils.register_topic(label="kanade_yuri_talk", prompt="Just Yuri Mod", category=["Topics"])
    # 9. Monika After Story
    mas_submod_utils.register_topic(label="kanade_mas_talk", prompt="Monika After Story", category=["Topics"])
    # 10. Project Diva
    mas_submod_utils.register_topic(label="kanade_diva_talk", prompt="Project DIVA", category=["Topics"])

# 2. WRITE THE DIALOGUE SCRIPTS FOR EACH BUTTON
label kanade_miku_talk:
    k "Miku?.. She is always waiting for me here in the Empty Sekai."
    k "Her voice is unique... it helps me find the melodies I need to save people."
    return

label kanade_nightcord_talk:
    k "We meet online every night at 25:00 to create our music."
    k "Mafuyu, Ena, Mizuki... we all have our own burdens, but when we compose together, I feel less alone."
    return

label kanade_ddlc_talk:
    k "A literature club... writing poems to find happiness."
    k "It sounds peaceful, but there's a heavy silence behind these walls."
    return

label kanade_madoka_talk:
    k "A magical girl carrying the weight of a cruel fate..."
    k "Her story makes my heart ache. I wish I could write a song that could save her from that despair."
    return

label kanade_sailor_talk:
    k "Fighting evil by moonlight... she is so bright and filled with hope."
    k "Sometimes, looking at someone so radiant makes me wonder if my melodies can ever reach that kind of light."
    return

label kanade_composing_talk:
    k "My synthesizer... my headset... this is all I need."
    k "I have to keep losing myself in the music. It is the only way I can save them."
    return

label kanade_poems_talk:
    k "Writing words down to express the darkness inside..."
    k "It is a lot like composing a melody. You capture a feeling before it completely consumes you."
    return

label kanade_yuri_talk:
    k "Yuri... she prefers reading alone in quiet spaces."
    k "I understand that comfort. Sometimes, the quietest rooms hold the deepest thoughts."
    return

label kanade_mas_talk:
    k "This classroom... a world built just for two people to talk forever."
    k "It feels a lot like my room. Just an endless loop of waiting and writing music."
    return

label kanade_diva_talk:
    k "Project DIVA... hitting every beat perfectly to keep the performance alive."
    k "It takes so much focus, but seeing everyone smile makes the long hours of practice worth it."
    return
