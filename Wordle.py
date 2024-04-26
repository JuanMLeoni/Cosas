import random
from colorama import Fore

ArrayWords = ["lugar", "feliz", "dulce", "pazos", "cajas", "silla", "nubes", "flora", "mesa", "giras",
        "techo", "lunes", "mango", "nubes", "fleco", "salto", "cielo", "julio", "luzon", "pilas",
        "ruido", "miedo", "jabon", "blusa", "noche", "rojas", "fuego", "calle", "botas", "villa",
        "meson", "volar", "santo", "huevo", "fruta", "lunes", "pilar", "agua", "arena", "blusa",
        "flor", "cajas", "silla", "uvas", "manos", "flojo", "grito", "masas", "risas", "perro",
        "gente", "alma", "radio", "papel", "luzon", "balon", "quedo", "risas", "arroz", "nieve",
        "broma", "fotos", "jarro", "sobre", "camas", "juvas", "lento", "risas", "salon", "queso",
        "fruta", "trigo", "feste", "horma", "pausa", "clave", "risas", "futon", "donas", "risas",
        "tabla", "flota", "risas", "carro", "rocas", "meson", "risas", "fiesta", "copas", "risas"]

Word = random.choice(ArrayWords)
intentos = 6
while intentos > 0:
    entrada = input("Ingrese una palabra de 5 letras o escriba 'stop' para salir: ")
    
    if entrada == "stop":
        break
    
    if len(entrada) != 5:
        print("La palabra debe tener exactamente 5 letras.")
        continue
    
    if entrada == Word:
        print("¡Felicidades! La palabra era:", Fore.GREEN + Word + Fore.WHITE)
        break
    
    Checkeada = set()
    dentro = set()
    
    for i, letra in enumerate(entrada):
        if letra == Word[i]:
            Checkeada.add(letra)
        elif letra in Word:
            dentro.add(letra)
    
    resultado = ""
    for letra in entrada:
        if letra in Checkeada:
            resultado += Fore.GREEN + letra + Fore.WHITE
        elif letra in dentro:
            resultado += Fore.YELLOW + letra + Fore.WHITE
        else:
            resultado += Fore.BLACK + letra + Fore.WHITE
    
    print("Intenta de nuevo. Resultado:", resultado)
    print("Te quedan", intentos - 1, "intentos.\n")
    intentos -= 1

if intentos == 0:
    print("Se te acabaron los intentos. La palabra era:", Word)