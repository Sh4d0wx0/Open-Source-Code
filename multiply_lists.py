def multiplica_lista(n,lista):
    nova_lista = []
    for c in range(n):
        for x in range(len(lista)):
            nova_lista.append(lista[x])
    return nova_lista
