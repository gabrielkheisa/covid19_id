<?php
header('Content-Type: application/json; charset=utf-8');

$q = $_REQUEST["q"];
$key = "KEY";

if ($q == "")
{
    $myfile = fopen("cache.txt", "r") or die("Unable to open file!");
    $teks = fread($myfile, filesize("cache.txt"));
    fclose($myfile);

    $pieces = explode(",", $teks);

    $marks = array(
        "terkonfirmasi" => $pieces[0],
        "perawatan" => $pieces[1],
        "sembuh" => $pieces[2],
        "meninggal" => $pieces[3],
        "last_update" => $pieces[4],
        "server_update" => $pieces[5]
    );

    echo json_encode($marks, JSON_PRETTY_PRINT);
}
else
{
    $txt = base64_decode($q);

    $pieces = explode(",", $txt);

    if (strcmp($pieces[6], $key) == 0)
    {
        $myfile = fopen("cache.txt", "w") or die("Unable to open file!");
        fwrite($myfile, $txt);
        fclose($myfile);
        echo "Done!";
    }
    else
    {
        die("Key Invalid");
    }
}
?>
