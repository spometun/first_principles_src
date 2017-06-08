window.addEventListener('load',  () => {
  const updateContentURL = '../../../api/update_translations.php';

  $(document).ready(() => $('#refresh-button').closest('.ui-btn').show());

  const { language } = CUR_LANGUAGE;
  $('#refresh-button').bind('click', () => {
    fetch(updateContentURL, () => {
      location.reload();
    });
  });
});
