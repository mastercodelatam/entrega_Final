import requests
from bs4 import BeautifulSoup

def get_bills(url):
    # Hacer la solicitud GET a la URL
    src = requests.get(url).text
    ##print(src[:1000])  # Imprimir los primeros 1000 caracteres del contenido HTML
    soup = BeautifulSoup(src, 'lxml')

    # Verificar la estructura de la página
    rows = soup.find_all('tr')

    bills = []

    for row in rows:
        # Buscar las celdas dentro de la fila
        cells = row.find_all('td')

        # Verificar si la fila contiene al menos 5 celdas
        if len(cells) >= 5:
            bill_id = cells[0].text.strip()  # Primer columna: ID del proyecto de ley
            description = cells[1].text.strip()  # Segunda columna: Descripción
            chamber = cells[2].text.strip()  # Tercera columna: Cámara (S o H)
            last_action = cells[3].text.strip()  # Cuarta columna: Última acción
            last_action_date = cells[4].text.strip()  # Quinta columna: Fecha de la última acción
            
            bill = (bill_id, description, chamber, last_action, last_action_date)
            bills.append(bill)

    return bills

# Llamada a la función con una URL de ejemplo
url = 'http://www.ilga.gov/senate/SenatorBills.asp?GA=98&MemberID=1911&Primary=True'
bills = get_bills(url)[0:5]
print(bills )
