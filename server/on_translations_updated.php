<!DOCTYPE html>
<html>
<body>

<?php

echo "Hello God! Updated";

$script_path = file_get_contents('script_path.txt');
$lang = file_get_contents('requered_lang');
// script_path has line end character so semicolon isn't needed
file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."pulling translation update from github\n" , FILE_APPEND);
`cd {$script_path} cd ../../lang; git pull`;
file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Generating htmls\n" , FILE_APPEND);
`deployment_dir=$(pwd)/../; cd {$script_path} ./2_update_translation.py \$deployment_dir web {$lang}`;
file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."htmls generated\n" , FILE_APPEND);
`touch last_update`;
?>

</body>
</html>
