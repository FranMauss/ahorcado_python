import random

ahorcado_ascii = [
        """
           ------
           |    |
           |    
           |    
           |    
           |    
        ========
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |    
        ========
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |    
        ========
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |    
        ========
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |    
        ========
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |    
        ========
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |    
        ========
        """
]

def generar_palabra():
    lista_palabras = [
        "ELEFANTE", "JIRAFA", "CANGREJO", "PINGÜINO", "COCODRILO",
        "ARGENTINA", "CANADA", "ESPAÑA", "JAPON", "ALEMANIA",
        "COMPUTADORA", "TELEVISOR", "MOCHILA", "MARTILLO", "RELOJ",
        "PIZZA", "HAMBURGUESA", "ESPAGUETI", "CHOCOLATE", "MANZANA",
        "MICROSCOPIO", "ROBOT", "SATELITE", "INTELIGENCIA", "PROGRAMACION",
        "AVENTURA", "UNIVERSO", "MAGIA", "HISTORIA", "TORMENTA"
    ]
    return random.choice(lista_palabras)

def pedir_letra(lista_letras):
    while True:
        letra = input("Introduce una letra: ").upper()
        if len(letra) == 1 and letra.isalpha():
            if letra not in lista_letras:
                lista_letras.append(letra)
                return letra
            else:
                print("Ya has introducido esa letra.")
        else:
            print("Introduce una sola letra válida.")

def comprobar_letra(letra, palabra, letras_adivinadas):
    if letra in palabra:
        letras_adivinadas.append(letra)
        print("Enhorabuena. La letra " + letra + " está en la palabra")
        return True
    print("Fallaste. La letra " + letra + " no está en la palabra")
    return False

def imp_palabra(palabra, letras_adivinadas):
    return " ".join(letra if letra in letras_adivinadas else "_" for letra in palabra)

def dibujo(vidas):
    return ahorcado_ascii[6-vidas]

def jugar():
    palabra = generar_palabra()
    vidas = 6
    lista_letras = []
    letras_adivinadas = []

    while True:

        print(dibujo(vidas))
        print(imp_palabra(palabra, letras_adivinadas))
        if not comprobar_letra(pedir_letra(lista_letras), palabra, letras_adivinadas):
            vidas = vidas - 1
            if vidas < 1:
                print("Has perdido.")
                break

        if set(palabra) == set(letras_adivinadas):
            print("Enhorabuena, has ganado.")
            break

jugar()