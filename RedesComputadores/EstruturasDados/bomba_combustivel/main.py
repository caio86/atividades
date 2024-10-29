# lamp = Lampada(4000, 50)
# print(lamp.cor)
# print(lamp.potencia)
# print(lamp.ligada)
#
# lamp2 = Lampada(6000, 30, True)
# print(lamp2.cor)
# print(lamp2.potencia)
# print(lamp2.ligada)
#
# tv1 = Televisao(5, 0)
# tv1.sintonizar_canal(7)
# tv1.aumentar_volume(10)
# tv1.diminuir_volume()
# print(tv1)


from bomba import BombaDeCombustivel, Combustivel


bomba1 = BombaDeCombustivel(1)
gasolina = Combustivel("gasolina", 6.20, 500)
etanol = Combustivel("etanol", 4.80, 400)
bomba1.combustiveis.append(gasolina)
bomba1.combustiveis.append(etanol)
print(bomba1)
