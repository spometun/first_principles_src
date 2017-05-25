window.addEventListener('load',  () => {
  const POEditorCommitURL = '#';

  withCurLanguage(({ language }) => {
    $('#refresh-button').bind('click', () => {
      fetch(POEditorCommitURL, () => {
        location.reload();
      });
    });
  });
});
