<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <form action="index.php">
        <input type="submit" value="Tilbage til forsiden">
      </form>
    <?php
    echo "<br><br>";

    include('login_test.php');
    include('user.php');
if(!$conn){
  // her er hvad der sker hvis siden ikke kqn forbinde til databasen
echo "Der er sket en fejl".'<br>'.'  <form action="index.php">
      <input type="submit" value="Tilbage til forsiden">
      </form>';
}

    $sql="SELECT * FROM movie ORDER by name";
    $result_movie= mysqli_query($conn, $sql);

    if(mysqli_num_rows($result_movie)>0){
echo '<table style="border-collapse: collapse; font-family: arial;" border="1" cellpadding="10">';
// her sætter jeg fx. border collapse (som fjerner margenen mellem to borders), font, og cell padding
//(cell padding sætter hvor meget større cellerne bliver end teksten)
    while($row_movie=mysqli_fetch_assoc($result_movie)){
//$row er hvor mange rækker der er i tabellen som bliver sat af hvor mange resultater der bliver fundet

      echo '<tr>
          <th><img src="'.$row_movie['picture'].'" style="height:175px;" />
          <th> Navn: <br> '.$row_movie['name'].'
          <th>Spilletid: <br> '.$row_movie['runtime']."";


if (isset($_SESSION['username'])) {
  if ($row['username'] == $user) {
    //information til ændring af status
        echo '<th> <form action="edit_status.php" method="post">
              <input type="hidden" name="edit" value="'.$row_movie['id'].'">
              <input type="hidden" name="site" value="browse">
              <input type="submit" value="Edit" name="i_gang"/>
              </form>';
             //så bliver der bare sat rækker og kolonner ind
        }
      }
    }
  }
mysqli_close($conn);

     ?>

  </body>
</html>
