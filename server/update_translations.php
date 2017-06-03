<!DOCTYPE html>
<html>
<body>

<?php
echo "Hello God!";
$ch = curl_init("https://poeditor.com/api/webhooks/github?api_token=5b0d77bc255634323a31af2df41c1388&id_project=106095&language=uk&operation=export_terms_and_translations");
curl_exec($ch);

file_put_contents('logs.txt', date("Y-m-d|H:i:s: ")."Call to poeditor webhook\n" , FILE_APPEND);
?>

</body>
</html>
