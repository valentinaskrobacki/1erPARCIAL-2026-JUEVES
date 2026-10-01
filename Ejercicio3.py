def total_interrupciones(a, b):
    #caso base: cuando las horas (b) llegan a 0, se detiene la recursion y retorna 0
    if b == 0:
        return 0
    #caso recursivo: sumamos las interrupciones de 1 hora (a) y llamamos a la func reduciendo la cant de hs en 1 (b-1)
    return a + total_interrupciones(a, b - 1)