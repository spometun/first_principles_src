<!DOCTYPE html>
<html>
<body>

<?php

echo "Hello God! Updated";
file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."New translation update detected. Start updating htmls with new translations\n" , FILE_APPEND);
$src_path = file_get_contents('src_path.txt');
// src_path has line end character so semicolon isn't needed
`root_dir=$(pwd)/../; cd {$src_path} cd ../../lang; git pull; cd ../src/script; ./2_update_translation.py \$root_dir web all`;

`touch last_update`;

file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."htmls updated\n" , FILE_APPEND);
?>

</body>
</html>
