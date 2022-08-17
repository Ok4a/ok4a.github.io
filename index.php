<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
    include('login_test.php');


    if (isset($_GET['error'])) {
      if ($_GET['error'] == "fejl") {
        echo "Du blev ikke logget ud";
      }
    }

    //er brugeren logget in
    if (isset($_SESSION['username'])) {
      if ($row['username'] == $user) {
        echo '<br><a href="user_site.php">Bruger</a> <br>';
        echo '<br><a href="browse.php">Browse</a><br>';
        echo '<br><a href="logout.php">Log ud</a>';
    }
    }else{
      echo '<br><a href="login.php">Log in</a> <br>';
      echo '<br><a href="new_user.php">Opret bruger</a> <br>';
      echo '<br><a href="browse.php">Browse</a><br>';
    }

      //admin
      if ($_SESSION['username'] == "andre") {
        echo '<br><br><a href="new_data.php">Tilføj ny film til databasen</a><br>';

      }

hello world
    ?>
  </body>
</html>
