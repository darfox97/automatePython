# Con BeautifulSoup podremos analizar un HTML obtenido con requests.

import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/"
respuesta = requests.get(url, timeout=10)


# Para seleccionar elementos HTML por su clase usaremos punto (.) y por id usaremos almohadilla (#)
# print(preguntas[0])
for pagina in range(1, 5):
    print(f"\n--- PÁGINA {pagina} ---")
    textoHTML = respuesta.text
    soup = BeautifulSoup(textoHTML, "html.parser")
    preguntas = soup.select(".s-post-summary")
    for pregunta in preguntas:
        # get_text solo devuelve lo que hay dentro de a:
        titulo = pregunta.select_one(".s-link").get_text()
        usuario = pregunta.select_one(".s-user-card--link").get_text()
        print(f"Usuario {usuario.strip()}: \n\t- {titulo.strip()}")

    respuesta = requests.get(
        f"https://stackoverflow.com/questions?tab=newest&page={pagina+1}", timeout=10)
