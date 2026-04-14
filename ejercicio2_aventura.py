from random import random, choice, randint
from datetime import datetime 


def generar_nombre():
    heroes = ["Rayquaza","Pikachu","Salamance","Charizard","Gyarados","Espeon"]
    random_hero = choice(heroes)
    return random_hero

def generar_clase():
    type = ["Fuego","Volador","Dragon","Agua","Hada","Normal"]
    random_type = choice(type)
    return random_type

def generar_hp():
    HP = randint(80,120)
    return HP

def mostrar_fecha():
    ahora = datetime.now()
    print(ahora.date())

print("==Generador de Aventuras==")
mostrar_fecha()
print()
print("==Heroes Generados==")
for i in range(1,6):
    print(f"Heroe {i}: {generar_nombre()} / Clase: {generar_clase()} / HP: {generar_hp()}")
