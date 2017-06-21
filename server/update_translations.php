<?php
$SLEEP_INTERVAL = 0.5;
$MAX_WAITING_TIME = 20;

$start_waiting_time = time();
$LANG = $_GET['lang'];

file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Triggering translation update from poeditor (lang = ".$LANG.")\n" , FILE_APPEND);
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
  file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Update successfully finished (lang = ".$LANG.")\n" , FILE_APPEND);
  echo 'ok';
}

if ($too_long) {
  file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Update time out (lang = ".$LANG.")\n" , FILE_APPEND);
  echo 'update time out';
}
?>
