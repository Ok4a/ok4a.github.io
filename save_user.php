<?php
//skaber database connection
include('user.php');

//tager brugerens input og laver til værdier
$username = $_POST['username'];
$password = $_POST['password'];
$gen_password = $_POST['gen_password'];

// ser om nogle af input felterne er tomme hvis en af dem er sender den dig tilbage med en fejlkode "error=empty"
if (empty($username) || empty($password) || empty($gen_password) ) {
  header("Location: ../eksamen/new_user.php?error=empty");
  exit;
} else {
//checker om kodeord blev gentaget rigtig hvis ikke sender den dig tilbage til ny bruger med en fejlkode "error=gen_psw"
if ($password !== $gen_password) {
  header("Location: ../eksamen/new_user.php?error=gen_psw");
} else {
  //henter bruger data for at se om brugernavet alderred er der
  $sql = "SELECT username FROM user WHERE username=?";
  $stmt = mysqli_stmt_init($conn);
//ser om stmt kan brues sammen med sql hvis ikke sender den sender den dig tilbage til start"
  if (!mysqli_stmt_prepare($stmt, $sql)) {
    header("Location: ../eksamen/new_user.php");
    exit();
  } else {
    //binder $username til ?
  mysqli_stmt_bind_param($stmt, "s", $username);
  mysqli_stmt_execute($stmt);
  mysqli_stmt_store_result($stmt);
  $resultcheck = mysqli_stmt_num_rows($stmt);
//checker om brugernavet er taget hvis det er sender den dig tilbage til ny bruger med en fejlkode "error=usertaken"
  if ($resultcheck > 0) {
    header("Location: ../eksamen/new_user.php?error=usertaken");
    exit();
  } else {
    //hvis username ikke findes. sætter den data ind i databasen og skaber en ny tabel
    $sql_bruger = "INSERT INTO user (username, password) VALUES ('$username','$password')";
    $sql_tabel = "CREATE TABLE user_$username ( id INT(11) AUTO_INCREMENT PRIMARY KEY, movie_id INT(11) NOT NULL, status TEXT NOT NULL)";

    if (mysqli_query($conn, $sql_bruger)) {
      if (mysqli_query($conn, $sql_tabel)) {
        session_start();  $_SESSION['username'] = $username;
        header('Location: ../eksamen/index.php');
      }
      } else {
        echo 'Error:'.$sql.'<br>'.mysqli_error($conn);
        }
      }
    }
  }
}
    mysqli_close($conn);
 ?>
