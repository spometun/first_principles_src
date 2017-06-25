window.addEventListener('load', () => {
  const BASE_URL = '../../../audio';

  const audio = document.getElementById('audio');
  audio.src = [
    BASE_URL, '/', CUR_LANGUAGE.language, '/', PAGE_NAME, '.mp3'
  ].join('');

  audio.addEventListener('loadeddata', () => {
    audio.style.display = '';
  });
  audio.load();
});
