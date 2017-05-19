const JSONS = {};
const jsonNames = ['languages'];

for (const jsonName of jsonNames) {
  JSONS[jsonName] = fetch(`../../jsons/${jsonName}.json`)
    .then(response => response.json());
}
