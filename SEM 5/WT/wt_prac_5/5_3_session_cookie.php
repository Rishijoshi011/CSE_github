<?php
    session_start();
    if(isset($_REQUEST['submit'])){
        $name = trim($_POST['name']);
        $email_id = trim($_POST['email_id']);
        echo "checking: ", $name;
        $_SESSION['name'] = $name;
        $cookie = setcookie("email", $email_id, time() + 3600, "/");
        header('Location: http://localhost/wt_5/5_3_show.php');
    }    

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form method="post">
        <input type="text" id="name" name="name" placeholder="Joe mama">
        <input type="email" id="email_id" name="email_id" placeholder="example@gmail.com">
        <button type="submit" name="submit"> Submit</button>
    </form>
</body>

</html>