<?php
session_start();
include '5_6_db.php'; // Include the database creation code

if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Fetch the user from the database
    $sql = "SELECT * FROM user WHERE username = '$username'";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        $row = mysqli_fetch_assoc($result);

        // Verify the password
        if (password_verify($password, $row['password'])) {
            $_SESSION['username'] = $username;
            header("Location: 5_6_welcome.php");
        } else {
            echo "Incorrect password.";
        }
    } else {
        echo "No user found with this username.";
        header("Location: 5_6_reg.php");
    }
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
    <h1> Login Form</h1>
    <form method="post">
        <input type="text" name="username" placeholder="Enter username" required>
        <input type="password" name="password" placeholder="Enter password" required>
        <button type="submit" name="login">Login</button>
    </form>

</body>

</html>