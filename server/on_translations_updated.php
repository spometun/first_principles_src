<!DOCTYPE html>
<html>
<body>

<?php

echo "Hello God! Updated";

$src_path = file_get_contents('src_path.txt');
// src_path has line end character so semicolon isn't needed
file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."pulling translation update from github\n" , FILE_APPEND);
`cd {$src_path} cd ../../lang; git pull`;
file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Generating htmls\n" , FILE_APPEND);
`root_dir=$(pwd)/../; cd {$src_path} ./2_update_translation.py \$root_dir web all`;
file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."htmls generated\n" , FILE_APPEND);
`touch last_update`;
?>

</body>
</html>
