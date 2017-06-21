const JSONS = {};
let CUR_LANGUAGE;
const jsonNames = ['languages'];
const { pathname } = window.location;

const withLanguages = (fn) => JSONS['languages'].then(fn);
const withCurLanguage = (fn) => CUR_LANGUAGE.then(fn);
const makePattern = (language) => `/${language}/`;

for (const jsonName of jsonNames) {
  JSONS[jsonName] = fetch(`../../${jsonName}.json`)
    .then(response => response.json());

  CUR_LANGUAGE = withLanguages(languages => {
    for (var i = 0; i < languages.length; i++) {
      const language = languages[i];
      const pattern = makePattern(language);
      if (pathname.includes(pattern)) {
        return { language, i, pattern };
      }
    }
  });
}
