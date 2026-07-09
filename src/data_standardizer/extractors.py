def get_href(card):
  """
  retorna el href del inmueble tomado
  """
  href = card.find_all("a")[0]["href"]

  return href

def get_url_img(card):
  """
  retorna la url de la imagen
  """
  url_img = card.find_all("img")[0]["src"]

  return url_img

def get_alt_img(card):
  """
  retorna la informacion de alt de la imagen
  """

  alt_img = card.find_all("img")[0]["alt"]

  return alt_img


def get_barrio(card):
  """
  retorna la informacion del barrio
  """

  barrio = card.find_all("div", class_="property-card__detail-top__left")[0].find_all("div")[0].get_text(strip=True).split("|")[0]

  return barrio


def get_titulo(card):
  """
  retorna el titulo
  """
  titulo = card.find_all("div", class_="property-card__detail-title")[0].find_all("h2")[0].get_text(strip=True)

  return titulo

def get_precio_str(card):
  """
  retorna el precio en str
  """
  precio_str = "0.0"
  try:
    precio_str = card.find_all("div", class_="property-card__detail-price")[0].get_text(strip=True)
  except Exception as e:
    print(f"error {e}")

  return precio_str

def get_precio(precio_str):
  """
  retorna el precio en numeros
  """
  precio = int(precio_str.replace("$","").replace(".",""))

  return precio

def get_atributos(card):
  """
  Funcion que retorna los atributos de area,hab., banos. paq.
  """
  atributos = card.find_all("div", class_="pt-main-specs--feature")
  list_atributos = [ a.get_text(strip=True)  for a in atributos ]

  return list_atributos

def get_area(resultado_filtro):
  """
  retorna el area del inmueble
  """
  area = resultado_filtro["area"]

  return area

def get_habitaciones(resultado_filtro):
  """
  retorna la cantidad de habitaciones
  """
  hab = resultado_filtro["habitaciones"]

  return hab

def get_bano(resultado_filtro):
  """
  retorna la cantidad de baños, existe la posibilida de que sea 0.5 bano
  """
  bano = resultado_filtro["banos"]

  return bano

def get_parq_cant(resultado_filtro):
  """
  retorna la cantidad de parqueaderos
  """
  parq_cant = resultado_filtro["parqueaderos"]
  return parq_cant