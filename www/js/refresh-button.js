window.addEventListener('load',  () => {
  const OK_RESPONSE = 'ok';
  const TOO_LONG_ERROR = 'Looks like something went wrong. Update timeout. Try to reload page (press F5)';
  const REFRESH_BUTTON_TEXT = 'Refreshing translation';
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
          case TOO_LONG_ERROR: {
            changeButtonText(refreshButton, REFRESH_BUTTON_TEXT);
            alert(text);
          } break;
        }
        location.reload();  
      })
    );
    changeButtonText(refreshButton, REFRESH_BUTTON_REFRESHING_TEXT);
  });
});
