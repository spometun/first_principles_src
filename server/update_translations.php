<!DOCTYPE html>
<html>
<body>

<?php
$SLEEP_INTERVAL = 0.5;

$start_waiting_time = time();
$LANG = $_GET['lang'];

echo "Hello God!";
file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Triggering update from poeditor for language ".$LANG."\n" , FILE_APPEND);
$ch = curl_init("https://poeditor.com/api/webhooks/github?api_token=5b0d77bc255634323a31af2df41c1388&id_project=106095&language=".$LANG."&operation=export_terms_and_translations");
curl_exec($ch);

$needUpdate = true;
while ($needUpdate) {
  $last_update_time = filemtime("last_update");
  if ($last_update_time > $start_waiting_time) {
    break;
  }
  sleep($SLEEP_INTERVAL);
  clearstatcache();
}

file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Update detected (lang = ".$LANG.")\n" , FILE_APPEND);
?>

</body>
</html>
