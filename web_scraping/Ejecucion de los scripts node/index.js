const axios = require('axios');
const cheerio = require('cheerio');

async function reto1() {
  console.log("===== Reto 1: Obtener y analizar una página web =====");
  try {
    const response = await axios.get('http://www.ilga.gov/senate/default.asp');
    const html = response.data;
    console.log("\nPrimeros 1000 caracteres del HTML:");
    console.log(html.substring(0, 1000));

    const $ = cheerio.load(html);
    console.log("\nHTML formateado (primeros 1000 caracteres):");
    console.log($.html().substring(0, 1000));

    // Obtener y mostrar los primeros 10 enlaces encontrados
    const links = $('a').slice(0, 10).map((i, el) => $(el).attr('href')).get();
    console.log("\nPrimeros 10 enlaces encontrados:");
    console.log(links);

    console.log("\nTotal de enlaces encontrados:", $('a').length);
  } catch (error) {
    console.error("Error en Reto 1:", error);
  }
}

async function reto2() {
  console.log("\n===== Reto 2: Extraer información de senadores =====");
  try {
    const { data } = await axios.get("http://www.ilga.gov/senate/default.asp");
    const $ = cheerio.load(data);
    let senatorsInfo = [];

    // Recorrer cada fila de la tabla y extraer los datos
    $('table tr').each((i, element) => {
      const cells = $(element).find('td.detail');
      if (cells.length >= 3) {
        const name = $(cells[0]).text().trim();
        const district = $(cells[1]).text().trim();
        const party = $(cells[2]).text().trim();
        const billLink = $(element).find("a[href*='SenatorBills.asp']").attr('href');
        const fullPath = billLink ? `http://www.ilga.gov${billLink}` : "No disponible";

        senatorsInfo.push({ name, district, party, fullPath });
      }
    });

    console.log(`\nNúmero de senadores extraídos: ${senatorsInfo.length}`);
    console.log("\nPrimeros 5 senadores:");
    console.log(senatorsInfo.slice(0, 5));
  } catch (error) {
    console.error("Error en Reto 2:", error);
  }
}

async function reto3() {
  console.log("\n===== Reto 3: Extraer información de proyectos de ley =====");
  try {
    const { data } = await axios.get('http://www.ilga.gov/senate/SenatorBills.asp?GA=98&MemberID=1911&Primary=True');
    const $ = cheerio.load(data);
    let bills = [];

    $('tr').each((i, element) => {
      const cells = $(element).find('td');
      if (cells.length >= 5) {
        const billId = $(cells[0]).text().trim();
        const description = $(cells[1]).text().trim();
        const chamber = $(cells[2]).text().trim();
        const lastAction = $(cells[3]).text().trim();
        const lastActionDate = $(cells[4]).text().trim();

        bills.push({ billId, description, chamber, lastAction, lastActionDate });
      }
    });

    console.log("\nPrimeros 5 proyectos de ley:");
    console.log(bills.slice(0, 5));
  } catch (error) {
    console.error("Error en Reto 3:", error);
  }
}

async function main() {
  console.log("Iniciando retos en Node.js...\n");
  await reto1();
  await reto2();
  await reto3();
}

// Ejecutar la función principal
main();
