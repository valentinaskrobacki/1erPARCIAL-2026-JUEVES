def organizar_eventos(eventos, descendente=False):
    #si la expresion es true, se ordena de forma descendente (Z a A)
    if descendente:
        return sorted(eventos, reverse=True)
    #caso contrario (o si no se envia parametro) se ordena ascendente (A a Z)
    else:
        return sorted(eventos)

        