import requests
from bs4 import BeautifulSoup

def obtener_senadores(url):
    # Hacer una solicitud GET a la página
    req = requests.get(url)

    # Verificar si la página respondió correctamente
    if req.status_code != 200:
        print(f"Error: No se pudo acceder a la página (Código {req.status_code})")
        return []

    # Parsear el HTML con BeautifulSoup
    soup = BeautifulSoup(req.text, 'lxml')

    # Encontrar todas las filas de la tabla de senadores
    senator_rows = soup.select("table tr")

    # Lista para almacenar la información
    senators_info = []

    # Verificar si se encontraron filas
    if not senator_rows:
        print("No se encontraron filas de senadores.")
        return []

    # Iterar sobre las filas de la tabla
    for row in senator_rows:
        # Extraer los datos de la fila
        cells = row.select("td.detail")
        
        # Verificar si la fila tiene datos válidos (mínimo 3 celdas)
        if len(cells) >= 3:
            name = cells[0].text.strip()
            district = cells[1].text.strip()
            party = cells[2].text.strip()
            
            # Buscar el enlace a los proyectos de ley del senador
            bill_link = row.select_one("a[href*='SenatorBills.asp']")
            
            if bill_link:
                relative_path = bill_link["href"]  # Obtener el 'href' relativo
                full_path = f"http://www.ilga.gov{relative_path}"  # Construir la URL completa
            else:
                full_path = "No disponible"

            # Agregar la información a la lista
            senators_info.append((name, district, party, full_path))

    # Si la lista está vacía, informar
    if not senators_info:
        print("No se encontraron senadores en la tabla.")

    return senators_info

# URL de la página del Senado de Illinois
url = "http://www.ilga.gov/senate/default.asp"

# Llamar a la función y obtener los senadores
senadores = obtener_senadores(url)

print(len(senadores))

# Imprimir los primeros 5 senadores obtenidos
for senador in senadores[:5]:
    print(senador)
