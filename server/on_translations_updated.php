<!DOCTYPE html>
<html>
<body>

<?php

echo "Hello God! Updated";
$src_path = file_get_contents('src_path.txt');
// src_path has line end character so semicolon isn't needed
`root_dir=$(pwd)/../; cd {$src_path} cd ../../lang; git pull; cd ../src/script; ./1_generate_translations.py \$root_dir`;

`touch last_update`;

file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Language repository update\n" , FILE_APPEND);
?>

</body>
</html>
