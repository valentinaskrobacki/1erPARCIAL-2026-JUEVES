def total_donas(a, b):
    """
    calcula de forma iterativa el total de donas consumidas en una fiesta.
    
    parametros:
    a (int): donas por persona.
    b (int): cantidad de personas

    devuelve:
    el total de donas consumidas (int)
    """
    total = 0
    for _ in range(b):
        total += a
    return total
