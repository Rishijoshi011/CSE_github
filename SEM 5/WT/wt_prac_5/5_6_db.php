<?php
    $conn = mysqli_connect("localhost", "root", "");

    $sql = "CREATE DATABASE IF NOT EXISTS login_sys";
    $result = mysqli_query($conn, $sql);
    if (!$result) {
        die("Error while creating db: " . mysqli_error($conn));
    }

    mysqli_select_db($conn, "login_sys");

    $sql = "CREATE TABLE IF NOT EXISTS user (
        id BIGINT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )";
    $result = mysqli_query($conn, $sql);
    if (!$result) {
        die("Error while creating table: " . mysqli_error($conn));
    }
?>
