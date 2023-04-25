# 🌳 🌊 🚁 🟩 ⬛️ 🔥 🏥 🧡 🪣 🏦 ⛅️ 🌩 🏆

from map import Map

tmp = Map(20, 10)
tmp.generate_forest(3, 10)
tmp.generate_river(10)
tmp.generate_river(10)
tmp.print_map()


tick = 1
while True:
    print('TICK', tick)
    tmp.print_map()
    tick += 1

