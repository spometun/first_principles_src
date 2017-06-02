<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello God! Updated";
$output = shell_exec('date | cat >> updates.txt');
`cd ~/first_principles/lang; git pull; cd ../src/script; sh run_all.sh`;
?>

</body>
</html>
