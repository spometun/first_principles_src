window.addEventListener('load',  () => {
  const updateContentURL = '../../../api/update_translations.php';

  $(document).ready(() => $('#refresh-button').closest('.ui-btn').show());

  withCurLanguage(({ language }) => {
    $('#refresh-button').bind('click', () => {
      fetch(updateContentURL, () => {
        location.reload();
      });
    });
  });
});
