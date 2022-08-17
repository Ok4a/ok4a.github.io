<?php
include('user.php');
$username = $_POST['username'];
$password = $_POST['password'];

//Ser om input felder er tomme hvis de er sender den dig tilbage med fejlkode
if (empty($username) || empty($password) ) {
  header("Location: ../eksamen/login.php?error=empty");
  exit;
} else {

//henter data fra user
$result = mysqli_query($conn,"SELECT * FROM user WHERE username = '$username' and password = '$password'")
        OR die("Fejl".mysqli_error());

//laver det om til et array
$row = mysqli_fetch_array($result);


//Tjekker om username = $username. hvis det er lave en session men username og sender dig til index.php
if ($row['username'] == $username && $row['password'] == $password) {
        session_start();  $_SESSION['username'] = $username;
        header('Location: ../eksamen/');
} else {
    header("Location: ../eksamen/login.php?error=fejl");
  }
}
mysqli_close($conn);
?>
