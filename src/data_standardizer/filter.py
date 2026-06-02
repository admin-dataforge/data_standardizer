def filtrar_atributos(lista_atributos):

  # se define un esquema inicial
  esquema_salida = {
      "area" : -1,
      "habitaciones" : -1,
      "banos" : -1,
      "parqueaderos" : 0
  }

  # aplciar filtros

  for item in lista_atributos:
    if 'm²' in item:
        esquema_salida['area'] = float(item.split()[0].replace(",","."))
    elif 'hab' in item:
        esquema_salida['habitaciones'] = int(item.split()[0])
    elif 'bañ' in item:
        esquema_salida['banos'] = float(item.split()[0])
    elif 'par' in item:
        esquema_salida['parqueaderos'] = int(item.split()[0])

  return esquema_salida