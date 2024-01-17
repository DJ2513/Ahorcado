from random import choice

lista_de_palabras = ['hola', 'bienvenido', 'zumo', 'paradigma', 'pregunta']
juego_terminado = False
vidas = 6
aciertos = 0
letras_correctas = []
letras_incorrectas = []


def elegir_palabra():
    palabra = choice(lista_de_palabras)
    letras_correctas = len(set(palabra))
    return palabra, letras_correctas


def pedir_letra():

    letra = ''
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    letra_correcta = False
    while not letra_correcta:
        letra = input('Elige una letra: ').lower()
        if letra in abecedario and len(letra) == 1:
            letra_correcta = True
        else:
            print("Haz ingresado una letra incorrecta o mas de una letra")

    return letra


def mostrar_palabra_oculta(palabra):
    lista_oculta = []
    for l in palabra:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))


def revisar_posible_victoria(palabra, letra_elegida, vidas, aciertos):
    fin_del_juego = False

    if letra_elegida in palabra:
        letras_correctas.append(letra_elegida)
        aciertos += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        print('Uyy se te acabaron los intentos! La palabra oculta era: ' + palabra)
        fin_del_juego = True
    elif aciertos == cantidad_letras:
        mostrar_palabra_oculta(palabra)
        print('¡Enhorabuena has ganado el juego!')
        fin_del_juego = True

    return vidas, fin_del_juego, aciertos


palabra, cantidad_letras = elegir_palabra()

while not juego_terminado:
    print("\n" + "*"*20 + "\n")
    mostrar_palabra_oculta(palabra)
    print(f'Vidas: {vidas}')
    print('Letras Incorrectas: ' + "-".join(letras_incorrectas))
    print("\n" + "*"*20 + "\n")

    letra_elegida = pedir_letra()
    vidas, fin, aciertos = revisar_posible_victoria(
        palabra, letra_elegida, vidas, aciertos)

    juego_terminado = fin
