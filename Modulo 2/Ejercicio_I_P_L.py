def adivinar_palabra(letra_prueba,palabra_intento, palabra_adivinar):
    letra_en_palabra = letra_prueba in palabra_adivinar
    print(f'¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}')

    longitud_correcta = len(palabra_intento) == len(palabra_adivinar)
    resultado_adivinanza = letra_en_palabra and longitud_correcta
    print(f'El jugador gana: {resultado_adivinanza}')

adivinar_palabra(letra_prueba = "m", palabra_intento = "mundo", palabra_adivinar = "mundo")