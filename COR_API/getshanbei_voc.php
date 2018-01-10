<?php
$word = $_GET['word'];

$a = file_get_contents("https://api.shanbay.com/bdc/search/?word=".$word);
$c = $a;
$c = json_decode($c);
$b = file_get_contents("https://api.shanbay.com/bdc/example/?vocabulary_id={$c->data->content_id}&type=sys");
$b = json_decode($b);

$c->data->object_id = $b;
echo json_encode($c);
?>
