//
<?php

header('Content-Type: application/excel');
header('Content-Disposition: attachment; filename="sample.csv"');
$data = array(
        'email',
        'reason',
        'message'
);

$fp = fopen('php://output', 'w');
foreach ( $data as $line ) {
    $val = explode(",", $line);
    fputcsv($fp, $val);
}
fclose($fp);






//     $keys = array('email','reason', 'message');
//     $csv_line = array();
//     foreach($keys as $key){
//         array_push($csv_line,'' . $_GET[$key]);
//     }
//     $fname = 'contact.csv';
//     $csv_line = implode(',',$csv_line);
//     if(!file_exists($fname)){$csv_line = "\r\n" . $csv_line;}
//     $fcon = fopen($fname,'a');
//     $fcontent = $csv_line;
//     fwrite($fcon,$csv_line);
//     fclose($fcon);
// 
?>




