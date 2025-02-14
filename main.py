import random

# Diccionario con los verbos en inglés y sus formas
verbos = {
    "Arise": ("Arose", "Arisen"),
    "Awake": ("Awoke", "Awoken"),
    "Be": ("Was/Were", "Been"),
    "Bear": ("Bore", "Borne/Born"),
    "Beat": ("Beat", "Beaten"),
    "Become": ("Became", "Become"),
    "Begin": ("Began", "Begun"),
    "Bend": ("Bent", "Bent"),
    "Bet": ("Bet", "Bet"),
    "Bind": ("Bound", "Bound"),
    "Bid": ("Bid", "Bid"),
    "Bite": ("Bit", "Bitten"),
    "Bleed": ("Bled", "Bled"),
    "Blow": ("Blew", "Blown"),
    "Break": ("Broke", "Broken"),
    "Breed": ("Bred", "Bred"),
    "Bring": ("Brought", "Brought"),
    "Broadcast": ("Broadcast", "Broadcast"),
    "Build": ("Built", "Built"),
    "Burn": ("Burnt/Burned", "Burnt/Burned"),
    "Burst": ("Burst", "Burst"),
    "Buy": ("Bought", "Bought"),
    "Cast": ("Cast", "Cast"),
    "Catch": ("Caught", "Caught"),
    "Come": ("Came", "Come"),
    "Cost": ("Cost", "Cost"),
    "Cut": ("Cut", "Cut"),
    "Choose": ("Chose", "Chosen"),
    "Cling": ("Clung", "Clung"),
    "Creep": ("Crept", "Crept"),
    "Deal": ("Dealt", "Dealt"),
    "Dig": ("Dug", "Dug"),
    "Do": ("Did", "Done"),
    "Draw": ("Drew", "Drawn"),
    "Dream": ("Dreamt/Dreamed", "Dreamt/Dreamed"),
    "Drink": ("Drank", "Drunk"),
    "Drive": ("Drove", "Driven")
}

def practicar_verbos():
    verbo = random.choice(list(verbos.keys()))
    pasado_simple, participio = verbos[verbo]
    
    print(f"Verbo en infinitivo: {verbo}")
    respuesta_simple = input("Ingresa el pasado simple: ").strip()
    respuesta_participio = input("Ingresa el participio pasado: ").strip()
    
    if respuesta_simple.lower() in map(str.lower, pasado_simple.split("/")) and respuesta_participio.lower() in map(str.lower, participio.split("/")):
        print("¡Correcto!")
    else:
        print(f"Incorrecto. Respuestas correctas: Pasado simple: {pasado_simple}, Participio pasado: {participio}")

if __name__ == "__main__":
    while True:
        practicar_verbos()
        if input("¿Quieres intentar otro? (s/n): ").strip().lower() != 's':
            break
