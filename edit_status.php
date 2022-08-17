<!DOCTYPE html>
<html lang="se" dir="ltr">
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
$movie_id= $_POST['edit'];
$chosen = $_POST['status'];
$site = $_POST['site'];

//Checker om man kommer fra en side og ikke bare skriver stigen i baren
if (!$site) {
  header("Location: ../eksamen/");

}

if(isset($_POST['update'])){

  //Har brugeren valgt at slette filmmen fra listen
  if ($chosen=='Slet') {
    $sql_delete = "DELETE FROM user_$user WHERE movie_id = $movie_id";

    if (mysqli_query($conn, $sql_delete)) {
      echo "Status Up";
      header("Location: ../eksamen/user_site.php");

    }else {
      echo "Fejl: Filmen belv ikke fjernet";
      echo "<a href='user_site.php'>Tilbage til bruger siden</a>";
    }

    }else {

      //kommer brugeren fra browse eller bruger siden
      if ($site == 'browse') {
        $sql_ny = "INSERT INTO user_$user (movie_id, status) VALUES ('$movie_id','$chosen')";
        if (mysqli_query($conn, $sql_ny)) {

          echo "<a href='browse.php'>Til browse</a><br>";
          echo "<a href='user_site.php'>Til bruger siden</a>";

        }else {
          echo "Fejl: Filmen blev ikke tilføjet";
          echo "<a href='browse.php'>Til Browse</a>";
        }

      }else {
        $sql_update = "UPDATE user_$user SET status = '$chosen' WHERE movie_id = $movie_id";

        if (mysqli_query($conn, $sql_update)) {
          header("Location: ../eksamen/user_site.php");

        }else {
          echo "Fejl: Status ikke opdatere";
          echo "<a href='user_site.php'>Tilbage til bruger siden</a>";


        }
      }
    }

  //Hvis der ikker er trykket på update
  }else {

    //En tilbage knap til browse eller bruger forsiden
    if ($site == 'browse') {
      echo "<a href='browse.php'>Til Browse</a>";
    }else{
      echo "<a href='user_site.php'>Til bruger siden</a>";
    }

    $result_movie = mysqli_query($conn, 'SELECT * FROM movie WHERE id ='.$movie_id);
    $movie = mysqli_fetch_array($result_movie);

    echo '<form action="" method="post">';
    echo '<table style="border-collapse: collapse;margin-left:auto;margin-right:auto; font-family: arial;" border="1" cellpadding="10">';

    //Finder det datasæt der skal bruges til filmen

    //billed og navn på film
    echo "<tr>";
    echo '<th><img src="'.$movie['picture'].'" style="height:175px;" />';
    echo "<th>".$movie['name'];

    //Hvad der skal statusen skal ændres til
    echo '<th> Status:<br>
            <select name="status">
              <option value="Planlagt">Planlagt</option>
              <option value="Igang">Igang</option>
              <option value="Færdig">Færdig</option>
              <option value="Slet">Slet</option>';

    //Tager noget information med videre om hvilken film det er
    echo '<input type="hidden" name="edit" value="'.$movie_id.'">';
    echo '<input type="hidden" name="site" value="'.$site.'">';

    echo '<input type="submit" name="update" value="update">';
  }


mysqli_close($conn);

 ?>


</body>
</html>
