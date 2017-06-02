window.addEventListener('load',  () => {
  const updateContentURL = '../../../api/update_translations.php';

  withCurLanguage(({ language }) => {
    $('#refresh-button').bind('click', () => {
      fetch(updateContentURL, () => {
        location.reload();
      });
    });
  });
});
