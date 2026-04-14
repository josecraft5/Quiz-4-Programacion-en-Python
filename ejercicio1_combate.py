# SECCION II — Ejercicios Pr´acticos (6 puntos)

def calcular_daño(ataque,defensa):
    daño = ataque-defensa
    if daño<0:
        return 0 
    else:
        return daño
    
def aplicar_daño(hp_actual,daño):
    new_hp = hp_actual - daño
    if new_hp<0:
        return 0 
    else:
        return new_hp    

def mostrar_estado(nombre, hp, hp_max=100):
    print(f"{nombre}, HP: {hp}/{hp_max}")

def realizar_ataque(atacante,defensor,daño=0):
    print(f"!{atacante} ataca a {defensor} por {daño} de daño!!")


