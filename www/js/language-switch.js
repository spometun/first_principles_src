window.addEventListener('load', () => {

  const languageSelect = document.getElementById("language-select");
  const { pathname } = window.location;

  withLanguages(languages => {
    languages.forEach(language => {
      const option = document.createElement('option');
      option.innerHTML = language;
      languageSelect.appendChild(option);
    });

    withCurLanguage(({ i, pattern }) => {
      // Change selection in language-select to current language
      languageSelect.selectedIndex = i;
      $('#language-select').selectmenu('refresh', true);

      // Add redirecting after changing language in language-select
      languageSelect.addEventListener('change', () => {
        const { selectedIndex } = languageSelect;
        if (i !== selectedIndex) {
          const newPattern = makePattern(languages[selectedIndex]);
          window.location = pathname.replace(pattern, newPattern);
        }
      });
    });
  });
});
