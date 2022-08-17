<?php
session_start();
include('user.php');

$user= $_SESSION['username'];

$result = mysqli_query($conn,"SELECT * FROM user WHERE username = '$user'")
        OR die("Fejl".mysqli_error());

$row = mysqli_fetch_array($result);

if (isset($_SESSION['username'])) {
  if ($row['username'] == $user) {

  }

} else {
    echo "Du er ikke logget ind <a href='../eksamen/login.php'> <span>Log in her</span></a> <br>";
  }

mysqli_close($conn);
 ?>
