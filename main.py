def on_on_chat():
    pass
player.on_chat("run", on_on_chat)

for index in range(4):
    mobs.spawn(PANDA, pos(0, 1, 0))