const JSONS = {};
const jsonNames = ['languages'];

for (const jsonName of jsonNames) {
  JSONS[jsonName] = fetch(`../../${jsonName}.json`)
    .then(response => response.json());
}
