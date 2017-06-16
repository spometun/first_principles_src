const makePattern = (language) => `/${language}/`;
const { pathname } = window.location;

const PAGE_NAME = pathname.slice(pathname.lastIndexOf('/') + 1);

let CUR_LANGUAGE;
for (var i = 0; i < LANGUAGES.length; i++) {
  const language = LANGUAGES[i];
  const pattern = makePattern(language);
  if (pathname.includes(pattern)) {
    CUR_LANGUAGE = { language, i, pattern };
    break;
  }
}

