 <head>
   <meta charset="utf-8">
  <link rel="stylesheet" href="style.css"/>
   <title>Login</title>
 </head>
<body>
<form class="login" method="post" action="login_data.php" name="login">
    <?php
    //ser hvad fejlkodene er hvis der er en
    if (isset($_GET['error'])) {
      if ($_GET['error'] == "notlogin") {
        echo "<div class='form'> <a> Du er ikke loget ind login her </a></div>";
      }
      elseif ($_GET['error'] == "empty") {
        echo "<div class='form'> <a> Alle felter skal udfyldes </a></div>";
      }
      elseif ($_GET['error']== "fejl") {
      echo "<div class='form'> <a> Fejl under login </a></div>";
      }
    }
     ?>
     <br>
        <input class="login-input" type="text" name="username" placeholder="Username"/>
        <input class="login-input" type="password" name="password" placeholder="Password"/>
        <input class="login-button" type="submit" name="submit" value="Login"/>
      <br><br>  Ikke registreret? <a href="../eksamen/new_user.php"> <span>Opret en bruger</span></a> </br></br>
         <a href="../eksamen/">Tilbage til forsiden</a>
        </form>
  </body>
