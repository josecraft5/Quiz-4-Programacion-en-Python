import ejercicio1_combate as comb

Heroe = "Chamber"
Enemigo = "Reyna"
hp_heroe = 100
hp_enemigo = 50

print("====Estado Inicial===")
print(f"Heroe empieza con {hp_heroe} HP ")
print(f"Enemigo empieza con {hp_enemigo} HP")
print()
daño1 = comb.calcular_daño(ataque=25,defensa=10)
ataque1= comb.realizar_ataque(Heroe,Enemigo,daño1)
daño_aplicado1 = comb.aplicar_daño(hp_enemigo,daño1)
comb.mostrar_estado(Enemigo, daño_aplicado1)
print()
daño2 = comb.calcular_daño(ataque=25,defensa=10)
ataque2= comb.realizar_ataque(Heroe,Enemigo,daño2)
daño_aplicado2 = comb.aplicar_daño(daño_aplicado1,daño2)
comb.mostrar_estado(Enemigo, daño_aplicado2)