<?php 
    include('5_1_data_re.php'); // ! if file not present it will continue to run
    // require('5_1_data_re.php'); // ! if file not present it will produce error and stop the execution

    echo date('Y-m-d'); 
    echo "<br>";
    echo date('H:i:s');
    echo "<br>";

    echo time();
    echo "<br>";
    echo mktime(0, 0, 0, 10, 6, 2024);
    echo "<br>";

    echo strtotime('next Monday'); 
    echo "<br>";
    echo strtotime('2024-12-25');
    echo "<br>";

    $dateInfo = getdate();
    echo "<br>";
    print_r($dateInfo);
    echo "<br>";

    if (checkdate(2, 29, 2024)) {
        echo 'Valid date';
        echo "<br>";
    } else {
        echo 'Invalid date';
        echo "<br>";
    }

    $date = date_create('2024-10-06');
    echo date_format($date, 'Y-m-d');
    echo "<br>";

    $date1 = date_create('2024-10-06');
    
    $date2 = date_create('2024-11-06');
    $diff = date_diff($date1, $date2);
    echo "<br>";
    echo $diff->format('%R%a days');
?>
