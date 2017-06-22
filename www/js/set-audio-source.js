window.addEventListener('load', () => {
  const BASE_URL = '../../../audio';
  const audio = document.getElementById('audio');
  const audioExts = ['m4a', 'ogg', 'mp3'];
  for (const ext of audioExts) {
    const audioSource = document.getElementById('audio_link_' + ext);
    audioSource.src = [
      BASE_URL, '/', CUR_LANGUAGE.language, '/', PAGE_NAME, '.', ext
    ].join('');
  }
  audio.load();
});
