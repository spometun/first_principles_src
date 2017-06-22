const makePattern = (language) => `/${language}/`;
const { pathname } = window.location;

const lastSlashIndex = pathname.lastIndexOf('/');
const lastDotIndex = pathname.lastIndexOf('.');
const PAGE_NAME = pathname.slice(lastSlashIndex + 1, lastDotIndex);

let CUR_LANGUAGE;
for (var i = 0; i < LANGUAGES.length; i++) {
  const language = LANGUAGES[i];
  const pattern = makePattern(language);
  if (pathname.includes(pattern)) {
    CUR_LANGUAGE = { language, i, pattern };
    break;
  }
}

