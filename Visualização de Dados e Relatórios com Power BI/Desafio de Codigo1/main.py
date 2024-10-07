def filtrar_visuais(lista_visuais):
    visuais = lista_visuais.split(", ")
    visuais_unicos = set([visual.title() for visual in visuais])
    lista_final = sorted(visuais_unicos)
    
    return ", ".join(lista_final)

entrada_usuario = input()

saida = filtrar_visuais(entrada_usuario)
print(saida)
