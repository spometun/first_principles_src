<?php
$SLEEP_INTERVAL = 0.5;
$MAX_WAITING_TIME = 20;
$OK_RESPONSE = 'ok';
$TOO_LONG_ERROR = 'update is too long';

$start_waiting_time = time();
$LANG = $_GET['lang'];

file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Triggering update from poeditor for language ".$LANG."\n" , FILE_APPEND);
$ch = curl_init("https://poeditor.com/api/webhooks/github?api_token=5b0d77bc255634323a31af2df41c1388&id_project=106095&language=".$LANG."&operation=export_terms_and_translations");
curl_exec($ch);

$was_update = filemtime("last_update") > $start_waiting_time;
$too_long = time() - $start_waiting_time > $MAX_WAITING_TIME;
while (!$was_update && !$too_long) {
  sleep($SLEEP_INTERVAL);
  clearstatcache();
  $was_update = filemtime("last_update") > $start_waiting_time;
  $too_long = time() - $start_waiting_time > $MAX_WAITING_TIME;
}

if ($was_update) {
  file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Update detected (lang = ".$LANG.")\n" , FILE_APPEND);
  echo 'ok';
}

if ($too_long) {
  file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Update is too long (lang = ".$LANG.")\n" , FILE_APPEND);
  echo 'update is too long';
}
?>
