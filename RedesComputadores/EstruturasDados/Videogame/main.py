from datetime import datetime
from videogame import Videogame

console3 = Videogame(datetime.now(), "Nintendo", "Nintendo WII")
console1 = Videogame()
console2 = Videogame(datetime.now(), "XBOX", "Xbox360")

console1.jogos_instalados.append("Crash")
console1.jogos_instalados.append("God of War")

print(console1)
print(console2)
print(console3)
