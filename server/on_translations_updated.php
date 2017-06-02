<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello God! Updated";
$output = shell_exec('date | cat >> updates.txt');
$src_path = file_get_contents('src_path.txt');
`cd {$src_path}; cd ../../lang; git pull; cd ../src/script; ./2_generate_translations.py`;
?>

</body>
</html>
