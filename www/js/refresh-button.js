window.addEventListener('load',  () => {
  const updateContentURL = '/api/update-content/';

  withCurLanguage(({ language }) => {
    $('#refresh-button').bind('click', () => {
      fetch(updateContentURL + language, () => {
        location.reload();
      });
    });
  });
});
