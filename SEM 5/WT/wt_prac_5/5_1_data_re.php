<?php include('5_2_require.php'); ?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Retrival</title>
</head>

<body>
    <table border="1" Cellspacing="10">
        <caption style="font-size: 24px; font-weight: 600;">User data</caption>
        <tr>
            <th>user Id</th>
            <th>Display Name</th>
            <th>email id</th>
            <th>contact</th>
        </tr>
        <?php
        $sql = "SELECT * FROM user_table";
        $result = mysqli_query($conn, $sql);
        if (mysqli_num_rows($result) > 0) {
            while ($row = mysqli_fetch_assoc($result)) {
                echo "
                        <tr> 
                        <td>" . $row['user_id'] . "  </td>
                        <td>" . $row['display_name'] . "  </td>
                        <td>" . $row['email_id'] . "  </td>
                        <td>" . $row['contact'] . "  </td>
                        </tr>
                        
                        ";
            }
        }
        ?>
    </table>
</body>

</html>