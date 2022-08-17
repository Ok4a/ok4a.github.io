<head>
  <meta charset="utf-8">
 <link rel="stylesheet" href="style.css"/>
  <title>Opret bruger</title>
</head>
  <body>
<form class="login" method="post" action="save_user.php">
<?php
//tager fejlkoden fra urlen og skriver fejkoden med echo
if (isset($_GET['error'])) {
  if ($_GET['error'] == "usertaken") {
    echo "<div class='form'> <a> brugernavn er taget </a></div>";
  }
  elseif ($_GET['error'] == "gen_psw") {
    echo "<div class='form'> <a> kodeord blev ikke gentaget rigtig </a></div>";
  }
  elseif ($_GET['signup'] == "success") {
    echo "<div class='form'> <a> Tilmelding fuldført </a></div>";
  }
  elseif ($_GET['error'] == "empty") {
    echo "<div class='form'> <a> Alle felter skal udfyldes </a></div>";
    }
  }
?>
<br>
<!--input felt -->
  <input class="login-input" type="text" name="username" placeholder="Username"/>
  <input class="login-input" type="password" name="password" placeholder="Password"/>
  <input class="login-input" type="password" name="gen_password" placeholder="Repeat Password"/>
  <input class="login-button" type="submit" name="submit" value="Opret bruger"/>
  <br><br>  Har en bruger? <a href="../eksamen/login.php"> <span>Login</span></a> </br></br>
     <a href="../eksamen/">Tilbage til forsiden</a>
  </form>
</body>
