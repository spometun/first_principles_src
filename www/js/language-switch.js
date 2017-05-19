window.onload = () => {
  const languageSelect = document.getElementById("language-select");
  const { pathname } = window.location;

  const makePattern = (language) => `/${language}/`;

  JSONS['languages'].then(languages => {
    let curLanguage;
    let curLanguagePattern;

    languages.forEach((language, i) => {
      const option = document.createElement('option');
      option.innerHTML = language;
      languageSelect.appendChild(option);

      const pattern = makePattern(language);
      if (pathname.includes(pattern)) {
        languageSelect.selectedIndex = i;
        $('#language-select').selectmenu('refresh', true);
        curLanguage = language;
        curLanguagePattern = pattern;
      }

    });

    languageSelect.addEventListener('change', () => {
      const { selectedIndex } = languageSelect;
      if (!pathname.includes(languages[selectedIndex])) {
        const newPattern = makePattern(languages[selectedIndex]);
        window.location = pathname.replace(curLanguagePattern, newPattern);
        console.log(window.location);
      }
    });
  });
};
