window.addEventListener('load',  () => {
  const updateContentURL = '../../../api/update_translations.php?lang=' + CUR_LANGUAGE.language;

  $(document).ready(() => $('#refresh-button').closest('.ui-btn').show());

  const { language } = CUR_LANGUAGE;
  const refreshButton = $('#refresh-button');
  refreshButton.bind('click', () => {
    fetch(updateContentURL).then(response =>
      response.blob().then(() => location.reload())
    );
    refreshButton.siblings('.ui-btn-inner')
      .find('.ui-btn-text').text("Refreshing...");
  });
});
