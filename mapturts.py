# script responsible for intialising all objects into the map as rectangle classes

import turtle
import items
import map as m  # imports necessary modules

#Chamber 1

room1c1 = m.Rectangle(-230, -170, -230, -170, "map", None)
room2c1 = m.Rectangle(-270, -230, -190, -180, "map", None)
room3c1 = m.Rectangle(-340, -270, -280, -150, "map", None)
room4c1 = m.Rectangle(-220, -210, -170, -120, "map", None)
room5c1 = m.Rectangle(-260, -160, -120, -60, "map", None)
room6c1 = m.Rectangle(-400, -340, -200, -190, "map", None)  # rooms in chamber 1

obj1c1 = m.Rectangle(-330, -325, -260, -255, "obj", items.apple)
obj2c1 = m.Rectangle(-225, -220, -65, -60, "obj", items.healthPotion)  # objects in chamber 1

rat1c1 = m.Rectangle(-320, -315, -240, -235, "enemy", items.giantRat)
rat2c1 = m.Rectangle(-245, -240, -80, -75, "enemy", items.giantRat)
rat3c1 = m.Rectangle(-210, -205, -70, -65, "enemy", items.goblin)
rat4c1 = m.Rectangle(-220, -215, -100, -95, "enemy", items.giantRat)
rat5c1 = m.Rectangle(-190, -185, -90, -85, "enemy", items.goblin)  # enemies in chamber 1

npc1c1 = m.Rectangle(-320, -315, -175, -170, "npc", items.level1)  # npcs in chamber 1

door1c1 = m.Rectangle(-400, -395, -200, -190, "door", items.level2Key)  # doors in chamber 1

#Chamber 2

room1c2 = m.Rectangle(-460, -400, -230, -160, "map", None)
room2c2 = m.Rectangle(-540, -460, -180, -170, "map", None)
room3c2 = m.Rectangle(-600, -540, -180, -110, "map", None)
room4c2 = m.Rectangle(-580, -570, -260, -180, "map", None)
room5c2 = m.Rectangle(-670, -540, -240, -230, "map", None)
room6c2 = m.Rectangle(-540, -480, -280, -210, "map", None)  # npc
room7c2 = m.Rectangle(-620, -560, -310, -260, "map", None)
room8c2 = m.Rectangle(-670, -660, -240, -180, "map", None)

obj1c2 = m.Rectangle(-440, -435, -225, -220, "obj", items.orange)
obj2c2 = m.Rectangle(-560, -555, -175, -170, "obj", items.orange)
obj3c2 = m.Rectangle(-575, -570, -130, -125, "obj", items.orange)
obj4c2 = m.Rectangle(-530, -525, -275, -270, "obj", items.orange)

taxC1c2 = m.Rectangle(-450, -445, -225, -220, "enemy", items.taxCollector)
taxC2c2 = m.Rectangle(-580, -575, -160, -155, "enemy", items.taxCollector)
taxC3c2 = m.Rectangle(-550, -545, -120, -115, "enemy", items.taxCollector)
taxC4c2 = m.Rectangle(-590, -585, -290, -285, "enemy", items.taxCollector)
airhead1c3 = m.Rectangle(-420, -415, -200, -195, "enemy", items.airhead)
airhead2c3 = m.Rectangle(-425, -420, -170, -165, "enemy", items.airhead)
airhead3c3 = m.Rectangle(-570, -565, -140, -135, "enemy", items.airhead)
airhead4c3 = m.Rectangle(-570, -565, -305, -300, "enemy", items.airhead)
airhead5c3 = m.Rectangle(-490, -485, -220, -215, "enemy", items.airhead)
airhead6c3 = m.Rectangle(-520, -515, -260, -255, "enemy", items.airhead)

npc1c2 = m.Rectangle(-530, -525, -230, -225, "npc", items.level2)

door1c2 = m.Rectangle(-670, -660, -185, -180, "door", items.level3Key)

#Chamber 3

room1c3 = m.Rectangle(-720, -660, -180, -140, "map", None)
room2c3 = m.Rectangle(-720, -710, -280, -180, "map", None)
room3c3 = m.Rectangle(-760, -690, -320, -280, "map", None)
room4c3 = m.Rectangle(-780, -720, -220, -210, "map", None)
room5c3 = m.Rectangle(-830, -780, -240, -190, "map", None)
room6c3 = m.Rectangle(-870, -830, -220, -210, "map", None)
room7c3 = m.Rectangle(-910, -870, -280, -200, "map", None)  # npc
room8c3 = m.Rectangle(-890, -880, -310, -280, "map", None)
room9c3 = m.Rectangle(-890, -820, -320, -310, "map", None)
room10c3 = m.Rectangle(-820, -790, -330, -300, "map", None)

obj1c3 = m.Rectangle(-885, -880, -270, -265, "obj", items.starfruit)
obj2c3 = m.Rectangle(-815, -810, -320, -315, "obj", items.starfruit)
obj3c3 = m.Rectangle(-755, -750, -310, -305, "obj", items.starfruit)
obj4c3 = m.Rectangle(-710, -705, -175, -170, "obj", items.starfruit)

taxC1c3 = m.Rectangle(-880, -875, -260, -255, "enemy", items.taxCollector)
taxC2c3 = m.Rectangle(-905, -900, -240, -235, "enemy", items.taxCollector)
taxC3c3 = m.Rectangle(-745, -740, -290, -285, "enemy", items.taxCollector)
meseeks1c3 = m.Rectangle(-760, -755, -310, -305, "enemy", items.taxCollector)
meseeks2c3 = m.Rectangle(-825, -820, -230, -225, "enemy", items.taxCollector)
meseeks3c3 = m.Rectangle(-740, -735, -305, -300, "enemy", items.taxCollector)

npc1c3 = m.Rectangle(-890, -895, -240, -235, "npc", items.level3)

door1c3 = m.Rectangle(-880, -870, -200, -195, "door", items.level4Key)

#Chamber 4

room1c4 = m.Rectangle(-880, -870, -200, -140, "map", None)
room2c4 = m.Rectangle(-870, -850, -150, -140, "map", None)
room3c4 = m.Rectangle(-850, -810, -180, -140, "map", None)
room4c4 = m.Rectangle(-930, -870, -140, -80, "map", None)
room5c4 = m.Rectangle(-870, -830, -90, -80, "map", None)
room6c4 = m.Rectangle(-780, -830, -120, -80, "map", None)
room7c4 = m.Rectangle(-790, -780, -150, -120, "map", None)
room8c4 = m.Rectangle(-790, -750, -180, -140, "map", None)  # npc
room9c4 = m.Rectangle(-1180, -930, -90, -80, "map", None)
room10c4 = m.Rectangle(-1420, -1180, -90, -80, "map", None)

dg1c4 = m.Rectangle(-845, -840, -160, -155, "enemy", items.dungeonGuardian)
dg2c4 = m.Rectangle(-920, -915, -110, -105, "enemy", items.dungeonGuardian)
dg3c4 = m.Rectangle(-760, -755, -155, -150, "enemy", items.dungeonGuardian)
dg4c4 = m.Rectangle(-980, -975, -85, -80, "enemy", items.dungeonGuardian)
dg5c4 = m.Rectangle(-1030, -1025, -90, -85, "enemy", items.dungeonGuardian)
dg6c4 = m.Rectangle(-1160, -1155, -85, -80, "enemy", items.dungeonGuardian)
dg7c4 = m.Rectangle(-1220, -1215, -90, -85, "enemy", items.dungeonGuardian)
dg8c4 = m.Rectangle(-1280, -1275, -85, -80, "enemy", items.dungeonGuardian)
dg9c4 = m.Rectangle(-1330, -1325, -90, -85, "enemy", items.dungeonGuardian)
dg10c4 = m.Rectangle(-1395, -1390, -85, -80, "enemy", items.dungeonGuardian)

npc1c4 = m.Rectangle(-770, -765, -160, -155, "npc", items.level4)

door1c4 = m.Rectangle(-1420, -1415, -90, -80, "door", items.exitKey)
