window.addEventListener('load', () => {
  const BASE_URL = '../../../audio';
  const audio = document.getElementById('audio');
  const audioSource = document.getElementById('audio_link_mp3');  
  audioSource.src = [
    BASE_URL, '/', CUR_LANGUAGE.language, '/', PAGE_NAME, '.mp3'
  ].join('');
  audio.load();
});
