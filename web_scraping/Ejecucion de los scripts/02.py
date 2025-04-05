# Import required libraries
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import time

# Make a GET request
req = requests.get('http://www.ilga.gov/senate/default.asp')
# Read the content of the server’s response
src = req.text
# View some output
print(src[:1000])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Parse the response into an HTML tree
soup = BeautifulSoup(src, 'lxml')
# Take a look
print(soup.prettify()[:1000])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Find all elements with a certain tag
a_tags = soup.find_all("a")
print(a_tags[:10])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
a_tags = soup.find_all("a")
a_tags_alt = soup("a")
print(a_tags[0])
print(a_tags_alt[0])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(len(a_tags))
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Get only the 'a' tags in 'sidemenu' class
side_menus = soup("a", class_="sidemenu")
side_menus[:5]
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Get elements with "a.sidemenu" CSS Selector.
selected = soup.select("a.sidemenu")
selected[:5]
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
## 🥊 Inicio Challenge: Find All
print ("🥊 Challenge: Find All")
# Encontrar todos los elementos <a> con la clase 'mainmenu'
mainmenu_links = soup.find_all("a", class_="mainmenu")

# Mostrar los primeros 5 elementos encontrados
print(mainmenu_links[:5])
## 🥊 Fin Challenge: Find All
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Get all sidemenu links as a list
side_menu_links = soup.select("a.sidemenu")

# Examine the first link
first_link = side_menu_links[0]
print(first_link)

# What class is this variable?
print('Class: ', type(first_link))
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(first_link.text)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(first_link['href'])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("## 🥊 Inicio Challenge: Extract specific attributes")
# Encontrar todos los elementos <a> con la clase 'mainmenu'
mainmenu_links = soup.find_all("a", class_="mainmenu")

# Extraer los atributos 'href'
hrefs = [link.get("href") for link in mainmenu_links if link.get("href")]

# Mostrar los primeros 5 enlaces
print(hrefs[:5])
print("## 🥊 Fin Challenge: Extract specific attributes")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Make a GET request
req = requests.get('http://www.ilga.gov/senate/default.asp?GA=98')
# Read the content of the server’s response
src = req.text
# Soup it
soup = BeautifulSoup(src, "lxml")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Get all table row elements
rows = soup.find_all("tr")
len(rows)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Returns every ‘tr tr tr’ css selector in the page
rows = soup.select('tr tr tr')

for row in rows[:5]:
    print(row, '\n')
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
example_row = rows[2]
print(example_row.prettify())
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
for cell in example_row.select('td'):
    print(cell)
print()

for cell in example_row.select('.detail'):
    print(cell)
print()

for cell in example_row.select('td.detail'):
    print(cell)
print()
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
assert example_row.select('td') == example_row.select('.detail') == example_row.select('td.detail')
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Select only those 'td' tags with class 'detail' 
detail_cells = example_row.select('td.detail')
detail_cells
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Keep only the text in each of those cells
row_data = [cell.text for cell in detail_cells]

print(row_data)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(row_data[0]) # Name
print(row_data[3]) # District
print(row_data[4]) # Party
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print('Row 0:\n', rows[0], '\n')
print('Row 1:\n', rows[1], '\n')
print('Last Row:\n', rows[-1])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Bad rows
print(len(rows[0]))
print(len(rows[1]))

# Good rows
print(len(rows[2]))
print(len(rows[3]))
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
good_rows = [row for row in rows if len(row) == 5]

# Let's check some rows
print(good_rows[0], '\n')
print(good_rows[-2], '\n')
print(good_rows[-1])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
rows[2].select('td.detail') 
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Bad row
print(rows[-1].select('td.detail'), '\n')

# Good row
print(rows[5].select('td.detail'), '\n')

# How about this?
good_rows = [row for row in rows if row.select('td.detail')]

print("Checking rows...\n")
print(good_rows[0], '\n')
print(good_rows[-1])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Define storage list
members = []

# Get rid of junk rows
valid_rows = [row for row in rows if row.select('td.detail')]

# Loop through all rows
for row in valid_rows:
    # Select only those 'td' tags with class 'detail'
    detail_cells = row.select('td.detail')
    # Keep only the text in each of those cells
    row_data = [cell.text for cell in detail_cells]
    # Collect information
    name = row_data[0]
    district = int(row_data[3])
    party = row_data[4]
    # Store in a tuple
    senator = (name, district, party)
    # Append to list
    members.append(senator)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Should be 61
len(members)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(members[:5])
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
# Hacer una solicitud GET a la página del Senado de Illinois
url = 'http://www.ilga.gov/senate/default.asp'
req = requests.get(url)

# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(req.text, 'lxml')

# Encontrar la tabla de senadores
senator_rows = soup.select("table[class='senate'] tr")

# Lista para almacenar la información
senators_info = []

# Iterar sobre las filas de la tabla
for row in senator_rows:
    # Extraer los datos de la fila
    cells = row.select("td.detail")
    
    if len(cells) >= 3:  # Verificar si la fila tiene datos válidos
        name = cells[0].text.strip()
        district = cells[1].text.strip()
        party = cells[2].text.strip()
        
        # Encontrar el enlace a los proyectos de ley del senador
        bill_link = row.select_one("a[href*='SenatorBills.asp']")
        
        if bill_link:
            relative_path = bill_link["href"]  # Obtener el 'href' relativo
            full_path = f"http://www.ilga.gov{relative_path}"  # Construir la URL completa
        else:
            full_path = "No disponible"  # En caso de que no haya enlace

        # Agregar los datos a la lista
        senators_info.append((name, district, party, full_path))

# Mostrar los primeros 5 resultados
for senator in senators_info[:5]:
    print(senator)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
