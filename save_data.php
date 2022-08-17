<?php
include("user.php");


//Check forbindelsen til serveren
if ($conn) {
  echo "Connection successful<br><br>";
} else {
  die('Connection faild:'.mysqli_connect_error());
}



    //Function der kan cheke file type
    function GetImageExtension($imagetype)
   	 {
       if(empty($imagetype)) return false;
       switch($imagetype)
       {
           case 'image/bmp': return '.bmp';
           case 'image/gif': return '.gif';
           case 'image/jpeg': return '.jpg';
           case 'image/png': return '.png';
           default: return false;
       }
     }
//Er der uplaoded en fil
if (!empty($_FILES["uploadedimage"]["name"])) {
  //Information om fillen
	$file_name=$_FILES["uploadedimage"]["name"];
	$temp_name=$_FILES["uploadedimage"]["tmp_name"];
	$imgtype=$_FILES["uploadedimage"]["type"];
	$ext= GetImageExtension($imgtype);
	$imagename=$_FILES["uploadedimage"]["name"];
	$target_path = "images/".$imagename;

  //Yderlige informationer
  $name=$_POST["movie_name"];
  $runtime=$_POST["runtime"];

  if(move_uploaded_file($temp_name, $target_path)) {
    $sql = "INSERT INTO movie ( picture , name, runtime ) VALUES ('$target_path','$name', '$runtime')";
    if (mysqli_query($conn, $sql)) {
      echo "File uploaded<br>";
    }else {
      echo "File not uploaded";
    }
  }else{
    echo '<a href="index.php">Tilbage til forsiden</a>';
    exit("Error While uploading data to the server");
  }
}else {
  echo '<a href="index.php">Tilbage til start</a><br>';
  exit("Ingen file valgt");
}
echo '<a href="index.php">Tilbage til forsiden</a>';

mysqli_close($conn);
?>
