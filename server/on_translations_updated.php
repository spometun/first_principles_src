<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello God! Updated";
$src_path = file_get_contents('src_path.txt');
`cd {$src_path}; cd ../../lang; git pull; cd ../src/script; ./2_generate_translations.py`;

file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Language repository update\n" , FILE_APPEND);
?>

</body>
</html>
