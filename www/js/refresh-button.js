window.addEventListener('load',  () => {
  const updateContentURL = '../../../api/trigger_update_from_poeditor.php';

  withCurLanguage(({ language }) => {
    $('#refresh-button').bind('click', () => {
      fetch(updateContentURL, () => {
        location.reload();
      });
    });
  });
});
