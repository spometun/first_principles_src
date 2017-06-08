window.addEventListener('load', () => {

  const languageSelect = document.getElementById("language-select");
  const { pathname } = window.location;

  withLanguages(languages => {
    withCurLanguage(({ pattern }) => {
      languages.forEach(language => {
        console.log(language);
        const link = document.createElement('a');
        const newPattern = makePattern(language);
        link.href = pathname.replace(pattern, newPattern);

        const img = document.createElement('img');
        img.alt = language;
        img.title = language;
        img.src = `../../images/flags/${language}.png`;

        link.appendChild(img);

        languageSelect.appendChild(link);
        console.log(languageSelect);
      });
    });
  });
});
