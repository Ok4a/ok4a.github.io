<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
<?php
include('login_test.php');

include('user.php');

session_start();

$user = $_SESSION['username'];

$sql_user = 'SELECT * FROM user_'.$user.'';
$result_user = mysqli_query($conn,$sql_user);

$sql_movie = 'SELECT * FROM movie';
$result_movie = mysqli_query($conn,$sql_movie);
$movie = mysqli_fetch_assoc($result_movie);

echo "<a href='index.php'>Tilbage til start</a><br><br>";

echo "<p> <font face='arial' size='5pt'>Velkommen  $user</font> </p>";




if (mysqli_num_rows($result_user)>0) {
  echo '<table style="border-collapse: collapse; font-family: arial;" border="1" cellpadding="10">';
  //data from each row
  while($row_user = mysqli_fetch_assoc($result_user)){

    $result_movie = mysqli_query($conn,$sql_movie);

    while ($row_movie = mysqli_fetch_assoc($result_movie)) {
      //Checker om en film er i film databasen også er i brugers data
      if ($row_movie['id'] == $row_user['movie_id']) {
        echo "<tr>";
        echo '<th><img src="'.$row_movie['picture'].'" style="height:175px;" />';
        echo "<th>".$row_movie['name'];
        echo '<th> Status:<br> '.$row_user['status'];

        //redigere status for film
        echo "<th><form method='post' action='edit_status.php'>";

        //informationen fra filmdata med til den nye side
        echo "<input type='hidden' name='edit' value='".$row_movie['id']."'>";
        echo "<input type='hidden' name='site' value='user'>";
        echo "<input type='submit' value='Edit Status' ></form>";
      }
    }

  }
}else {
  echo "Der er ingen film på din liste";
}


myqli_close($conn);
 ?>

 <!--Tilbage til start -->


  </body>
</html>
