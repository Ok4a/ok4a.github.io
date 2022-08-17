<?php
session_start();
if (session_destroy()) {
  header("Location: ../eksamen/");
} else {
  header("Location: ../eksamen/index.php??error=fejl");
  }
?>
