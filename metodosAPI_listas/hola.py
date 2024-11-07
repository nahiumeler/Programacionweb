lista=[
    {"ingrediente":"leche","cantidad":"2gr","marca":"la serenisima"},
    {"ingrediente":"cacao","cantidad":"20gr","marca":"nesquik"},
    {"ingrediente":"coca","cantidad":"100ml","marca":"pepsi"},
    {"ingrediente":"agua","cantidad":"200ml","marca":"glaciar"}

]


def agregar(ingrediente,cantidad,marca):
    diccionario={"ingrediente":ingrediente,"cantidad":cantidad,"marca":marca}
    lista.append(diccionario)
    return lista

def eliminar(ingrediente):
    for i in lista:
        if i["ingrediente"]==ingrediente:
            lista.remove(i)
            return lista


def editar(ingrediente,edicion,nuevo_valor):
    for i in lista:
        if i["ingrediente"]==ingrediente:
            i[edicion]=nuevo_valor
            return lista
        



