<?php
session_start();
include '5_6_db.php'; // Include the database creation code

if (isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Check if the username already exists
    $check_user = "SELECT * FROM user WHERE username = '$username'";
    $res = mysqli_query($conn, $check_user);

    if (mysqli_num_rows($res) > 0) {
        echo "Username already exists.";
    } else {
        // Hash the password
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        // Insert the user into the database
        $sql = "INSERT INTO user (username, password) VALUES ('$username', '$hashed_password')";
        if (mysqli_query($conn, $sql)) {
            echo "Registration successful!";
            header("Location: 5_6_login.php");
        } else {
            echo "Error: " . mysqli_error($conn);
        }
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
    <form method="post">
        <h1> Registration Form</h1>
        <input type="text" name="username" placeholder="Enter username" required>
        <input type="password" name="password" placeholder="Enter password" required>
        <button type="submit" name="register">Register</button>
    </form>

</body>

</html>

