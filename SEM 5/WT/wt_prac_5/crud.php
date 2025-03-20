<?php 

$conn = mysqli_connect("localhost","root","");
$sql = "CREATE DATABASE IF NOT EXISTS techshop;";

$result = mysqli_query($conn, $sql);
if(!$result) {
    echo "something wrong while creating database: ". mysqli_error($conn);
} else {
    $conn = mysqli_connect("localhost","root","","techshop");
    
    $sql = "CREATE TABLE IF NOT EXISTS items(id BIGINT PRIMARY KEY AUTO_INCREMENT, cpu VARCHAR(50), gpu VARCHAR(50),memory VARCHAR(50));";
    $result = mysqli_query($conn, $sql);
    if(!$result) {
        echo "something wrong while creating table: ". mysqli_error($conn);
    }
    if(isset($_REQUEST["submit"])) {
        function add_item(){
            global $conn;
            $cpu = $_POST['inp_cpu'];
            $gpu = $_POST['inp_gpu'];   
            $memory = $_POST['inp_memory'];
            
            $cpu = trim($cpu);
            $gpu = trim($gpu);
            $memory = trim($memory);

            $sql = "INSERT INTO items (cpu, gpu, memory) VALUES ('$cpu', '$gpu', '$memory');" ;
            $result = mysqli_query($conn, $sql);
            if(!$result) {
                echo $sql, "<br>" , $cpu, "<br>";
                echo "Error while inserting into database". mysqli_error($conn);
            } else {
                echo '<script> alert("Data inserted Successfully"); </script>';
            }
        }
        add_item();
    }


}


?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <style>
        *{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body, html {
            height: 100%;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h1{
            font-size: 32px;    
        }

        form,table {
            width: 100%;
            /* height: 100%; */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        table {
            margin: 20px 0 0 0;
            width: 50%;
            text-align: center;
        }

        caption, h1{
            font-weight: 700;
            font-size: 32px;
            text-transform: uppercase;
        }

        td, th{
            min-width: 50px;
            padding: 5px;
        }
        .inp, .btn {
            width: 200px;
            margin-top: 10px;
        }
        .inp2{
            border: none    ;
            text-align: center;
        }
        .btn_box {
            border: none;
        }

        .btn2 { 
            width: 70px;
        }

    </style>

</head>

<body>
    <form action="crud.php"  method="post" enctype="multipart/form-data">
        <h1> Shop from here</h1>
        <input class = "inp" type = "text" id = "inp_cpu" name = "inp_cpu[]" class = "" placeholder="CPU name" required>
        <input class = "inp" type = "text" id = "inp_gpu" name = "inp_gpu[]" placeholder="GPU name" required>
        <input class = "inp" type = "text" id="inp_memory" name = "inp_memory[]" placeholder = "Memory" required>
        <button class = "btn" type = "submit" name = "submit"> Submit</button>
        <table border="1" Cellspacing ="10">
            <caption>Your List</caption>
            <tr>
                <th>ID</th>
                <th>CPU</th>
                <th>GPU</th>
                <th>MEMORY</th>
            </tr>
            <?php
                $sql = "SELECT * FROM items;";
                $result = mysqli_query($conn, $sql);
                if(mysqli_num_rows($result) > 0) {
                    while($row = mysqli_fetch_assoc($result)) {
                        echo "
                        <tr> 
                        <td>". $row['id']  ."  </td>
                        <td> <input class = 'inp2' id = ".$row['id']." value = ". $row['cpu']  .">  </td>
                        <td>". $row['gpu']  ."  </td>
                        <td>". $row['memory']  ."  </td>
                        <td class = 'btn_box'> <button class = 'btn2' type='submit' name='update' id=".$row['id']."> Update </td>
                        </tr>
                        
                        ";
                    }
                }
                ?>
    </table>
</form>
</body>

</html>