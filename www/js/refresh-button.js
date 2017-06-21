window.addEventListener('load',  () => {
  const OK_RESPONSE = 'ok';
  const TOO_LONG_ERROR = 'Update timeout. Looks like something went wrong. Try to reload page (press F5)';
  const REFRESH_BUTTON_TEXT = 'Refresh translation (' + CUR_LANGUAGE.language + ')';
  const REFRESH_BUTTON_REFRESHING_TEXT = 'Refreshing...';

  const updateContentURL = '../../../api/update_translations.php?lang=' + CUR_LANGUAGE.language;

  const changeButtonText = (button, text) => (
    button.siblings('.ui-btn-inner').find('.ui-btn-text').text(text)
  );

  const { language } = CUR_LANGUAGE;
  const refreshButton = $('#refresh-button');
  refreshButton.bind('click', () => {
    fetch(updateContentURL).then(response =>
      response.text().then(text => {
        console.log(text);
        switch (text) {
          case OK_RESPONSE: {
            location.reload();
          } break;
          case TOO_LONG_ERROR: {
            changeButtonText(refreshButton, REFRESH_BUTTON_TEXT);
            alert(text);
          } break;
        }
      })
    );
    changeButtonText(refreshButton, REFRESH_BUTTON_REFRESHING_TEXT);
  });
});
